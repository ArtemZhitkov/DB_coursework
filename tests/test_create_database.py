import unittest
from unittest.mock import patch, MagicMock
from src.create_database import DBCreate


class TestDBCreate(unittest.TestCase):

    @patch("psycopg2.connect")  # Патчим psycopg2.connect
    def test_create_database(self, mock_connect):
        # Настройка мока
        mock_conn = MagicMock()
        mock_cursor = MagicMock()
        mock_conn.cursor.return_value = mock_cursor
        mock_connect.return_value = mock_conn

        # Создаем экземпляр класса
        db_creator = DBCreate(database_name="test_db")

        # Вызов метода
        db_creator.create_database()

        # Проверка, что DROP DATABASE был вызван
        mock_cursor.execute.assert_any_call("DROP DATABASE IF EXISTS test_db")

        # Проверка, что CREATE DATABASE был вызван
        mock_cursor.execute.assert_any_call("CREATE DATABASE test_db")

        # Проверка, что курсор был закрыт
        mock_cursor.close.assert_called_once()

        # Проверка, что соединение было закрыто
        mock_conn.close.assert_called()

    # @patch("psycopg2.connect")  # Патчим psycopg2.connect
    # def test_save_data_to_database(self, mock_connect):
    #     # Настройка мока для соединения и курсора
    #     mock_conn = MagicMock()
    #     mock_cursor = MagicMock()
    #     mock_conn.cursor.return_value.__enter__.return_value = mock_cursor
    #     mock_connect.return_value = mock_conn
    #
    #     # Создаем экземпляр класса DBCreate
    #     db_creator = DBCreate(database_name="test_db")
    #
    #     # Подготовка тестовых данных
    #     test_data = [
    #         {
    #             "employers": [
    #                 {"employer_id": 1, "employer_name": "Компания А", "employer_url": "https://company-a.com"},
    #                 {"employer_id": 2, "employer_name": "Компания Б", "employer_url": "https://company-b.com"},
    #             ],
    #             "vacancies": [
    #                 {
    #                     "name": "Вакансия 1",
    #                     "employer_id": 1,
    #                     "url": "https://vacancy-1.com",
    #                     "area": "Москва",
    #                     "salary": 100000,
    #                     "description": "Описание вакансии 1",
    #                 },
    #                 {
    #                     "name": "Вакансия 2",
    #                     "employer_id": 2,
    #                     "url": "https://vacancy-2.com",
    #                     "area": "Санкт-Петербург",
    #                     "salary": 80000,
    #                     "description": "Описание вакансии 2",
    #                 },
    #             ],
    #         }
    #     ]
    #
    #     # Вызов метода save_data_to_database
    #     db_creator.save_data_to_database(test_data)
    #
    #     # Проверка, что курсор выполняет вставку для работодателей
    #     mock_cursor.execute.assert_any_call(
    #         """INSERT INTO employees (employer_id, employer_name, employer_url)
    #            VALUES (%s, %s, %s) ON CONFLICT DO NOTHING""",
    #         (1, "Компания А", "https://company-a.com"),
    #     )
    #     mock_cursor.execute.assert_any_call(
    #         """INSERT INTO employees (employer_id, employer_name, employer_url)
    #            VALUES (%s, %s, %s) ON CONFLICT DO NOTHING""",
    #         (2, "Компания Б", "https://company-b.com"),
    #     )
    #
    #     # Проверка, что курсор выполняет вставку для вакансий
    #     mock_cursor.execute.assert_any_call(
    #         """INSERT INTO vacancies (vacancy_name, employer_id, vacancy_url, area, salary, description)
    #            VALUES (%s, %s, %s, %s, %s, %s)""",
    #         ("Вакансия 1", 1, "https://vacancy-1.com", "Москва", 100000, "Описание вакансии 1"),
    #     )
    #     mock_cursor.execute.assert_any_call(
    #         """INSERT INTO vacancies (vacancy_name, employer_id, vacancy_url, area, salary, description)
    #            VALUES (%s, %s, %s, %s, %s, %s)""",
    #         ("Вакансия 2", 2, "https://vacancy-2.com", "Санкт-Петербург", 80000, "Описание вакансии 2"),
    #     )
    #
    #     # Проверка, что commit был вызван
    #     mock_conn.commit.assert_called_once()
    #
    #     # Проверка, что соединение было закрыто
    #     mock_conn.close.assert_called_once()
