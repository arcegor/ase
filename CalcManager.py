import re
import traceback


class CalcManager(object):

    def __init__(self, data):
        super().__init__()
        self.data = data
        self.result = None

    @staticmethod
    def parse_row(row):
        if not isinstance(row, str):
            return None
        between_pattern = re.compile('отметки')
        on_pattern = re.compile('перекрытие\s*на\s*отметке')
        link_to_table_pattern = re.compile('таблицу')
        level_from_pattern = re.compile('-\d*,\d*')
        level_to_pattern = re.compile('\+\d*,\d*')
        between_part = re.search(between_pattern, row)
        on_part = re.search(on_pattern, row)
        link_to_table_part = re.search(link_to_table_pattern, row)
        if link_to_table_part:
            return None
        if on_part:
            lfp = re.search(level_from_pattern, row).group(0).replace(',', '.').replace(' ', '')
            ltp = re.search(level_to_pattern, row).group(0).replace(',', '.').replace(' ', '')
            if lfp:
                lfp = float(lfp)
            else:
                lfp = None
            if ltp:
                ltp = float(ltp)
            else:
                ltp = None
            return 'o', lfp, ltp
        if between_part:
            lfp = re.search(level_from_pattern, row).group(0).replace(',', '.').replace(' ', '')
            ltp = re.search(level_to_pattern, row).group(0).replace(',', '.').replace(' ', '')
            if lfp:
                lfp = float(lfp)
            else:
                lfp = None
            if ltp:
                ltp = float(ltp)
            else:
                ltp = None
            return 'b', lfp, ltp
        return None

    def process_calc(self):
        result = []
        tmp_index = None
        res_old = None
        for index, row in self.data.iterrows():
            row = row.tolist()
            flag = row[0]
            try:
                res = CalcManager.parse_row(flag)
            except AttributeError:
                traceback.print_exc()
                continue
            except TypeError:
                traceback.print_exc()
                continue
            if not res:
                continue
            if tmp_index and tmp_index != index:
                result.append([tmp_index, index, res_old])
            res_old = res
            tmp_index = index
        self.process_trees(result)

    def process_trees(self, indexes):
        pass
