import unittest
from unittest.mock import patch, MagicMock
from src.search_vacancies import SearchVacancies


class TestSearchVacancies(unittest.TestCase):

    def setUp(self):
        self.search = SearchVacancies()

    @patch("requests.get")
    def test_successful_search(self, mock_get):

        mock_response = MagicMock()
        mock_response.json.return_value = {"items": [{"id": 1}, {"id": 2}, {"id": 3}], "pages": 10}
        mock_get.return_value = mock_response

        vacancies = self.search.search_query()

        self.assertEqual(len(vacancies), 30)
        self.assertEqual(self.search._SearchVacancies__params["page"], 10)

    @patch("requests.get")
    def test_empty_search(self, mock_get):

        mock_response = MagicMock()
        mock_response.json.return_value = {"items": [], "pages": 0}
        mock_get.return_value = mock_response

        vacancies = self.search.search_query()

        self.assertEqual(len(vacancies), 0)
        self.assertEqual(self.search._SearchVacancies__params["page"], 0)

    @patch("requests.get")
    def test_error_response(self, mock_get):

        mock_response = MagicMock()
        mock_response.status_code = 500
        mock_get.return_value = mock_response

        with self.assertRaises(Exception):
            self.search.search_query()

    @patch("requests.get")
    def test_single_page_search(self, mock_get):

        mock_response = MagicMock()
        mock_response.json.return_value = {"items": [{"id": 1}, {"id": 2}], "pages": 10}
        mock_get.return_value = mock_response

        vacancies = self.search.get_vacancies(0)

        self.assertEqual(len(vacancies), 2)
