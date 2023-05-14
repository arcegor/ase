import re

import pandas as pd


class ProcessManager(object):

    @staticmethod
    def find_collisions(data: list[pd.DataFrame]):
        # TO DO: (Соня, это пункт 4-6 в ТЗ)
        # Здесь нужно реализовать сам поиск коллизий.
        # На вход подается список датафреймов (один эталонный и второй целевой).
        # На выходе нужно вернуть два датафрейма: отчет о найденных ошибках и отредоктированный целевой документ
        pass

    @staticmethod
    def validate_kks(kks: str) -> bool:
        result = False
        pattern = re.compile('^\s?[A-Z]+\s?[0-9]?')
        return result
