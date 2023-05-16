import re

import pandas as pd


class ProcessManager(object):

    @staticmethod
    def find_collisions(data: dict):
        names = data.keys()
        result = {}
        for name in names:
            name_new = re.split(' ', name)[-1]
            result[name_new] = data[name].iloc[:10]
        return result

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
