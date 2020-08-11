from abc import ABC, abstractmethod
from typing import List


class Parser:

    @abstractmethod
    def reader(self) -> List:
        pass

    @abstractmethod
    def chunk_reader(self, max_rows) -> List:
        pass