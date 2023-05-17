import gc
import os

from ProcessManager import ProcessManager


class FileManager(object):

    def __init__(self):
        self.data = {}
        self.result = {}
        self.pm = ProcessManager()
        self.source_filenames = {}

    def validate(self) -> bool:
        if self.data:
            return True

    def get_result(self) -> list:
        keys = self.result.keys()
        path = os.getcwd() + '/RESULT'
        if not os.path.exists(path):
            os.makedirs(path)
        for key in keys:
            name = self.pm.generate_name(self.source_filenames, key)
            filepath = os.path.join(path, name)
            self.result[key].to_excel(filepath)
        return list(keys)

    def preprocess(self):
        keys = list(self.data.keys())
        self.source_filenames['source'] = keys[1]
        self.source_filenames['target'] = keys[0]
        self.data['source'] = self.data.pop(keys[1])
        self.data['target'] = self.data.pop(keys[0])

    def process(self):
        self.preprocess()
        self.result = self.pm.find_collisions(self.data)
        return True

    def clear(self):
        del self.data
        gc.collect()
        self.data = {}


