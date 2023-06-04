import re


class CalcManager(object):

    def __init__(self, data):
        super().__init__()
        self.data = data
        self.result = None

    @staticmethod
    def parse_row(row):
        between_pattern = re.compile('\s*отметки')
        on_pattern = re.compile('\s*перекрытие\s*на\s*отметке')
        level_from_pattern = re.compile('\s*-\d*,\d*')
        level_to_pattern = re.compile('\s*\+\d*,\d*')
        between_part = re.search(between_pattern, row).group(0).replace(',', '.')
        on_part = re.search(on_pattern, row).group(0).replace(',', '.')
        if on_part:
            lfp = re.search(level_from_pattern, row).group(0).replace(',', '.')
            ltp = re.search(level_to_pattern, row).group(0).replace(',', '.')
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
            lfp = re.search(level_from_pattern, row).group(0).replace(',', '.')
            ltp = re.search(level_to_pattern, row).group(0).replace(',', '.')
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
        for index, row in self.data.iterrows():
            row = row.tolist()
            try:
                res = CalcManager.parse_row(row[0])
            except TypeError:
                continue
            if not res:
                continue
            flag, down, up = res

    def check_trees(self):
        pass
