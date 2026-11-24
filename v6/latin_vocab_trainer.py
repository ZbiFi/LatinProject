#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Łacina – słówka i odmiana w zdaniach. Uruchom: python latin_vocab_trainer.py"""
import random
import re
import tkinter as tk
import unicodedata
from tkinter import ttk, messagebox

from latin_data import WORD_GROUPS
from latin_practice import CASES, NUMBERS, NOUNS, decline, make_questions
from latin_statistics import load_history, save_completed, material_fingerprint

# Nazwy przypadków wyświetlane w trybie odmiany.
# Polski opis pomaga zapamiętać łacińskie nazewnictwo.
FORM_CASE_LABELS = {
    "nom": "Nominativus [mianownik]",
    "gen": "Genetivus [dopełniacz]",
    "dat": "Dativus [celownik]",
    "acc": "Accusativus [biernik]",
    "abl": "Ablativus [narzędnik]",
    "voc": "Vocativus [wołacz]",
}


def normalized(text):
    """Porównanie bez rozróżniania wielkości liter i nadmiarowych spacji."""
    return re.sub(r"\s+", " ", unicodedata.normalize("NFC", text).casefold().strip())


def translations(text):
    """Średniki w bazie oznaczają alternatywne polskie tłumaczenia."""
    return [normalized(part) for part in text.split(";") if part.strip()]


