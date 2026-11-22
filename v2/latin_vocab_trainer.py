#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Łacina – słówka i odmiana w zdaniach. Uruchom: python latin_vocab_trainer.py"""
import random
import re
import tkinter as tk
import unicodedata
from tkinter import ttk, messagebox

from latin_data import WORD_GROUPS
from latin_practice import CASES, NUMBERS, make_questions


def normalized(text):
    """Porównanie bez rozróżniania wielkości liter i nadmiarowych spacji."""
    return re.sub(r"\s+", " ", unicodedata.normalize("NFC", text).casefold().strip())


def translations(text):
    """Średniki w bazie oznaczają alternatywne polskie tłumaczenia."""
    return [normalized(part) for part in text.split(";") if part.strip()]


class LatinTrainer(tk.Tk):
    """GUI obsługuje dwa tryby, wspólne statystyki i powtórki błędów."""

    def __init__(self):
        super().__init__()
        self.title("Łacina – trener słówek i zdań")
        self.geometry("860x745")
        self.minsize(710, 630)
        self.configure(bg="#f4f7fb")

        self.group_vars = {name: tk.BooleanVar(value=True) for name in WORD_GROUPS}
        self.mode = tk.StringVar(value="words")
        self.direction = tk.StringVar(value="mixed")
        self.repeat_errors = tk.BooleanVar(value=True)
        self.show_case = tk.BooleanVar(value=False)
        self.status = tk.StringVar(value="Wybierz tryb oraz grupy i rozpocznij naukę.")
        self.prompt = tk.StringVar(value="Gotowy do nauki?")
        self.question_label = tk.StringVar(value="")
        self.polish_sentence = tk.StringVar(value="")
        self.hint = tk.StringVar(value="")
        self.progress = tk.StringVar(value="Poprawne: 0   |   Błędne: 0   |   Pytania: 0")
        self.feedback = tk.StringVar(value="")
        self.explanation = tk.StringVar(value="")

        self.active_mode = None
        self.current = None
        self.current_direction = None
        self.checked = False
        self.deck = []
        self.pending_retry = []
        self.correct = self.wrong = self.asked = 0

        self._style()
        self._layout()
        self._mode_changed()
        self.bind("<Return>", self._enter)
        self.bind("<Control-n>", lambda _event: self.next_question())
        self.bind("<Escape>", lambda _event: self.answer_entry.delete(0, tk.END))

    def _style(self):
        style = ttk.Style(self)
        if "clam" in style.theme_names():
            style.theme_use("clam")
        style.configure("TFrame", background="#f4f7fb")
        style.configure("TLabel", background="#f4f7fb", foreground="#27364a", font=("Arial", 11))
        style.configure("Title.TLabel", font=("Arial", 21, "bold"), foreground="#172a44")
        style.configure("Sub.TLabel", font=("Arial", 10), foreground="#60748b")
        style.configure("Prompt.TLabel", font=("Arial", 22, "bold"), foreground="#123e72")
        style.configure("Polish.TLabel", font=("Arial", 14), foreground="#172a44")
        style.configure("Feedback.TLabel", font=("Arial", 12, "bold"))
        style.configure("TCheckbutton", background="#f4f7fb", font=("Arial", 10))
        style.configure("TRadiobutton", background="#f4f7fb", font=("Arial", 10))
        style.configure("TButton", font=("Arial", 11), padding=(12, 7))
        style.configure("Accent.TButton", font=("Arial", 11, "bold"), padding=(14, 8))
        style.configure("TLabelframe", background="#f4f7fb")
        style.configure("TLabelframe.Label", background="#f4f7fb", font=("Arial", 10, "bold"))

    def _layout(self):
        root = ttk.Frame(self, padding=20)
        root.pack(fill="both", expand=True)
        ttk.Label(root, text="Łacina • trener słówek i zdań", style="Title.TLabel").pack(anchor="w")
        ttk.Label(root, text="Dwa niezależne tryby: znaczenie słówek albo rzeczownik w zdaniu.",
                  style="Sub.TLabel").pack(anchor="w", pady=(3, 12))

        modes = ttk.LabelFrame(root, text="Tryb nauki", padding=9)
        modes.pack(fill="x", pady=(0, 10))
        ttk.Radiobutton(modes, text="Słówka – tłumaczenia", variable=self.mode,
                        value="words", command=self._mode_changed).pack(side="left", padx=(0, 24))
        ttk.Radiobutton(modes, text="Zdania – przetłumacz i odmień", variable=self.mode,
                        value="sentences", command=self._mode_changed).pack(side="left")

        options = ttk.Frame(root)
        options.pack(fill="x")
        groups = ttk.LabelFrame(options, text="Deklinacje", padding=10)
        groups.pack(side="left", fill="both", expand=True, padx=(0, 6))
        for name, var in self.group_vars.items():
            ttk.Checkbutton(groups, text=f"{name} ({len(WORD_GROUPS[name])} słów)",
                            variable=var).pack(anchor="w", pady=2)

        right = ttk.Frame(options)
        right.pack(side="left", fill="both", expand=True, padx=(6, 0))
        self.direction_frame = ttk.LabelFrame(right, text="Kierunek – tryb słówek", padding=9)
        self.direction_frame.pack(fill="x", pady=(0, 7))
        self.direction_buttons = []
        for text, value in (("Polski → łacina", "pl_la"), ("Łacina → polski", "la_pl"),
                            ("Oba kierunki (losowo)", "mixed")):
            b = ttk.Radiobutton(self.direction_frame, text=text, variable=self.direction, value=value)
            b.pack(anchor="w")
            self.direction_buttons.append(b)
        ttk.Checkbutton(right, text="Pokaż przypadek i liczbę (wskazówka)",
                        variable=self.show_case, command=self._update_case_hint).pack(anchor="w")

        bar = ttk.Frame(root)
        bar.pack(fill="x", pady=(10, 10))
        ttk.Checkbutton(bar, text="Powtarzaj błędne odpowiedzi", variable=self.repeat_errors).pack(side="left")
        ttk.Button(bar, text="Rozpocznij / zresetuj", command=self.start_session).pack(side="right")

        ttk.Separator(root).pack(fill="x", pady=(2, 11))
        ttk.Label(root, textvariable=self.question_label, style="Sub.TLabel").pack(anchor="center")
        ttk.Label(root, textvariable=self.prompt, style="Prompt.TLabel",
                  wraplength=790, justify="center").pack(pady=(7, 8))
        ttk.Label(root, textvariable=self.polish_sentence, style="Polish.TLabel",
                  wraplength=790, justify="center").pack(pady=(0, 5))
        ttk.Label(root, textvariable=self.hint, style="Sub.TLabel",
                  wraplength=790, justify="center").pack(pady=(0, 10))

        self.answer_entry = ttk.Entry(root, font=("Arial", 16), justify="center")
        self.answer_entry.pack(fill="x", padx=30, ipady=7)
        buttons = ttk.Frame(root)
        buttons.pack(pady=(12, 5))
        self.check_button = ttk.Button(buttons, text="Sprawdź (Enter)",
                                       style="Accent.TButton", command=self.check_answer)
        self.check_button.pack(side="left", padx=5)
        self.next_button = ttk.Button(buttons, text="Następne (Enter)", command=self.next_question)
        self.next_button.pack(side="left", padx=5)
        self.show_button = ttk.Button(buttons, text="Pokaż odpowiedź", command=self.reveal_answer)
        self.show_button.pack(side="left", padx=5)

        self.feedback_label = ttk.Label(root, textvariable=self.feedback,
                                         style="Feedback.TLabel", wraplength=790, justify="center")
        self.feedback_label.pack(pady=(9, 2))
        ttk.Label(root, textvariable=self.explanation, style="Sub.TLabel",
                  wraplength=790, justify="center").pack(pady=(0, 4))
        ttk.Separator(root).pack(fill="x", pady=(9, 8))
        ttk.Label(root, textvariable=self.progress).pack(anchor="center")
        ttk.Label(root, textvariable=self.status, style="Sub.TLabel",
                  wraplength=790, justify="center").pack(pady=(4, 0))
        ttk.Label(root, text="Enter: sprawdź / następne    •    Ctrl+N: następne    •    Esc: wyczyść pole",
                  style="Sub.TLabel").pack(side="bottom", pady=(9, 0))
        self._update_buttons()

    def _mode_changed(self):
        is_words = self.mode.get() == "words"
        for button in self.direction_buttons:
            button.configure(state="normal" if is_words else "disabled")
        self.status.set("Po zmianie trybu kliknij «Rozpocznij / zresetuj», aby rozpocząć nową rundę.")

    def _update_case_hint(self):
        if self.current is not None and self.active_mode == "sentences":
            q = self.current
            self.hint.set(f"Słowo do przetłumaczenia: {q.polish_hint}"
                          + (f"  •  {CASES[q.case]}, {NUMBERS[q.number]}" if self.show_case.get() else ""))

    def start_session(self):
        groups = {name for name, var in self.group_vars.items() if var.get()}
        if not groups:
            messagebox.showwarning("Brak grup", "Zaznacz co najmniej jedną deklinację.")
            return
        self.active_mode = self.mode.get()
        if self.active_mode == "words":
            selected = [(latin, polish) for name in WORD_GROUPS if name in groups
                        for latin, polish in WORD_GROUPS[name]]
        else:
            selected = make_questions(groups)
        if not selected:
            messagebox.showwarning("Brak pytań", "Brak ćwiczeń dla wybranych grup w tym trybie.")
            return
        self.deck = list(selected)
        random.shuffle(self.deck)
        self.pending_retry = []
        self.current = None
        self.correct = self.wrong = self.asked = 0
        self.progress.set("Poprawne: 0   |   Błędne: 0   |   Pytania: 0")
        self.status.set(f"Tryb: {'słówka' if self.active_mode == 'words' else 'zdania'}. "
                        f"Pytań w rundzie: {len(selected)}. Kolejność losowa.")
        self.next_question()

    def next_question(self):
        if self.active_mode is None:
            self.status.set("Najpierw kliknij «Rozpocznij / zresetuj».")
            return
        if not self.deck:
            if self.pending_retry and self.repeat_errors.get():
                self.deck, self.pending_retry = self.pending_retry, []
                random.shuffle(self.deck)
                self.status.set("Powtórka pytań, przy których wystąpiły błędy.")
            else:
                self.current = None
                self.question_label.set("Koniec rundy")
                self.prompt.set("Dobra robota!")
                self.polish_sentence.set("")
                self.hint.set("")
                self.feedback.set("Kliknij «Rozpocznij / zresetuj», by zacząć następną rundę.")
                self.explanation.set("")
                self.checked = True
                self._update_buttons()
                return
        self.current = self.deck.pop()
        self.checked = False
        self.answer_entry.delete(0, tk.END)
        self.feedback.set("")
        self.explanation.set("")
        self.feedback_label.configure(foreground="#27364a")
        if self.active_mode == "words":
            latin, polish = self.current
            direction = self.direction.get()
            self.current_direction = random.choice(("pl_la", "la_pl")) if direction == "mixed" else direction
            self.question_label.set("Przetłumacz na łacinę" if self.current_direction == "pl_la"
                                    else "Przetłumacz na polski")
            self.prompt.set(polish.replace(";", " /") if self.current_direction == "pl_la" else latin)
            self.polish_sentence.set("")
            self.hint.set("")
        else:
            q = self.current
            self.question_label.set("Przetłumacz polski rzeczownik i wpisz poprawną formę łacińską")
            self.prompt.set(q.sentence)
            self.polish_sentence.set(q.polish_sentence)
            self._update_case_hint()
        self._update_buttons()
        self.answer_entry.focus_set()

    def expected(self):
        if self.current is None:
            return ""
        if self.active_mode == "sentences":
            return self.current.expected
        latin, polish = self.current
        return latin if self.current_direction == "pl_la" else polish.replace(";", " / ")

    def check_answer(self):
        if self.current is None or self.checked:
            return
        answer = normalized(self.answer_entry.get())
        if not answer:
            self.feedback.set("Wpisz odpowiedź albo wybierz «Pokaż odpowiedź».")
            return
        if self.active_mode == "sentences":
            correct = answer == normalized(self.current.expected)
        else:
            latin, polish = self.current
            accepted = [normalized(latin)] if self.current_direction == "pl_la" else translations(polish)
            correct = answer in accepted
        self._finish(correct, revealed=False)

    def reveal_answer(self):
        if self.current is not None and not self.checked:
            self._finish(False, revealed=True)

    def _finish(self, correct, revealed):
        self.checked = True
        self.asked += 1
        if correct:
            self.correct += 1
            self.feedback.set("✓ Poprawnie!")
            self.feedback_label.configure(foreground="#16804d")
        else:
            self.wrong += 1
            self.feedback.set(("Odpowiedź: " if revealed else "Nie tym razem. Poprawnie: ") + self.expected())
            self.feedback_label.configure(foreground="#b34236")
            if self.repeat_errors.get():
                self.pending_retry.append(self.current)
        if self.active_mode == "sentences":
            q = self.current
            self.explanation.set(f"{q.latin} → {q.expected}  •  {CASES[q.case]}, {NUMBERS[q.number]}"
                                 f"  •  {q.group}")
        self.progress.set(f"Poprawne: {self.correct}   |   Błędne: {self.wrong}   |   Pytania: {self.asked}")
        self._update_buttons()

    def _update_buttons(self):
        active = self.current is not None
        self.check_button.configure(state="normal" if active and not self.checked else "disabled")
        self.show_button.configure(state="normal" if active and not self.checked else "disabled")
        self.next_button.configure(state="normal" if active and self.checked else "disabled")

    def _enter(self, _event):
        if self.current is not None:
            self.next_question() if self.checked else self.check_answer()


if __name__ == "__main__":
    LatinTrainer().mainloop()
