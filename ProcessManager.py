import re

import numpy as np
import pandas as pd


class ProcessManager(object):

    def __init__(self):
        super()
        self.target_kks = set()
        self.collisions_data = []
        self.collisions_count = 0

    def find_collisions(self, data: dict, progress):
        result = {'target': self.compare_frames_by_kks(data['source'], data['target'], progress)}
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

    def create_source_set(self, source: pd.DataFrame, progress):
        res = set()
        df = source.iloc[:, 2].dropna().unique().tolist()[1:]
        shift = 50 / len(df)
        for index, item in enumerate(df):
            item = self.prepare_kks(item)
            res = res.union(self.create_kks_set(item))

            progress.setValue(index * shift)
            progress.setFormat('Поиск коллизий {0:.2f}%'.format(index * shift))
        return res, progress

    def compare_frames_by_kks(self, source: pd.DataFrame, target: pd.DataFrame, progress) -> pd.DataFrame:
        self.target_kks, progress = self.create_source_set(source, progress)
        shift = 50 / len(target[[10]])
        try:
            target[[10]] = \
                target.apply(
                    lambda x: self.check_collision(x[[1]], x[[10]], progress, shift),
                    axis=1)
        except ValueError:
            target[[10]] = pd.DataFrame([x[0] for x in self.collisions_data])
        return target

    def check_collision(self, x, y, progress, shift):
        progress.setValue(len(self.collisions_data) * shift)
        progress.setFormat('Поиск коллизий {0:.2f}%'.format(len(self.collisions_data) * shift))
        x, y = str(x.item()), str(y.item())
        if y == 'None':
            self.collisions_data.append((np.NaN, 0))
            return np.NaN
        if y in ['-', '0']:
            if x in self.target_kks:
                self.collisions_data.append((1, 1))
                self.collisions_count += 1
                return 1
            else:
                self.collisions_data.append((0, 0))
                return 0
        else:
            if x not in self.target_kks:
                self.collisions_data.append((0, 1))
                self.collisions_count += 1
                return 0
            else:
                self.collisions_data.append((1, 0))
                return 1

    @staticmethod
    def generate_name(old_names, name) -> str:
        new_name = re.split(r'[\\/.]+', old_names[name])[-2] + '.xlsx'
        return new_name
