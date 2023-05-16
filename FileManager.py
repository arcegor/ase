import gc

import pandas as pd

from ProcessManager import ProcessManager as pm


class FileManager(object):

    def __init__(self):
        self.data = {}
        self.result = {}

    def validate(self) -> bool:
        if self.data:
            return True

    def get_result(self) -> list:
        keys = self.result.keys()
        for key in keys:
            self.result[key].to_excel(key)
        return list(keys)

    def process(self):
        try:
            self.result = pm.find_collisions(self.data)
        except BaseException:
            return False
        return True

    def clear(self):
        del self.data
        gc.collect()
        self.data = {}
