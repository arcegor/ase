import gc


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

    def preprocess(self):
        keys = list(self.data.keys())
        self.data['source'] = self.data.pop(keys[1])
        self.data['target'] = self.data.pop(keys[0])

    def process(self):
        FileManager.preprocess(self)
        self.result = pm.find_collisions(self.data)
        return True

    def clear(self):
        del self.data
        gc.collect()
        self.data = {}
