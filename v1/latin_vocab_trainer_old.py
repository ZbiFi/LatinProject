#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Trener słówek łacińskich (Python 3, bez dodatkowych bibliotek)."""

import random
import re
import tkinter as tk
import unicodedata
from tkinter import ttk, messagebox

# Rozszerzanie bazy: dopisz nową grupę, np. "III deklinacja": [("rex", "król"), ...].
# Wprowadzamy formę podstawową (mianownik l. pojedynczej), bez odmiany przez przypadki.
WORD_GROUPS = {
    "I deklinacja": [
        ("puella", "dziewczyna"),
        ("rosa", "róża"),
        ("aqua", "woda"),
        ("terra", "ziemia"),
        ("via", "droga"),
        ("silva", "las"),
        ("femina", "kobieta"),
        ("vita", "życie"),
        ("insula", "wyspa"),
        ("patria", "ojczyzna"),
        ("familia", "rodzina"),
        ("amica", "przyjaciółka"),
        ("filia", "córka"),
        ("villa", "dom wiejski; willa"),
        ("porta", "brama"),
        ("stella", "gwiazda"),
        ("luna", "księżyc"),
        ("cura", "troska; opieka"),
        ("nauta", "żeglarz"),
        ("poeta", "poeta"),
    ],
    "II deklinacja": [
        ("servus", "niewolnik"),
        ("dominus", "pan; właściciel"),
        ("amicus", "przyjaciel"),
        ("puer", "chłopiec"),
        ("ager", "pole"),
        ("filius", "syn"),
        ("equus", "koń"),
        ("magister", "nauczyciel"),
        ("populus", "lud; naród"),
        ("hortus", "ogród"),
        ("deus", "bóg"),
        ("locus", "miejsce"),
        ("animus", "duch; umysł"),
        ("liber", "książka"),
        ("bellum", "wojna"),
        ("templum", "świątynia"),
        ("donum", "dar; prezent"),
        ("verbum", "słowo"),
        ("oppidum", "miasto; miasteczko"),
        ("periculum", "niebezpieczeństwo"),
    ],
}


def normalized(text):
    """Porównanie bez rozróżniania wielkości liter i zbędnych spacji.

    Zachowujemy polskie znaki; 'róża' i 'roza' to różne zapisy.
    """
    return re.sub(r"\s+", " ", unicodedata.normalize("NFC", text).casefold().strip())


def translations(text):
    """Średnik rozdziela dopuszczalne polskie odpowiedzi."""
    return [normalized(part) for part in text.split(";") if part.strip()]


