from typing import List
from .parser import Parser
import xlrd
import pandas as pd


class ExcelParser(Parser):

    def __init__(self, path, index):
        self.path = path
        self._index = index
        self.rows = 0
        self.cols = 0

    @property
    def index(self):
        return self._index

    @index.setter
    def index(self, n):
        self._index = n

    def chunk_reader(self, max_rows) -> List:
        data = []
        df = pd.read_excel(self.path, skiprows=max_rows)
        for chunk in df:
            data.append(chunk)
        return data

    def reader(self) -> List:
        data = []
        workbook = xlrd.open_workbook(self.path)
        sheet = workbook.sheet_by_index(self._index)
        self.rows = sheet.nrows
        self.cols = sheet.ncols
        for i in range(self.rows):
            data.append(sheet.row_values(i))

        return data