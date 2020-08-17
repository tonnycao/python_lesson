from typing import List
import csv
from .parser import Parser
import pandas as pd


class CsvParser(Parser):
    call_counter = 0

    def __init__(self, path, delimiter=None):
        self.rows = 0
        self.path = path

        if delimiter is None:
            delimiter = ','
        self.delimiter = delimiter

    def reader(self) -> List:
        i = 0
        data = []
        with open(self.path, newline='') as f:
            reader = csv.reader(f, delimiter=self.delimiter)

            for row in reader:
                if i > 0:
                    data.append(row)
                i += 1
            self.rows = i

        return data

    def chunk_reader(self, chunk_size=1024) -> List:
        CsvParser.call_counter += 1
        i = 0
        data = []
        for df in pd.read_csv(self.path, chunksize=chunk_size,
                              delimiter=self.delimiter, encoding='utf-8'):

            for row in df:
                if CsvParser.call_counter == 0 and i > 0:
                    data.append(row)
                elif CsvParser.call_counter > 0:
                    data.append(row)
                i += 1

        return data
