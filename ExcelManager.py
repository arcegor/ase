from copy import copy

import openpyxl


class ExcelManager:
    def __init__(self):
        super()

    @staticmethod
    def update_spreadsheet(wb: openpyxl.Workbook, df, start_col: int, start_row: int, sheet_name: str):
        """
        :param wb: Workbook excel
        :param df: Датафрейм Pandas для записи
        :param start_col: Стартовая колонка в таблице листа Excel, куда буду писать данные
        :param start_row: Стартовая строка в таблице листа Excel, куда буду писать данные
        :param sheet_name: Имя листа в таблице Excel, куда буду писать данные
        :return:
        """

        for ir in range(0, len(df)):
            for ic in range(0, len(df.iloc[ir])):
                wb[sheet_name].cell(start_row + ir, start_col + ic).value = df.iloc[ir][ic]
        return wb

    @staticmethod
    def load_excel(path: str):
        return openpyxl.load_workbook(path)

    @staticmethod
    def save_excel(wb, path):
        return wb.save(path)

    @staticmethod
    def process_unmerge_cells(ws, merged):
        for group in list(merged):
            min_col, min_row, max_col, max_row = group.bounds
            cell_start = ws.cell(row=min_row, column=min_col)
            top_left_cell_value = cell_start.value

            ws.unmerge_cells(str(group))

            for i_row in range(min_row, max_row + 1):
                for j_col in range(min_col, max_col + 1):
                    ws.cell(row=i_row, column=j_col, value=top_left_cell_value)
                    # copy the cell format
                    ws.cell(row=i_row, column=j_col).alignment = copy(cell_start.alignment)
                    ws.cell(row=i_row, column=j_col).border = copy(cell_start.border)
                    ws.cell(row=i_row, column=j_col).font = copy(cell_start.font)
        return ws

    @staticmethod
    def process_merge_cells(ws, merged):
        for group in list(merged):
            ws.merge_cells(str(group))
        return ws
