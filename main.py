from __future__ import annotations
from parser.parser import Parser
from parser.csv_parser import CsvParser
from parser.txt_parser import TxtParser
from model.gmacc import Gmacc
from model.zotfov import Zotfov
from typing import List
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base


class Context():

    def __init__(self, session, strategy: Parser) -> None:
        self._strategy = strategy
        self.session = session

    @property
    def strategy(self) -> Parser:
        return self._strategy

    @strategy.setter
    def strategy(self, strategy: Parser) -> None:
        self._strategy = strategy

    def read_data(self) -> List:
        result = self._strategy.reader()
        return result

    def storage_data(self, cls, data):
        self.session.bulk_insert_mappings(cls,
                               [dict(name="u1"), dict(name="u2"), dict(name="u3")]
                               )
        self.session.commit()


if __name__ == '__main__':
    engine = create_engine('mysql+pymysql://root:@localhost:3306/db_example?charset=utf8mb4', pool_recycle=3600)
    DBSession = sessionmaker(bind=engine)
    session = DBSession()
    cc = Context(session, CsvParser('gmacc.csv'))
    data = cc.read_data()
    cc.storage_data(Gmacc, data)