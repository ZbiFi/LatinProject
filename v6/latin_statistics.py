"""Niezalezna historia zakonczonych lekcji; bez zaleznosci od trybow nauki."""
import hashlib
import json
import os
from datetime import datetime
from pathlib import Path

STATS_FILE = Path(__file__).resolve().parent / 'latin_statistics.json'


def lesson_key(config):
    """Stabilny klucz dla dowolnego trybu i jego opcji (bez opcji pomocniczych)."""
    canonical = json.dumps(config, ensure_ascii=False, sort_keys=True, separators=(',', ':'))
    return hashlib.sha256(canonical.encode('utf-8')).hexdigest()[:24]


def material_fingerprint(words):
    canonical = json.dumps(sorted(words), ensure_ascii=False)
    return hashlib.sha256(canonical.encode('utf-8')).hexdigest()[:16]


def load_history(path=STATS_FILE):
    path = Path(path)
    if not path.exists():
        return {'version': 1, 'lessons': {}}
    with path.open('r', encoding='utf-8') as f:
        data = json.load(f)
    if not isinstance(data, dict) or data.get('version') != 1 or not isinstance(data.get('lessons'), dict):
        raise ValueError('Nieznany lub uszkodzony format pliku statystyk.')
    return data


def save_completed(config, label, result, path=STATS_FILE):
    """Wywolywac WYŁĄCZNIE po zakonczeniu pelnej rundy."""
    path = Path(path)
    data = load_history(path)
    key = lesson_key(config)
    lesson = data['lessons'].setdefault(key, {'config': config, 'label': label, 'sessions': []})
    entry = dict(result)
    entry['completed_at'] = datetime.now().astimezone().isoformat(timespec='seconds')
    entry['accuracy'] = round(100 * entry['correct'] / entry['attempts'], 2) if entry['attempts'] else 0
    entry['first_try_accuracy'] = round(100 * entry['first_try_correct'] / entry['questions'], 2) if entry['questions'] else 0
    lesson['sessions'].append(entry)
    path.parent.mkdir(parents=True, exist_ok=True)
    temp = path.with_name(path.name + '.tmp')
    try:
        with temp.open('w', encoding='utf-8') as f:
            json.dump(data, f, indent=2, ensure_ascii=False)
            f.write('\n')
        os.replace(temp, path)
    finally:
        if temp.exists():
            temp.unlink()
    return entry
