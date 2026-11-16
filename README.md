# Нобелевские лауреаты: финальное задание

## Что нужно

- python 3.8+
- библиотека для графиков: `pip install matplotlib`
- jupyter: `pip install jupyter`
- файл `laureates.json` (сохранённый запрос к API
  `https://api.nobelprize.org/2.1/laureates?limit=1200`) в той же папке,
  что и ноутбук, под этим именем. В репозиторий он не добавляется (`.gitignore`).

## Запуск

1. перейти в папку проекта: `cd omd`
2. запустить Jupyter: `jupyter notebook laureates_countries_task.ipynb`
3. выполнить все ячейки: `Kernel -> Restart & Run All`.
Ноутбук нужно запускать из этой папки, иначе он не найдёт модули `.py`
и `laureates.json`.

## Проверка модулей

каждый модуль содержит assert-ы, при успехе печатается `ok`:
`python json_dict_processing.py` (аналогично для остальных `.py`).
