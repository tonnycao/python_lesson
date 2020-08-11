from typing import List

from .parser import Parser


class TxtParser(Parser):

    def __init__(self, path, delimiter):
        self.path = path
        self.delimiter = delimiter
        self.rows = 0

    def reader(self) -> List:
        data = []

        with open(self.path, mode='r', encoding='utf-8') as f:
            lines = f.readlines()
            i = 0
            for line in lines:
                if i > 0:
                    item = line.split(self.delimiter)
                    data.append(item)
                i += 1
            self.rows = i

        return data

    def chunk_reader(self, max_rows) -> List:
        pass