class LatinTrainer(tk.Tk):
    """GUI obsługuje trzy tryby, wspólne statystyki i powtórki błędów."""

    def __init__(self):
        super().__init__()
        self.title("Łacina – słówka, zdania i odmiana")
        self.geometry("930x890")
        self.minsize(750, 740)
        self.configure(bg="#f4f7fb")

        self.group_vars = {name: tk.BooleanVar(value=("zestaw 2" not in name)) for name in WORD_GROUPS}
        self.mode = tk.StringVar(value="words")
        self.direction = tk.StringVar(value="mixed")
        self.repeat_errors = tk.BooleanVar(value=True)
        self.show_case = tk.BooleanVar(value=False)
        self.forms_scope = tk.StringVar(value="basic")
        self.random_forms = {}  # (losowany przypadek, liczba) na rzeczownik i rundę
        self.forms_specs = []
        self.forms_entries = {}
        self.forms_available = []
        self.status = tk.StringVar(value="Wybierz tryb oraz grupy i rozpocznij naukę.")
        self.prompt = tk.StringVar(value="Gotowy do nauki?")
        self.question_label = tk.StringVar(value="")
        self.polish_sentence = tk.StringVar(value="")
        self.hint = tk.StringVar(value="")
        self.progress = tk.StringVar(value="Poprawne: 0   |   Błędne: 0   |   Próby: 0")
        self.feedback = tk.StringVar(value="")
        self.explanation = tk.StringVar(value="")

        self.active_mode = None
        self.current = None
        self.current_direction = None
        self.checked = False
        self.deck = []
        self.pending_retry = []  # (pytanie, najwczesniejszy numer kolejnego pytania)
        self.question_index = 0
        self.correct = self.wrong = self.asked = 0
        self.session_config = None
        self.session_label = ''
        self.session_material = ''
        self.session_options = {}
        self.session_questions = 0
        self.first_try_correct = 0
        self.current_repeated = False
        self.direction_counts = {'pl_la': 0, 'la_pl': 0}
        self.field_errors = {}
        self.reveals = 0
        self.session_saved = False

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
        ttk.Label(root, text="Łacina • słówka, zdania i odmiana", style="Title.TLabel").pack(anchor="w")
        ttk.Label(root, text="Trzy tryby: tłumaczenia, zdania oraz odmiana rzeczownika.",
                  style="Sub.TLabel").pack(anchor="w", pady=(3, 12))

        modes = ttk.LabelFrame(root, text="Tryb nauki", padding=9)
        modes.pack(fill="x", pady=(0, 10))
        ttk.Radiobutton(modes, text="Słówka – tłumaczenia", variable=self.mode,
                        value="words", command=self._mode_changed).pack(side="left", padx=(0, 24))
        ttk.Radiobutton(modes, text="Zdania – przetłumacz i odmień", variable=self.mode,
                        value="sentences", command=self._mode_changed).pack(side="left", padx=(0, 24))
        ttk.Radiobutton(modes, text="Odmiana – formy rzeczownika", variable=self.mode,
                        value="forms", command=self._mode_changed).pack(side="left")

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

        self.forms_options = ttk.LabelFrame(root, text="Zakres odmiany (tryb: Odmiana)", padding=7)
        self.forms_options.pack(fill="x", pady=(9, 0))
        self.forms_scope_options = (
            ("Nom. sg. + Gen. sg.", "basic"),
            ("Wszystkie przypadki liczby pojedynczej", "singular"),
            ("Nom. sg. + Gen. sg. + liczba mnoga", "plural"),
            ("Nom. sg. + Gen. sg. + losowy przypadek (lp. lub lm.)", "random"),
            ("Pełna odmiana (lp. + lm.)", "full"),
        )
        self.forms_scope_labels = {value: label for label, value in self.forms_scope_options}
        self.forms_scope_by_label = {label: value for label, value in self.forms_scope_options}
        self.forms_scope_select = ttk.Combobox(
            self.forms_options, state="readonly", width=63,
            values=[label for label, _ in self.forms_scope_options])
        self.forms_scope_select.current(0)
        self.forms_scope_select.pack(anchor="w", fill="x")
        self.forms_scope_select.bind("<<ComboboxSelected>>", self._change_forms_scope)

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

        self.forms_frame = ttk.Frame(root)
        self.forms_column_header = ttk.Frame(self.forms_frame)
        self.forms_column_header.pack(fill="x")
        self.forms_fields = ttk.Frame(self.forms_frame)
        self.forms_fields.pack(fill="x")
        buttons = ttk.Frame(root)
        self.buttons_frame = buttons
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
        ttk.Button(root, text="Pokaż statystyki", command=self.show_statistics).pack(
            side="bottom", anchor="e", pady=(5, 2))
        self._update_buttons()

    def _change_forms_scope(self, _event=None):
        self.forms_scope.set(self.forms_scope_by_label[self.forms_scope_select.get()])
        if self.active_mode == "forms":
            # Po zmianie zakresu nie kontynuuj rundy z poprzednią konfiguracją pól.
            self.active_mode = None
            self.current = None
            self.checked = True
            self._update_buttons()
        self.status.set("Zmieniono zakres odmiany. Kliknij «Rozpocznij / zresetuj».")

    def _specs_for_noun(self, noun):
        """Zwraca przypadki z wybranego zakresu; przy losowym zachowuje wybór w powtórkach."""
        specs = [("nom", "sg"), ("gen", "sg")]
        scope = self.forms_scope.get()
        if scope in ("singular", "full"):
            specs.extend((case, "sg") for case in ("dat", "acc", "abl", "voc"))
        if scope in ("plural", "full"):
            specs.extend((case, "pl") for case in CASES)
        if scope == "random":
            specs.append(self.random_forms[noun.latin])
        return specs

    def _build_forms_fields(self):
        """Jedno pole na każdą wybraną formę; dwie kolumny dla liczby sg./pl."""
        for widget in self.forms_fields.winfo_children():
            widget.destroy()
        self.forms_entries = {}
        for column, number in enumerate(("sg", "pl")):
            ttk.Label(self.forms_fields, text=NUMBERS[number], font=("Arial", 10, "bold")).grid(
                row=0, column=column * 2, columnspan=2, sticky="w", pady=(0, 3), padx=(0, 15))
            specs = [case for case in CASES if (case, number) in self.forms_specs]
            for row, case in enumerate(specs, 1):
                ttk.Label(self.forms_fields, text=f"{FORM_CASE_LABELS[case]}:").grid(
                    row=row, column=column * 2, sticky="w", padx=(0, 5), pady=2)
                entry = ttk.Entry(self.forms_fields, width=19, font=("Arial", 11))
                entry.grid(row=row, column=column * 2 + 1, sticky="ew", padx=(0, 18), pady=2)
                self.forms_entries[(case, number)] = entry
        self.forms_fields.columnconfigure(1, weight=1)
        self.forms_fields.columnconfigure(3, weight=1)

    def _mode_changed(self):
        is_words = self.mode.get() == "words"
        for button in self.direction_buttons:
            button.configure(state="normal" if is_words else "disabled")
        is_forms = self.mode.get() == "forms"
        self.forms_scope_select.configure(state="readonly" if is_forms else "disabled")
        if is_forms:
            self.answer_entry.pack_forget()
            self.forms_frame.pack(fill="x", padx=30, pady=(3, 0), before=self.buttons_frame)
        else:
            self.forms_frame.pack_forget()
            self.answer_entry.pack(fill="x", padx=30, ipady=7, before=self.buttons_frame)
        self.status.set("Po zmianie trybu kliknij «Rozpocznij / zresetuj», aby rozpocząć nową rundę.")

    def _update_case_hint(self):
        if self.current is not None and self.active_mode == "sentences":
            if self.show_case.get() and self.session_config:
                self.session_options['hints_enabled'] = True
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
        elif self.active_mode == "forms":
            selected = [noun for noun in NOUNS.values() if noun.group in groups]
            self.random_forms = {}
            if self.forms_scope.get() == "random":
                for noun in selected:
                    candidates = [(case, number) for number in ("sg", "pl")
                                  for case in CASES if (case, number) not in
                                  {("nom", "sg"), ("gen", "sg")}]
                    available = []
                    for spec in candidates:
                        try:
                            decline(noun, *spec)
                        except ValueError:
                            continue
                        available.append(spec)
                    if not available:
                        messagebox.showerror("Odmiana niedostępna",
                                             f"Brak dodatkowego przypadku dla {noun.latin}.")
                        return
                    self.random_forms[noun.latin] = random.choice(available)
            self.forms_specs = self._specs_for_noun(selected[0]) if selected else []
            try:
                for noun in selected:
                    decline(noun, "nom", "sg")
                    decline(noun, "gen", "sg")
            except ValueError as exc:
                messagebox.showerror("Odmiana niedostępna", str(exc) + "\nZmień zakres lub grupę.")
                return
            self._build_forms_fields()
        else:
            selected = make_questions(groups)
        if not selected:
            messagebox.showwarning("Brak pytań", "Brak ćwiczeń dla wybranych grup w tym trybie.")
            return
        # Migawka konfiguracji zapobiega mieszaniu historii po zmianie ustawien.
        options = {}
        if self.active_mode == 'words':
            options['direction'] = self.direction.get()
        elif self.active_mode == 'forms':
            options['scope'] = self.forms_scope.get()
        self.session_config = {'mode': self.active_mode, 'groups': sorted(groups), 'options': options}
        labels = {'words': 'Tłumaczenia', 'forms': 'Odmiana', 'sentences': 'Zdania'}
        option_label = (self.direction.get() if self.active_mode == 'words' else
                        self.forms_scope.get() if self.active_mode == 'forms' else '')
        self.session_label = labels.get(self.active_mode, self.active_mode) + ' | ' + ', '.join(sorted(groups))
        if option_label:
            self.session_label += ' | ' + option_label
        self.session_options = {'repetitions_enabled': self.repeat_errors.get(),
                                'hints_enabled': self.show_case.get() if self.active_mode == 'sentences' else False}
        self.session_material = material_fingerprint(
            [latin for group in groups for latin, _ in WORD_GROUPS[group]])
        self.session_questions = len(selected)
        self.first_try_correct = 0
        self.direction_counts = {'pl_la': 0, 'la_pl': 0}
        self.field_errors = {}
        self.reveals = 0
        self.session_saved = False
        self.deck = list(selected)
        random.shuffle(self.deck)
        self.pending_retry = []
        self.question_index = 0
        self.current = None
        self.correct = self.wrong = self.asked = 0
        self.progress.set("Poprawne: 0   |   Błędne: 0   |   Próby: 0")
        mode_name = {"words": "słówka", "sentences": "zdania", "forms": "odmiana"}[self.active_mode]
        self.status.set(f"Tryb: {mode_name}. "
                        f"Pytań w rundzie: {len(selected)}. Losowe szablony i kolejność.")
        self.next_question()

    def _queue_retry(self):
        """Zapamietaj blad; powtorka po co najmniej 3 innych pytaniach, jesli sa."""
        if self.session_options.get('repetitions_enabled', False):
            # Nastepne pytanie ma indeks question_index + 1.
            self.pending_retry.append((self.current, self.question_index + 4))

    def _draw_question(self):
        """Losowo przeplataj powtorki z nowymi pytaniami."""
        if not self.session_options.get('repetitions_enabled', False):
            self.pending_retry.clear()
        eligible = [i for i, (_, due) in enumerate(self.pending_retry)
                    if due <= self.question_index + 1]
        if eligible and (not self.deck or random.random() < 0.30):
            index = random.choice(eligible)
            question, _ = self.pending_retry.pop(index)
            return question, True
        if self.deck:
            return self.deck.pop(), False
        if self.pending_retry:
            # Koniec nowej puli: wyjatkowo przy malej liczbie pytan
            # nie da sie zagwarantowac 3 roznych pytan pomiedzy powtorkami.
            index = random.randrange(len(self.pending_retry))
            question, _ = self.pending_retry.pop(index)
            return question, True
        return None, False

    def next_question(self):
        if self.active_mode is None:
            self.status.set("Najpierw kliknij «Rozpocznij / zresetuj».")
            return
        # Nie pozwalaj ominac pytania przed udzieleniem odpowiedzi.
        if self.current is not None and not self.checked:
            return
        self.current, repeated = self._draw_question()
        self.current_repeated = repeated
        if self.current is None:
            self._save_finished_session()
            self.question_label.set("Koniec rundy")
            self.prompt.set("Dobra robota!")
            self.polish_sentence.set("")
            self.hint.set("")
            self.feedback.set("Kliknij «Rozpocznij / zresetuj», by zacząć następną rundę.")
            self.explanation.set("")
            self.checked = True
            self._update_buttons()
            return
        self.question_index += 1
        if repeated:
            self.status.set("Powtórka wcześniejszego błędu — spróbuj przypomnieć sobie odpowiedź.")
        else:
            self.status.set("Nowe pytanie. Po odpowiedzi naciśnij Enter, aby przejść dalej.")
        self.checked = False
        self.answer_entry.delete(0, tk.END)
        for field in self.forms_entries.values():
            field.configure(state="normal")
            field.delete(0, tk.END)
            field.configure(foreground="#27364a")
        self.feedback.set("")
        self.explanation.set("")
        self.feedback_label.configure(foreground="#27364a")
        if self.active_mode == "words":
            latin, polish = self.current
            direction = self.session_config['options']['direction']
            self.current_direction = random.choice(("pl_la", "la_pl")) if direction == "mixed" else direction
            self.question_label.set("Przetłumacz na łacinę" if self.current_direction == "pl_la"
                                    else "Przetłumacz na polski")
            self.prompt.set(polish.replace(";", " /") if self.current_direction == "pl_la" else latin)
            self.polish_sentence.set("")
            self.hint.set("")
        elif self.active_mode == "forms":
            noun = self.current
            # W wariancie losowym zestaw pól może być inny dla każdego rzeczownika.
            new_specs = self._specs_for_noun(noun)
            if new_specs != self.forms_specs:
                self.forms_specs = new_specs
                self._build_forms_fields()
            self.question_label.set("Podaj łacińskie formy rzeczownika")
            self.prompt.set(noun.polish.replace(";", " /"))
            self.polish_sentence.set(f"{noun.group}   •   rodzaj: {noun.gender}")
            self.forms_available = []
            for spec, entry in self.forms_entries.items():
                try:
                    decline(noun, *spec)
                except ValueError:
                    entry.configure(state="disabled")
                else:
                    self.forms_available.append(spec)
            unavailable = len(self.forms_available) != len(self.forms_specs)
            self.hint.set("Wpisz formy w polach. Nom. i Gen. lp. są obowiązkowe."
                          + (" Trzecia forma jest losowana osobno dla każdego rzeczownika."
                             if self.forms_scope.get() == "random" else "")
                          + (" Niedostępne formy pominięto (np. deus w lm.)." if unavailable else ""))
        else:
            q = self.current
            self.question_label.set("Przetłumacz polski rzeczownik i wpisz poprawną formę łacińską")
            self.prompt.set(q.sentence)
            self.polish_sentence.set(q.polish_sentence)
            self._update_case_hint()
        self._update_buttons()
        if self.active_mode == "forms":
            self.forms_entries[self.forms_specs[0]].focus_set()
        else:
            self.answer_entry.focus_set()

    def expected(self):
        if self.current is None:
            return ""
        if self.active_mode == "sentences":
            return self.current.expected
        if self.active_mode == "forms":
            return "; ".join(f"{FORM_CASE_LABELS[c]} {NUMBERS[n]}: {decline(self.current, c, n)}"
                             for c, n in self.forms_available)
        latin, polish = self.current
        return latin if self.current_direction == "pl_la" else polish.replace(";", " / ")

    def check_answer(self):
        if self.current is None or self.checked:
            return
        if self.active_mode == "forms":
            answers = {spec: normalized(self.forms_entries[spec].get()) for spec in self.forms_available}
            if not any(answers.values()):
                self.feedback.set("Wpisz formy albo wybierz «Pokaż odpowiedź».")
                return
            mistakes = []
            for spec, answer in answers.items():
                expected = normalized(decline(self.current, *spec))
                ok = answer == expected
                self.forms_entries[spec].configure(foreground="#16804d" if ok else "#b34236")
                if not ok:
                    mistakes.append(f"{FORM_CASE_LABELS[spec[0]]} {NUMBERS[spec[1]]}: {expected}")
            for spec, answer in answers.items():
                if answer != normalized(decline(self.current, *spec)):
                    key = f'{spec[0]}_{spec[1]}'
                    self.field_errors[key] = self.field_errors.get(key, 0) + 1
            self._finish(correct=not mistakes, revealed=False, detail="; ".join(mistakes))
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
        self._finish(correct=correct, revealed=False)

    def reveal_answer(self):
        if self.current is not None and not self.checked:
            self._finish(correct=False, revealed=True)

    def _finish(self, correct, revealed, detail=None):
        """Pokaz wynik i odblokuj Nastepne po kazdej odpowiedzi."""
        self.checked = True
        self.asked += 1
        if not self.current_repeated and correct:
            self.first_try_correct += 1
        if revealed:
            self.reveals += 1
            if self.active_mode == 'forms':
                for spec in self.forms_available:
                    key = f'{spec[0]}_{spec[1]}'
                    self.field_errors[key] = self.field_errors.get(key, 0) + 1
        if self.active_mode == 'words':
            self.direction_counts[self.current_direction] += 1
        if correct:
            self.correct += 1
            self.feedback.set("✓ Poprawnie!")
            self.feedback_label.configure(foreground="#16804d")
        else:
            self.wrong += 1
            self.feedback.set(("Odpowiedź: " if revealed else "✗ Błąd. Poprawna odpowiedź: ")
                              + (detail if detail is not None else self.expected()))
            self.feedback_label.configure(foreground="#b34236")
            self._queue_retry()
            if self.session_options.get('repetitions_enabled', False):
                self.status.set("Zadanie wróci później w losowym momencie. Naciśnij Enter, by przejść dalej.")
            else:
                self.status.set("Naciśnij Enter, by przejść do następnego zadania.")
        if self.active_mode == "sentences":
            q = self.current
            self.explanation.set(f"{q.latin} → {q.expected}  •  {CASES[q.case]}, {NUMBERS[q.number]}"
                                 f"  •  {q.group}")
        elif self.active_mode == "forms":
            self.explanation.set(f"Hasło słownikowe: {self.current.latin}, {self.current.genitive} "
                                 f"• {self.current.gender} • {self.current.group}")
        else:
            self.explanation.set("")
        self.progress.set(f"Poprawne: {self.correct}   |   Błędne: {self.wrong}   |   Próby: {self.asked}")
        self._update_buttons()

    def _save_finished_session(self):
        if self.session_saved or not self.session_config:
            return
        result = {
            'questions': self.session_questions,
            'correct': self.correct,
            'wrong': self.wrong,
            'attempts': self.asked,
            'first_try_correct': self.first_try_correct,
            'reveals': self.reveals,
            'material_fingerprint': self.session_material,
            'material_word_count': len(set(
                latin for group in self.session_config['groups']
                for latin, _ in WORD_GROUPS[group])),
            'options_used': dict(self.session_options),
            'direction_attempts': dict(self.direction_counts) if self.active_mode == 'words' else {},
            'field_errors': dict(self.field_errors) if self.active_mode == 'forms' else {}
        }
        try:
            save_completed(self.session_config, self.session_label, result)
        except (OSError, ValueError) as exc:
            messagebox.showerror('Błąd zapisu statystyk', str(exc))
        else:
            self.session_saved = True

    def show_statistics(self):
        """Lista konfiguracji i wykres postepu, bez dodatkowych bibliotek."""
        try:
            lessons = load_history()['lessons']
        except (OSError, ValueError) as exc:
            messagebox.showerror('Błąd odczytu statystyk', str(exc))
            return
        window = tk.Toplevel(self)
        window.title('Historia nauki łaciny')
        window.geometry('900x680')
        window.minsize(650, 500)
        frame = ttk.Frame(window, padding=14)
        frame.pack(fill='both', expand=True)
        ttk.Label(frame, text='Statystyki ukończonych lekcji', style='Title.TLabel').pack(anchor='w', pady=(0, 10))
        if not lessons:
            ttk.Label(frame, text='Brak ukończonych lekcji. Zakończ rundę, aby zapisać pierwszy wynik.').pack(anchor='w')
            return
        entries = sorted(lessons.items(), key=lambda item: item[1].get('label', ''))
        labels = [f"{item.get('label', key)} ({len(item.get('sessions', []))} lekcji)"
                  for key, item in entries]
        ttk.Label(frame, text='Wybierz konfigurację:').pack(anchor='w')
        selector = ttk.Combobox(frame, state='readonly', values=labels)
        selector.pack(fill='x', pady=(2, 10))
        info = ttk.Label(frame, text='', font=('Arial', 11))
        info.pack(anchor='w', pady=(0, 8))
        chart = tk.Canvas(frame, height=215, background='white', highlightthickness=1,
                          highlightbackground='#d4dae2')
        chart.pack(fill='x', pady=(0, 12))
        ttk.Label(frame, text='Historia sesji (najnowsze na górze):').pack(anchor='w')
        columns = ('date', 'questions', 'correct', 'wrong', 'attempts', 'accuracy', 'first_try', 'words')
        table_frame = ttk.Frame(frame)
        table_frame.pack(fill='both', expand=True)
        table = ttk.Treeview(table_frame, columns=columns, show='headings', height=11)
        headings = ('Data', 'Pytań', 'Popr.', 'Błędów', 'Prób', 'Skut. %', '1. próba %', 'Słów')
        widths = (175, 65, 65, 65, 65, 85, 95, 65)
        for col, heading, width in zip(columns, headings, widths):
            table.heading(col, text=heading)
            table.column(col, width=width, minwidth=50, anchor='center')
        table.pack(side='left', fill='both', expand=True)
        scrollbar = ttk.Scrollbar(table_frame, command=table.yview)
        scrollbar.pack(side='right', fill='y')
        table.configure(yscrollcommand=scrollbar.set)
        details = ttk.Label(frame, text='', wraplength=850)
        details.pack(anchor='w', pady=(10, 0))

        def selected_session(_event=None):
            row = table.selection()
            if not row:
                return
            session = table.item(row[0], 'values')
            entry = displayed_sessions[int(table.item(row[0], 'tags')[0])]
            extras = []
            if entry.get('field_errors'):
                extras.append('Błędy form: ' + ', '.join(
                    f'{k}: {v}' for k, v in sorted(entry['field_errors'].items())))
            if entry.get('direction_attempts'):
                extras.append('Kierunki (próby): ' + ', '.join(
                    f'{k}: {v}' for k, v in entry['direction_attempts'].items()))
            extras.append(f"Pokazane odpowiedzi: {entry.get('reveals', 0)}")
            extras.append('Powtórki: ' + ('tak' if entry.get('options_used', {}).get('repetitions_enabled') else 'nie'))
            details.config(text='  |  '.join(extras))

        displayed_sessions = []

        def redraw(_event=None):
            nonlocal displayed_sessions
            item = entries[selector.current()][1]
            sessions = item.get('sessions', [])
            displayed_sessions = list(reversed(sessions))
            for row in table.get_children():
                table.delete(row)
            for i, session in enumerate(displayed_sessions):
                table.insert('', 'end', tags=(str(i),), values=(
                    session['completed_at'][:19].replace('T', ' '), session['questions'],
                    session['correct'], session['wrong'], session['attempts'],
                    f"{session['accuracy']:.1f}", f"{session['first_try_accuracy']:.1f}",
                    session.get('material_word_count', '-')))
            average = sum(s['accuracy'] for s in sessions) / len(sessions)
            recent = sessions[-1]
            info.config(text=f"Ukończone lekcje: {len(sessions)}   |   Średnia skuteczność: {average:.1f}%"
                             f"   |   Ostatni wynik: {recent['accuracy']:.1f}%"
                             f"   |   Pierwsze próby: {recent['first_try_accuracy']:.1f}%")
            details.config(text='Kliknij wiersz, aby zobaczyć szczegóły lekcji.')
            draw_chart(sessions)

        def draw_chart(sessions):
            chart.delete('all')
            width = max(chart.winfo_width(), 500)
            height = 215
            left, right, top, bottom = 46, width - 18, 18, height - 28
            for percent in (0, 25, 50, 75, 100):
                y = bottom - (bottom - top) * percent / 100
                chart.create_line(left, y, right, y, fill='#e2e7ed')
                chart.create_text(left - 9, y, text=str(percent), anchor='e', fill='#697789')
            if not sessions:
                return
            for key, color in (('accuracy', '#146cba'), ('first_try_accuracy', '#259366')):
                points = []
                for i, session in enumerate(sessions):
                    x = left + (right - left) * (i / max(1, len(sessions) - 1))
                    y = bottom - (bottom - top) * session[key] / 100
                    points.extend((x, y))
                if len(points) >= 4:
                    chart.create_line(*points, fill=color, width=2)
                for x, y in zip(points[::2], points[1::2]):
                    chart.create_oval(x-3, y-3, x+3, y+3, fill=color, outline=color)
            chart.create_text(left, height - 8, text='Niebieski: skuteczność prób', anchor='w', fill='#146cba')
            chart.create_text(right, height - 8, text='Zielony: pierwsza próba', anchor='e', fill='#259366')

        table.bind('<<TreeviewSelect>>', selected_session)
        selector.bind('<<ComboboxSelected>>', redraw)
        chart.bind('<Configure>', lambda _event: draw_chart(entries[selector.current()][1]['sessions'])
                   if selector.current() >= 0 else None)
        selector.current(0)
        redraw()

    def _update_buttons(self):
        active = self.current is not None
        self.check_button.configure(state="normal" if active and not self.checked else "disabled")
        self.show_button.configure(state="normal" if active and not self.checked else "disabled")
        self.next_button.configure(state="normal" if active and self.checked else "disabled")
        for spec, entry in self.forms_entries.items():
            entry.configure(state="normal" if active and not self.checked and spec in self.forms_available
                            else "disabled")

    def _enter(self, _event):
        if self.current is not None:
            self.next_question() if self.checked else self.check_answer()


if __name__ == "__main__":
    LatinTrainer().mainloop()
