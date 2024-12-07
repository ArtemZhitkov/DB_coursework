from typing import Any

import psycopg2

from config import config


class DBCreate:
    """Класс создает и заполняет таблицы PostgreSQL"""
    def __init__(self):
        self.database_name = "hh_ru"
        self.__params = config()
        self.__conn = psycopg2.connect(dbname="postgres", **self.__params)

    def create_database(self) -> None:
        """Метод создает базу данных и таблицы"""
        conn = self.__conn
        conn.autocommit = True
        cur = conn.cursor()
        try:
            cur.execute(f"DROP DATABASE {self.database_name}")
        except Exception as e:
            print(f"Произошла ошибка: {e}")
        # else:
        #     cur.execute(f"DROP DATABASE {database_name}")
        finally:
            cur.execute(f"CREATE DATABASE {self.database_name}")

        conn.close()

        conn = psycopg2.connect(dbname=self.database_name, **self.__params)

        with conn.cursor() as cur:
            cur.execute(
                """
                CREATE TABLE employees (
                employer_id INT PRIMARY KEY,
                employer_name VARCHAR(255) NOT NULL,
                employer_url TEXT NOT NULL
                )
            """
            )

        with conn.cursor() as cur:
            cur.execute(
                """
                CREATE TABLE vacancies (
                employer_id INT REFERENCES employees(employer_id),
                vacancy_name VARCHAR(255) NOT NULL,
                vacancy_url TEXT PRIMARY KEY,
                area VARCHAR(255) NOT NULL,
                salary INT,
                description TEXT
                )
            """
            )
        conn.commit()
        conn.close()

    def save_data_to_database(self, data: list[dict[str, Any]]) -> None:
        """Метод заполняет таблицы данными"""

        conn = self.__conn = psycopg2.connect(dbname=self.database_name, **self.__params)

        with conn.cursor() as cur:
            for vacancy in data:
                employer_id = vacancy["employer"]["id"]
                if vacancy["salary"] is None:
                    salary = 0
                else:
                    salary = vacancy["salary"]["from"]
                cur.execute(
                    """
                    INSERT INTO employees (employer_id, employer_name, employer_url)
                    VALUES (%s, %s, %s) on conflict do nothing
                    RETURNING employer_id""",
                    (vacancy["employer"]["id"], vacancy["employer"]["name"], vacancy["employer"]["url"]),
                )

                cur.execute(
                    """
                    INSERT INTO vacancies (employer_id, vacancy_name, vacancy_url,
                    area, salary, description)
                    VALUES (%s, %s, %s, %s, %s, %s)""",
                    (
                        employer_id,
                        vacancy["name"],
                        vacancy["alternate_url"],
                        vacancy["area"]["name"],
                        salary,
                        vacancy["snippet"]["requirement"],
                    ),
                )
        conn.commit()
        conn.close()
