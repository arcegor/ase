import gc

import pandas as pd

from ProcessManager import ProcessManager as pm


class FileManager(object):

    def __init__(self):
        self.data = {}
        self.result = {}

    def validate(self) -> bool:
        # TO DO: (Ваня, это пункт 2-3 в ТЗ)
        # сделать проверку данных на соответствие шаблону
        # Результ True если все хорошо, False - иначе (тип bool)
        pass

    def get_result(self, result: list[pd.DataFrame]) -> str:
        # TO DO: (Егор, это пункт 7 в ТЗ)
        # результирующие датафреймы result нужно записать в файлы excel
        # (в будущем возможно и другие форматы) в папку "Результат", вернуть имя файла
        pass

    def process(self, data):
        self.result = pm.find_collisions(data)
        pass

    def clear(self):
        del self.data
        gc.collect()
        self.data = {}