class LatinTrainer(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Trener łaciny — słówka")
        self.geometry("820x630")
        self.minsize(670, 560)
        self.configure(bg="#f4f7fb")

        self.group_vars = {name: tk.BooleanVar(value=True) for name in WORD_GROUPS}
        self.direction = tk.StringVar(value="mixed")
        self.repeat_errors = tk.BooleanVar(value=True)
        self.status = tk.StringVar(value="Wybierz grupy i rozpocznij naukę.")
        self.prompt = tk.StringVar(value="Gotowy do nauki?")
        self.question_label = tk.StringVar(value="")
        self.progress = tk.StringVar(value="Poprawne: 0   |   Błędne: 0   |   Pytania: 0")
        self.feedback = tk.StringVar(value="")
        self.current = None
        self.current_direction = None
        self.checked = False
        self.deck = []
        self.pending_retry = []
        self.correct = 0
        self.wrong = 0
        self.asked = 0

        self._style()
        self._layout()
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
        style.configure("Prompt.TLabel", font=("Arial", 26, "bold"), foreground="#123e72")
        style.configure("Feedback.TLabel", font=("Arial", 12, "bold"))
        style.configure("TCheckbutton", background="#f4f7fb", font=("Arial", 10))
        style.configure("TRadiobutton", background="#f4f7fb", font=("Arial", 10))
        style.configure("TButton", font=("Arial", 11), padding=(12, 8))
        style.configure("Accent.TButton", font=("Arial", 11, "bold"), padding=(14, 9))
        style.configure("TLabelframe", background="#f4f7fb")
        style.configure("TLabelframe.Label", background="#f4f7fb", font=("Arial", 10, "bold"))

    def _layout(self):
        root = ttk.Frame(self, padding=24)
        root.pack(fill="both", expand=True)
        ttk.Label(root, text="Łacina • trening słówek", style="Title.TLabel").pack(anchor="w")
        ttk.Label(root, text="Tłumacz formy podstawowe: polski ↔ łacina. Bez odmiany przez przypadki.", style="Sub.TLabel").pack(anchor="w", pady=(4, 14))

        options = ttk.Frame(root)
        options.pack(fill="x")
        groups_frame = ttk.LabelFrame(options, text="Grupy słówek", padding=12)
        groups_frame.pack(side="left", fill="both", expand=True, padx=(0, 8))
        for name, var in self.group_vars.items():
            ttk.Checkbutton(groups_frame, text=f"{name} ({len(WORD_GROUPS[name])})", variable=var).pack(anchor="w", pady=2)

        direction_frame = ttk.LabelFrame(options, text="Kierunek tłumaczenia", padding=12)
        direction_frame.pack(side="left", fill="both", expand=True, padx=(8, 0))
        for text, value in (("Polski → łacina", "pl_la"), ("Łacina → polski", "la_pl"), ("Oba kierunki (losowo)", "mixed")):
            ttk.Radiobutton(direction_frame, text=text, variable=self.direction, value=value).pack(anchor="w", pady=2)

        bar = ttk.Frame(root)
        bar.pack(fill="x", pady=(12, 14))
        ttk.Checkbutton(bar, text="Powtarzaj błędne odpowiedzi", variable=self.repeat_errors).pack(side="left")
        ttk.Button(bar, text="Rozpocznij / zresetuj", command=self.start_session).pack(side="right")

        separator = ttk.Separator(root)
        separator.pack(fill="x", pady=(0, 16))
        ttk.Label(root, textvariable=self.question_label, style="Sub.TLabel").pack(anchor="center")
        ttk.Label(root, textvariable=self.prompt, style="Prompt.TLabel", wraplength=730, justify="center").pack(pady=(9, 15))
        self.answer_entry = ttk.Entry(root, font=("Arial", 16), justify="center")
        self.answer_entry.pack(fill="x", padx=40, ipady=8)

        buttons = ttk.Frame(root)
        buttons.pack(pady=(14, 6))
        self.check_button = ttk.Button(buttons, text="Sprawdź (Enter)", style="Accent.TButton", command=self.check_answer)
        self.check_button.pack(side="left", padx=6)
        self.next_button = ttk.Button(buttons, text="Następne (Enter)", command=self.next_question)
        self.next_button.pack(side="left", padx=6)
        self.show_button = ttk.Button(buttons, text="Pokaż odpowiedź", command=self.reveal_answer)
        self.show_button.pack(side="left", padx=6)

        self.feedback_label = ttk.Label(root, textvariable=self.feedback, style="Feedback.TLabel", wraplength=740, justify="center")
        self.feedback_label.pack(pady=(10, 9))
        ttk.Separator(root).pack(fill="x", pady=(12, 9))
        ttk.Label(root, textvariable=self.progress).pack(anchor="center")
        ttk.Label(root, textvariable=self.status, style="Sub.TLabel", wraplength=740, justify="center").pack(pady=(5, 0))
        ttk.Label(root, text="Enter: sprawdź / następne    •    Ctrl+N: następne    •    Esc: wyczyść pole", style="Sub.TLabel").pack(side="bottom", pady=(12, 0))
        self._update_buttons()

    def start_session(self):
        selected = [(latin, polish) for name, var in self.group_vars.items() if var.get() for latin, polish in WORD_GROUPS[name]]
        if not selected:
            messagebox.showwarning("Brak słówek", "Zaznacz co najmniej jedną grupę deklinacji.")
            return
        self.deck = selected.copy()
        random.shuffle(self.deck)
        self.pending_retry = []
        self.correct = self.wrong = self.asked = 0
        self.progress.set("Poprawne: 0   |   Błędne: 0   |   Pytania: 0")
        self.status.set(f"Wybrane słówka: {len(selected)}. Słówka pojawiają się bez powtórek w pierwszym przebiegu.")
        self.next_question()

    def next_question(self):
        if not self.deck:
            if self.pending_retry and self.repeat_errors.get():
                self.deck, self.pending_retry = self.pending_retry, []
                random.shuffle(self.deck)
                self.status.set("Powtórka słówek, przy których wystąpiły błędy.")
            else:
                self.current = None
                self.question_label.set("Koniec rundy")
                self.prompt.set("Świetna robota!")
                self.feedback.set("Kliknij «Rozpocznij / zresetuj», aby zacząć kolejną rundę.")
                self.checked = True
                self._update_buttons()
                return
        self.current = self.deck.pop()
        selected_direction = self.direction.get()
        self.current_direction = random.choice(("pl_la", "la_pl")) if selected_direction == "mixed" else selected_direction
        latin, polish = self.current
        self.question_label.set("Przetłumacz na łacinę" if self.current_direction == "pl_la" else "Przetłumacz na polski")
        self.prompt.set(polish.replace(";", " / ") if self.current_direction == "pl_la" else latin)
        self.answer_entry.delete(0, tk.END)
        self.feedback.set("")
        self.checked = False
        self._update_buttons()
        self.answer_entry.focus_set()

    def expected(self):
        if not self.current:
            return ""
        latin, polish = self.current
        return latin if self.current_direction == "pl_la" else polish.replace(";", " / ")

    def check_answer(self):
        if self.current is None or self.checked:
            return
        user_answer = normalized(self.answer_entry.get())
        if not user_answer:
            self.feedback.set("Wpisz odpowiedź albo wybierz «Pokaż odpowiedź».")
            return
        latin, polish = self.current
        accepted = [normalized(latin)] if self.current_direction == "pl_la" else translations(polish)
        is_correct = user_answer in accepted
        self._finish(is_correct, revealed=False)

    def reveal_answer(self):
        if self.current is None or self.checked:
            return
        self._finish(False, revealed=True)

    def _finish(self, is_correct, revealed):
        self.checked = True
        self.asked += 1
        if is_correct:
            self.correct += 1
            self.feedback.set("✓ Poprawnie!")
            self.feedback_label.configure(foreground="#16804d")
        else:
            self.wrong += 1
            self.feedback.set(("Odpowiedź: " if revealed else "Nie tym razem. Poprawnie: ") + self.expected())
            self.feedback_label.configure(foreground="#b34236")
            if self.repeat_errors.get():
                self.pending_retry.append(self.current)
        self.progress.set(f"Poprawne: {self.correct}   |   Błędne: {self.wrong}   |   Pytania: {self.asked}")
        self._update_buttons()

    def _update_buttons(self):
        active = self.current is not None
        self.check_button.configure(state=("normal" if active and not self.checked else "disabled"))
        self.show_button.configure(state=("normal" if active and not self.checked else "disabled"))
        self.next_button.configure(state=("normal" if active else "disabled"))

    def _enter(self, _event):
        if self.current is None:
            return
        if self.checked:
            self.next_question()
        else:
            self.check_answer()


if __name__ == "__main__":
    LatinTrainer().mainloop()
