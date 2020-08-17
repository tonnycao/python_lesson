from xlrd import open_workbook
import csv

def readData(file_path):
    data = []
    i = 0
    with open(file_path, mode='r', encoding='utf-8') as f:
        lines = f.readlines()
        i = 0
        for line in lines:
            item = (line.split("\t"))
            if i>0:
                data.append(item)
            i +=1
    return data


import pymysql
from sqlalchemy import Column, String, create_engine, Float, MetaData, Table, Integer, DECIMAL
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

engine = create_engine('mysql+pymysql://root:P4ssword@localhost:3306/QA?charset=utf8', pool_recycle=10000)
Base = declarative_base()
metadata = MetaData(engine)

class xlsTable(Base):
    __tablename__ = 'xls_table'

    id = Column(Integer, primary_key=True)
    cocd = Column(Integer, nullable=True)
    tx = Column(String(255), nullable=True)
    pos_receipt = Column(String(255), nullable=True)
    item = Column(String(255), nullable=True)
    year = Column(String(255), nullable=True)
    period = Column(String(255), nullable=True)
    posting_date = Column(String(255), nullable=True)
    document_created = Column(String(255), nullable=True)
    paymt_date = Column(String(255), nullable=True)
    billt = Column(String(255), nullable=True)
    invoice_id = Column(String(255), nullable=True)
    invoice_no = Column(String(255), nullable=True)
    invoice_date = Column(String(255), nullable=True)
    tax_base_amt_in_lc = Column(DECIMAL(19, 2), nullable=True)
    tax_amt_in_lc = Column(DECIMAL(19, 2), nullable=True)
    crcy= Column(String(255), nullable=True)
    tax_base_amt_in_gc = Column(DECIMAL(19, 2), nullable=True)
    tax_amt_in_gc = Column(DECIMAL(19, 2), nullable=True)
    lcur2= Column(String(255), nullable=True)
    store= Column(String(255), nullable=True)
    store_name= Column(String(255), nullable=True)
    postal_code= Column(String(255), nullable=True)
    store_address= Column(String(255), nullable=True)
    trs_key= Column(String(255), nullable=True)
    checking_in_lc= Column(DECIMAL(19, 2), nullable=True)
    checking_in_gc= Column(DECIMAL(19, 2), nullable=True)
    tax_Gross_amt_in_doc_curr= Column(DECIMAL(19, 2), nullable=True)
    created_on= Column(String(255), nullable=True)
    amount= Column(DECIMAL(19, 2), nullable=True)
    article_no= Column(String(255), nullable=True)
    material_description= Column(String(255), nullable=True)
    billed_qty= Column(String(255), nullable=True)
    gl_acct= Column(String(255), nullable=True)
    posting_status= Column(String(255), nullable=True)
    mdse_catgry_desc= Column(String(255), nullable=True)
    prod_class= Column(String(255), nullable=True)
    prod_class_desc= Column(String(255), nullable=True)
    fiscal_code= Column(String(255), nullable=True)
    customer_ho_branch_no = Column(String(255), nullable=True)

def create_table():
    Base.metadata.create_all(engine)


def drop_table():
    Base.metadata.drop_all(engine)


def xlsdataStore():
    drop_table()
    create_table()
    xls_file = r'/Users/jimmy/downloads/D186.xls'
    data = readData(xls_file)
    DBSession = sessionmaker(bind=engine)
    session = DBSession()
    try:
        for i in data:
            record = xlsTable(
                cocd=i[0].strip(),
                tx = i[1].strip(),
                pos_receipt = i[2].strip(),
                item = i[3].strip(),
                year = i[4].strip(),
                period =i[5].strip(),
                posting_date = i[6].strip(),
                document_created = i[7].strip(),
                paymt_date = i[8].strip(),
                billt = i[9].strip(),
                invoice_id = i[10].strip(),
                invoice_no = i[11].strip(),
                invoice_date = i[12].strip(),
                tax_base_amt_in_lc = i[13].replace(',', ''),
                tax_amt_in_lc = i[14].replace(',', ''),
                crcy = i[15].strip(),
                tax_base_amt_in_gc = i[16].replace(',', ''),
                tax_amt_in_gc = i[17].replace(',', ''),
                lcur2 = i[18].strip(),
                store = i[19].strip(),
                store_name = i[20].strip(),
                postal_code = i[21].strip(),
                store_address = i[22].strip(),
                trs_key = i[23].strip(),
                checking_in_lc = i[24].replace(',', ''),
                checking_in_gc = i[25].replace(',', ''),
                tax_Gross_amt_in_doc_curr = i[26].replace(',', ''),
                created_on = i[27].strip(),
                amount = i[28].replace(',', ''),
                article_no = i[29].strip(),
                material_description = i[30].strip(),
                billed_qty = i[31].strip(),
                gl_acct = i[32].strip(),
                posting_status = i[33].strip(),
                mdse_catgry_desc = i[34].strip(),
                prod_class = i[35].strip(),
                prod_class_desc = i[36].strip(),
                fiscal_code = i[37].strip(),
                customer_ho_branch_no = i[38].strip(),
            )
            session.add(record)
        session.commit()
    except:
        session.rollback()
    finally:
        session.close()


if __name__ == '__main__':
    xlsdataStore()
