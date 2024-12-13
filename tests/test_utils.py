import unittest

from src.employer import Employer
from src.utils import cast_objects_to_dict
from src.vacancy import Vacancy


class TestCastObjectsToDict(unittest.TestCase):

    def setUp(self):
        self.vacancies = [
            Vacancy(
                name="Junior Python Developer",
                employer_id=1,
                url="https://example.com/vacancy1",
                area="Moscow",
                salary=50000,
                description="Description for Junior Python Developer",
            )
        ]
        self.employers = [
            Employer(employer_id=1, employer_name="Tech Corp", employer_url="https://example.com/company1")
        ]
        self.result = cast_objects_to_dict(self.vacancies, self.employers)

    def test_cast_objects_to_dict(self):
        expected_result = [
            {
                "vacancies": [
                    {
                        "name": "Junior Python Developer",
                        "employer_id": 1,
                        "url": "https://example.com/vacancy1",
                        "area": "Moscow",
                        "salary": 50000,
                        "description": "Description for Junior Python Developer",
                    }
                ],
                "employers": [
                    {"employer_id": 1, "employer_name": "Tech Corp", "employer_url": "https://example.com/company1"}
                ],
            }
        ]
        self.assertEqual(self.result, expected_result)

    def test_empty_lists(self):
        empty_vacancies = []
        empty_employers = []
        result = cast_objects_to_dict(empty_vacancies, empty_employers)
        self.assertEqual(result, [{"vacancies": [], "employers": []}])

    def test_single_vacancy_multiple_employers(self):
        multiple_employers = [
            Employer(employer_id=1, employer_name="Tech Corp", employer_url="https://example.com/company1"),
            Employer(employer_id=2, employer_name="IT Solutions", employer_url="https://example.com/company2"),
        ]
        result = cast_objects_to_dict([self.vacancies[0]], multiple_employers)
        self.assertEqual(len(result), 1)
        self.assertEqual(len(result[0]["employers"]), 2)

    def test_no_vacancies(self):
        no_vacancies = []
        result = cast_objects_to_dict(no_vacancies, self.employers)
        self.assertEqual(result[0]["vacancies"], [])

    def test_no_employers(self):
        no_employers = []
        result = cast_objects_to_dict(self.vacancies, no_employers)
        self.assertEqual(result[0]["employers"], [])
