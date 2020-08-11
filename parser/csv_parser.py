from typing import List
import csv
from .parser import Parser


class CsvParser(Parser):

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

    def chunk_reader(self, max_rows) -> List:
        pass
