from typing import List

from .parser import Parser


class TxtParser(Parser):
    count = 0
    offset = None

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
        data = []
        with open(self.path) as f:
            if TxtParser.offset:
                f.seek(TxtParser.offset)
            row = 0
            while row < max_rows-1:
                row += 1
                row_data = f.readline()
                if not row_data:
                    break
                data.append(row_data)
                if row == max_rows:
                    TxtParser.offset = f.tell()
                    break

        TxtParser.count += 1

        return data

    @staticmethod
    def read_in_chunks(file_object, chunk_size=1024):
        while True:
            data = file_object.read(chunk_size)
            if not data:
                break
            yield data

