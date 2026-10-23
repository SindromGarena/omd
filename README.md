# omd
Домашнее задание 2

## Установка 

Для установки нужен Python >3.8, сторонних библиотек не нужно (csv, sys стандартные)

На bash
git clone git@github.com:SindromGarena/omd.git 
cd omd

## Запуск 

На bash 
python3 report.py <номер варианта>

## Варианты 
1 - Иерархия 
2 - сводка по департаментам
3 - то же, что и 2 вариант, но в csv

Пример: python3 report.py 2

## Проверка стиля

На bash

pip install flake8 
flake8 report.py
