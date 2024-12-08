import unittest

from src.employer import Employer


class TestEmployer(unittest.TestCase):
    def test_employer_creation(self):
        employer = Employer(1, "Компания А", "https://company-a.com")
        self.assertEqual(employer.employer_name, "Компания А")
        self.assertEqual(employer.employer_url, "https://company-a.com")

    def test_cast_to_object_list(self):
        employer_data = [
            {"employer": {"id": 1, "name": "Компания А", "url": "https://company-a.com"}},
            {"employer": {"id": 2, "name": "Компания Б", "url": "https://company-b.com"}},
        ]
        employers = Employer.cast_to_object_list(employer_data)
        self.assertEqual(len(employers), 2)
        self.assertEqual(employers[0].employer_name, "Компания А")
