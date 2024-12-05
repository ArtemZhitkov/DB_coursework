from typing import Any

import requests

from src.base_class import Api


class SearchVacancies(Api):
    """Класс для поиска вакансий с помощью API"""

    def __init__(self) -> None:
        self.__url = "https://api.hh.ru/vacancies"
        self.__headers = {"User-Agent": "HH-User-Agent"}
        self.__params = {
            "employer_id": [
                "78638",
                "2180",
                "2748",
                "3529",
                "4716984",
                "5516123",
                "3776",
                "2738360",
                "5331842",
                "1740",
            ],
            "page": 0,
            "per_page": 100,
        }
        self.__vacancies: list[Any] = []

    def search_query(self) -> Any:
        # self.__params["text"] = keyword
        while self.__params.get("page") != 20:
            response = requests.get(self.__url, headers=self.__headers, params=self.__params)
            if response.status_code == 200:
                vacancies = response.json()["items"]
                self.__vacancies.extend(vacancies)
                self.__params["page"] += 1
        return self.__vacancies
