# Анализ каталога фильмов

Статистика, топ фильмов, жанры и актёры. Все функции находятся в
`catalog_analysis.py`, итоговый отчёт выводит `build_report`.

Python 3.12+, uv. Автор: Naumov Pavel.

```bash
uv sync
uv run catalog_analysis.py
uv run ruff check .
uv run python -m unittest discover -s tests
```
