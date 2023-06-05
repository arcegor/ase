import re
import traceback


class CalcManager(object):

    def __init__(self, data):
        super().__init__()
        self.data = data
        self.result = None

    @staticmethod
    def parse_row(row):
        between_pattern = re.compile('отметки')
        on_pattern = re.compile('отметке')
        link_to_table_pattern = re.compile('таблицу')
        level_from_pattern = re.compile('-\d+,\d+')
        level_to_pattern = re.compile('\+\d+,\d+')
        between_part = re.search(between_pattern, row)
        on_part = re.search(on_pattern, row)
        link_to_table_part = re.search(link_to_table_pattern, row)
        if link_to_table_part:
            return None
        if on_part:
            lfp = re.search(level_from_pattern, row)
            ltp = re.search(level_to_pattern, row)
            if lfp:
                lfp = float(lfp.group(0).replace(',', '.').replace(' ', ''))
            else:
                lfp = None
            if ltp:
                ltp = float(ltp.group(0).replace(',', '.').replace(' ', ''))
            else:
                ltp = None
            return 'o', lfp, ltp
        if between_part:
            lfp = re.search(level_from_pattern, row)
            ltp = re.search(level_to_pattern, row)
            if lfp:
                lfp = float(lfp.group(0).replace(',', '.').replace(' ', ''))
            else:
                lfp = None
            if ltp:
                ltp = float(ltp.group(0).replace(',', '.').replace(' ', ''))
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
            if not isinstance(flag, str):
                continue
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
                if index - tmp_index > 2:
                    result.append([tmp_index, index, res_old])
            res_old = res
            tmp_index = index
        trees = self.process_trees(result)
        self.calc_trees(trees)
        return trees

    def process_trees(self, indexes):
        result = []
        for scope in indexes:
            start, stop, flag, down, top = scope[0] + 1, scope[1], scope[2][0], scope[2][1], scope[2][2]
            df_temp = self.data.iloc[start:stop, :]
            result += self.process_scope(df_temp, flag)
        return result

    @staticmethod
    def process_scope(df_scope, flag):
        res = None
        if flag == 'o':
            res = CalcManager.calc_on(df_scope)
        else:
            if flag == 'b':
                res = CalcManager.calc_between(df_scope)
        return res

    @staticmethod
    def calc_on(df_scope):
        res = []
        order_number, kks, depth, heat_isolation, neighbouring_areas, z = None, None, None, None, None, None
        for index, row in df_scope.iterrows():
            if isinstance(row[0], int):
                order_number, kks, heat_isolation, neighbouring_areas = row[0], row[1], row[10], row[13]
                res.append([order_number, kks, depth, heat_isolation, neighbouring_areas, z])
        return res

    @staticmethod
    def calc_between(df_scope):
        res = []
        order_number, kks, depth, heat_isolation, neighbouring_areas, z = None, None, None, None, None, None
        for index, row in df_scope.iterrows():
            if row[0] is None:
                try:
                    z = int(row[2])
                except TypeError:
                    continue
                except ValueError:
                    continue
            if z is not None:
                res.append([order_number, kks, depth, heat_isolation, neighbouring_areas, z])
                z = None
            if isinstance(row[0], int):
                order_number, kks, depth, heat_isolation, neighbouring_areas = row[0], row[1], row[6], row[10], row[13]
        res.append([order_number, kks, depth, heat_isolation, neighbouring_areas, z])
        return res

    def calc_trees(self, trees):
        for tree in trees:
            pass
