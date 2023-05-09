import os
import re
import shutil

import pandas as pd


class FileManager(object):

    def __init__(self):
        self.data = {}
        self.files = []

    @staticmethod
    def create_item(df, fname):
        path = os.getcwd() + '/TEMP'
        name = 'processed_' + re.split('/', fname)[-1]
        if not os.path.exists(path):
            os.makedirs(path)
        filepath = os.path.join(path, name)
        df.to_excel(filepath)
        return filepath

    def get_item(self):
        path = os.getcwd() + '/RESULT'
        if not os.path.exists(path):
            os.makedirs(path)
        for item in self.files:
            shutil.copy(item, path)
            file_to_delete = item
            os.remove(file_to_delete)
        if len(os.listdir(os.getcwd() + '/TEMP')) == 0:
            os.rmdir(os.getcwd() + '/TEMP')
