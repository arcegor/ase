import copy
import gc

import pandas as pd

from ExcelManager import ExcelManager
from ProcessManager import ProcessManager


class FileManager(object):

    def __init__(self):
        super()
        self.data = {}
        self.result = {}
        self.pm = ProcessManager()
        self.em = ExcelManager()
        self.workbook_data = {}
        self.source_filenames = {}
        self.merged_cells = {}
        self.percent = 0

    def validate(self) -> bool:
        if self.source_filenames:
            return True

    def get_result(self, flag: str, filename: str):
        self.em.save_excel(self.workbook_data[flag], filename)
        return True

    def preprocess(self):
        keys = list(self.source_filenames.keys())
        for key in keys:
            self.preprocess_excel(self.source_filenames[key], key)
            self.get_merged_cells(key)

    def process(self):
        self.preprocess()
        self.result = self.pm.find_collisions(self.data)
        wb = self.workbook_data['target']
        wb.active = self.em.process_unmerge_cells(wb.active, merged=self.merged_cells['target'],
                                                  coords=(2, 10, len(self.result['target']), 11), col=11)
        wb_new = self.em.update_spreadsheet(wb, self.pm.collisions_data, 11, 2, wb.active.title)
        wb_new.active = self.em.process_merge_cells(wb_new.active, self.merged_cells['target'], col=11)
        self.workbook_data['target'] = wb_new
        self.create_report()
        self.percent = 100 * self.pm.collisions_count / len(self.pm.collisions_data)
        return True

    def create_report(self):
        report_wb = self.em.new_wb()
        sheet = report_wb.active
        sheet['A2'].value = self.pm.collisions_count
        sheet['A1'].value = 'Количество найденных коллизий'
        report_wb.active = sheet
        self.workbook_data['report'] = report_wb
        return True

    def clear(self):
        del self.data
        gc.collect()
        self.data = {}

    def preprocess_excel(self, filename, flag):
        wb = self.em.load_excel(filename)
        self.workbook_data[flag] = wb
        self.data[flag] = pd.DataFrame(wb.active.values)

    def get_merged_cells(self, key):
        ws = self.workbook_data[key].active
        merged = copy.deepcopy(ws.merged_cells.ranges)
        self.merged_cells[key] = merged

