import unittest

from src.vacancy import Vacancy


class TestVacancy(unittest.TestCase):
    def test_vacancy_creation(self):
        vacancy = Vacancy("Программист", 1, "https://example.com", None, None, None)
        self.assertEqual(vacancy.area, "Регион не указан")
        self.assertEqual(vacancy.salary, 0)
        self.assertEqual(vacancy.description, "Описание отсутствует")

    def test_vacancy_string(self):
        vacancy = Vacancy("Программист", 1, "https://example.com", "Москва", 100000, "Знание Python")
        self.assertEqual(
            str(vacancy), "Программист: Знание Python, Регион: Москва, Зарплата: 100000, Ссылка: https://example.com"
        )

    def test_cast_to_object_list(self):
        vacancies_data = [
            {
                "name": "Программист",
                "employer": {"id": 1},
                "alternate_url": "https://example.com",
                "area": {"name": "Москва"},
                "salary": {"from": 100000},
                "snippet": {"requirement": "Знание Python"},
            }
        ]
        vacancies = Vacancy.cast_to_object_list(vacancies_data)
        self.assertEqual(len(vacancies), 1)
        self.assertEqual(vacancies[0].name, "Программист")
