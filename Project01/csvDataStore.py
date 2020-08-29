from xlrd import open_workbook
import csv


def readData(file_path):
    if file_path.endswith("csv"):
        with open(file_path, 'r') as f:
            reader = csv.reader(f)
            list = []
            for i in reader:
                list.append(i)
            list.pop(0)
            return list
    else:
        data = open_workbook(file_path, encoding_override='utf-8')
        table = data.sheets()[0]
        rows = table.nrows
        cols = table.ncols
        list = []
        for i in range(1, rows):
            row_data = table.row_values(i)
            list.append(row_data)
        return list


import pymysql
from sqlalchemy import Column, String, create_engine, Float, MetaData, Table, Integer
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

engine = create_engine('mysql+pymysql://root:P4ssword@localhost:3306/QA?charset=utf8', pool_recycle=10000)
Base = declarative_base()
metadata = MetaData(engine)


class CsvTable(Base):
    __tablename__ = "csv_table"

    id = Column(Integer, primary_key=True)
    sales_organisation_cd = Column(Integer, nullable=True)
    apple_id = Column(Integer, nullable=True)
    cust_id = Column(Integer, nullable=True)
    legal_name = Column(String(255), nullable=True)
    price_grp_cd = Column(String(255), nullable=True)
    auth_description = Column(String(255), nullable=True)
    billing_block_cd = Column(String(255), nullable=True)
    order_block_cd = Column(String(255), nullable=True)
    delivery_block_cd = Column(String(255), nullable=True)
    posting_block_cd = Column(String(255), nullable=True)
    sales_block_cd = Column(String(255), nullable=True)
    marked_for_delete_ind = Column(String(255), nullable=True)
    acct_status_cd = Column(String(255), nullable=True)

def create_table():
    Base.metadata.create_all(engine)


def drop_table():
    Base.metadata.drop_all(engine)


def csvdataStore():
    drop_table()
    create_table()
    csv_file = r'../gmacc.csv'
    data = readData(csv_file)
    DBSession = sessionmaker(bind=engine)
    session = DBSession()
    try:
        for i in data:
            ed_user = CsvTable(
                sales_organisation_cd=i[0],
                apple_id=i[1],
                cust_id=i[2],
                legal_name=i[3].replace('"', ''),
                price_grp_cd=i[4],
                auth_description=i[5],
                billing_block_cd=i[6],
                order_block_cd=i[7],
                delivery_block_cd=i[8],
                posting_block_cd=i[9],
                sales_block_cd=i[10],
                marked_for_delete_ind=i[11],
                acct_status_cd=i[12]
            )
            session.add(ed_user)
        session.commit()
    except:
        session.rollback()
    finally:
        session.close()


if __name__ == '__main__':
    csvdataStore()
