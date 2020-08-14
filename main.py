from __future__ import annotations
import pprint
import time
from parser.parser import Parser
from parser.csv_parser import CsvParser
from parser.txt_parser import TxtParser
from model.gmacc import Gmacc
from model.zotfov import Zotfov
from typing import List
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
from sqlalchemy import inspect
from sqlalchemy.ext.declarative import declarative_base


def timeit(method):
    def timed(*args, **kw):
        ts = time.time()
        result = method(*args, **kw)
        te = time.time()
        if 'log_time' in kw:
            name = kw.get('log_name', method.__name__.upper())
            kw['log_time'][name] = int((te - ts) * 1000)
        else:
            print('%r  %2.2f ms' % (method.__name__, (te - ts) * 1000))
        return result
    return timed


class Context():

    def __init__(self, session, columns, strategy: Parser) -> None:
        self._strategy = strategy
        self.session = session
        self.columns = columns

    @property
    def strategy(self) -> Parser:
        return self._strategy

    @strategy.setter
    def strategy(self, strategy: Parser) -> None:
        self._strategy = strategy

    @timeit
    def read_data(self) -> List:
        result = self._strategy.reader()
        return result

    @staticmethod
    def clear_item(item):
        return item.strip().replace("\"", "").replace(",", "")

    @timeit
    def storage_data_batch(self, cls, data):
        size = 2000
        rows = []
        for raw in data:
            i = map(self.clear_item, raw)
            item = dict(zip(tuple(self.columns), tuple(i)))
            rows.append(item)
            if len(rows) == size:
                self.session.bulk_insert_mappings(cls,rows)
                self.session.commit()
                rows = []

        if len(rows) > 0:
            self.session.bulk_insert_mappings(cls, rows)
            self.session.commit()

    @timeit
    def storage_data(self, cls, data):
        mapper = inspect(cls)
        fields = mapper.all_orm_descriptors.keys()
        for raw in data:
            i = map(self.clear_item, raw)
            item = dict(zip(tuple(self.columns), tuple(i)))
            self.session.bulk_insert_mappings(cls, [item])
            self.session.commit()


if __name__ == '__main__':
    engine = create_engine('mysql+pymysql://root:@localhost:3306/db_example?charset=utf8mb4', pool_recycle=3600)
    DBSession = sessionmaker(bind=engine)
    session = DBSession()
    mapper = inspect(Gmacc)
    # get table column
    gmacc_column = [
        'sales_organisation_cd',
        'apple_id',
        'cust_id',
        'legal_name',
        'price_grp_cd',
        'auth_description',
        'billing_block_cd',
        'order_block_cd',
        'delivery_block_cd',
        'posting_block_cd',
        'sales_block_cd',
        'marked_for_delete_ind',
        'acct_status_cd'
    ]
    cc = Context(session, gmacc_column, CsvParser('gmacc.csv'))
    data = cc.read_data()
    cc.storage_data_batch(Gmacc, data)