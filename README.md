Получение данных о работодателях и вакансиях с hh.ru

Этот проект предназначен для получения данных о работодателях и их вакансиях с сайта hh.ru с использованием публичного API hh.ru и библиотеки `requests`. Проект включает в себя проектирование базы данных PostgreSQL для хранения полученных данных и реализацию кода для заполнения таблиц данными о работодателях и их вакансиях.
## Содержание

- [Описание](#описание)
- [Установка](#установка)
- [Использование](#использование)
- [Тестирование](#тестирование)
- [Лицензия](#лицензия)
- [Контакты](#контакты)


## Описание

Проект включает в себя следующие ключевые компоненты:
1. Получение данных о работодателях и вакансиях с помощью API hh.ru.
2. Проектирование таблиц в базе данных PostgreSQL для хранения информации о работодателях и вакансиях.
3. Реализация класса `DBManager` для работы с данными в базе данных.
4. Заполнение таблиц данными о работодателях и вакансиях.
## Установка


1. Клонируйте репозиторий:

   ```bash
   https://github.com/ArtemZhitkov/DB_coursework.git
2. Перейдите в каталог проекта:
    ```bash
   cd DB_coursework
3. Установите зависимости:
    ```bash
   poetry install
4. Настройте базу данных PostgreSQL, если это необходимо.

## Использование

Запустите файл main.py

## Тестирование
Для запуска тестов используйте:
   ```
   python -m unittest
   ```
Тесты проверяют корректность работы методов получения данных и заполнения таблиц.   
## Лицензия
Этот проект лицензирован под MIT License. Подробности см. в файле [LICENSE](LICENSE.txt).
## Контакты
Имя: Артем Житков
Email: aptem_deadly@mail.ru
GitHub: Artem Zhitkov