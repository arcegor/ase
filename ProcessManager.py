import re

import pandas as pd


class ProcessManager(object):

    def __init__(self):
        super()

    @staticmethod
    def find_collisions(data: dict):
        result = {'target': ProcessManager.compare_frames_by_kks(data['source'], data['target'])}
        return result

    @staticmethod
    def prepare_kks(kks: str) -> list:
        kks_pattern = re.compile('\s*[A-Z]+')
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

    @staticmethod
    def create_kks_set(kks: list) -> set:
        kks_set = set()
        number_part = kks[1]
        str_part = kks[0]
        if number_part == '':
            kks_set.add(str_part)
        if len(re.findall(r'[0-9]+', number_part)) == 1:
            kks_set.add(str_part + number_part)
        if len(re.findall(r'-', number_part)) > 0:
            start = int(re.split(r'-', number_part)[0])
            end = int(re.split(r'-', number_part)[1])
            for i in range(start, end):
                item = str_part + str(i)
                kks_set.add(item)
        if len(re.findall(r'[/,]', number_part)) > 0:
            temp = re.split(r'[/,]', number_part)
            for i in temp:
                item = str_part + i
                kks_set.add(item)
        return kks_set

    @staticmethod
    def create_source_set(source: pd.DataFrame):
        res = set()
        df = source.iloc[:, 2].dropna().unique().tolist()[1:]
        for item in df:
            item = ProcessManager.prepare_kks(item)
            res = res.union(ProcessManager.create_kks_set(item))
        return res

    @staticmethod
    def compare_frames_by_kks(source: pd.DataFrame, target: pd.DataFrame):
        source = ProcessManager.create_source_set(source)
        target = target[['Код системы (KKS)', 'Толщина изоляции трубопро вода Sи,']]
        return target

    @staticmethod
    def generate_name(old_name) -> str:
        name = re.split(r'[\/.]+', old_name)[-2]
        name = name.join('.xlsm')
        return name
