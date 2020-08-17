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
        with open(self.path) as f:
            for piece in self.read_in_chunks(f):
                pass

    def read_in_chunks(file_object, chunk_size=1024):
        """Lazy function (generator) to read a file piece by piece.
        Default chunk size: 1k."""
        while True:
            data = file_object.read(chunk_size)
            if not data:
                break
            yield data


