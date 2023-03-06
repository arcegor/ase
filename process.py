import os
import re
import shutil

import pandas as pd


class FileManager(object):

    def __init__(self):
        self.data = {}
        self.files = []

    def process_all(self, progress):
        for key in self.data.keys():
            df = self.process_item(self.data[key], progress)
            self.files.append(self.create_item(df, key))

    @staticmethod
    def process_item(df, progress):
        df_new = pd.DataFrame(columns=['Система по ККС', 'Количество', '№ помещения', 'Категория'])
        length = df.shape[0] / 100
        for index, row in df.iterrows():
            progress.setValue(index / length)
            progress.setFormat('{0:.2f}%'.format(index / length))
            zone_number = row['№ помещения']
            kks_system = row['Система по ККС']
            count = row['Количество']
            category = row['Категория']
            tmp = re.split(' / ', str(zone_number))
            if len(tmp) == 0:
                continue
            if len(tmp) == 2:
                new_row_2 = [kks_system, count, tmp[1].strip(), category]
                df_new.loc[-1] = new_row_2
                df_new.index = df_new.index + 1
            new_row_1 = [kks_system, count, tmp[0].strip(), category]
            df_new.loc[-1] = new_row_1
            df_new.index = df_new.index + 1
        df_new = df_new.sort_index()
        df_new = df_new.dropna()
        return df_new

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
