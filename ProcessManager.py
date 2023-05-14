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

    # Метод обрабатывает исходную строку с кодом KKS, возвращает список из буквенной и числовой части (частей) кода KKS,
    @staticmethod
    def prepare_kks(kks: str) -> list:
        kks_pattern = re.compile('[A-Z]+')
        number_pattern = re.compile('[0-9]+\s*[,-/]?\s*[0-9]*')
        kks_part = re.search(kks_pattern, kks)
        number_part = re.search(number_pattern, kks)
        if kks_part:
            kks_part = kks_part.group(0).replace(' ', '')
        else:
            kks_part = ''
        if number_part:
            number_part = number_part.group(0).replace(' ', '')
        else:
            number_part = ''
        result = [kks_part, number_part]
        return result
