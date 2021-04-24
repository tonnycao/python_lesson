import csv
import pprint
from sqlalchemy import create_engine

from sqlalchemy import Column, String, Integer,create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

engine = create_engine('mysql+pymysql://root:@localhost:3306/db_example?charset=utf8mb4', pool_recycle=3600)
Base = declarative_base()


def create_table():
    Base.metadata.create_all(engine)


def drop_table():
    Base.metadata.drop_all(engine)


def parse_gmacc():
    drop_table()
    create_table()
    # parse_file()


def parse_file():
    i = 0
    data = []
    with open('gmacc.csv', newline='') as f:
        reader = csv.reader(f, delimiter=',')

        for row in reader:

            if i > 0:
                data.append(row)
            i += 1
    return data


class Gmacc(Base):
     __tablename__ = 'gmacc'

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

def main():
    drop_table()
    create_table()
    data = parse_file()
    DBSession = sessionmaker(bind=engine)
    session = DBSession()
    # 创建新User对象:
    for i in data:
        ed_user = Gmacc(
            sales_organisation_cd=i[0],
            apple_id=i[1],
            cust_id=i[2],
            legal_name = i[3].replace('"',''),
            price_grp_cd = i[4],
            auth_description =i[5],
            billing_block_cd = i[6],
            order_block_cd = i[7],
            delivery_block_cd =i[8],
            posting_block_cd = i[9],
            sales_block_cd = i[10],
            marked_for_delete_ind = i[11],
            acct_status_cd=i[12]
        )
        session.add(ed_user)
    session.commit()
    # pprint.pprint(data)


if __name__ == '__main__':
    create_table()
