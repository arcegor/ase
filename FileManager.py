import gc
import os

import pandas as pd

from ProcessManager import ProcessManager
import openpyxl


class FileManager(object):

    def __init__(self):
        self.data = {}
        self.styles = {}
        self.result = {}
        self.pm = ProcessManager()
        self.source_filenames = {}
        self.flag_source = False
        self.flag_target = False

    def validate(self) -> bool:
        if self.data:
            return True

    def get_result(self, flag: str):
        keys = list(self.result.keys())
        path = os.getcwd() + '/RESULT'
        if not os.path.exists(path):
            os.makedirs(path)
        if flag in keys:
            name = self.pm.generate_name(self.source_filenames, flag)
            filepath = os.path.join(path, name)
            self.result[flag].to_excel(filepath)
        return True

    def preprocess(self):
        keys = list(self.data.keys())
        self.source_filenames['source'] = keys[1]
        self.source_filenames['target'] = keys[0]
        self.data['source'] = self.data.pop(keys[1])
        self.data['target'] = self.data.pop(keys[0])

    def process(self):
        # self.preprocess()
        # self.result = self.pm.find_collisions(self.data)
        return True

    def clear(self):
        del self.data
        gc.collect()
        self.data = {}


