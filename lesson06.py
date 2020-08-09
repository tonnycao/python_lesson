from xlrd import open_workbook
import csv

def readData(file_path):
    if file_path.endswith("csv"):
        with open(file_path,'r') as f:
            reader = csv.reader(f)
            list = []
            for i in reader:
                list.append(i)
            list.pop(0)
            return list
    else:
        data=open_workbook(file_path,encoding_override='utf-8')
        table =data.sheets()[0]
        rows=table.nrows
        cols=table.ncols
        list = []
        for i in range(1,rows):
            row_data=table.row_values(i)
            list.append(row_data)
        return list


import pymysql
from sqlalchemy import Column, String, create_engine, Float, MetaData, Table, Integer
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

engine = create_engine('mysql+pymysql://root:P4ssword@localhost:3306/QA?charset=utf8', pool_recycle=10000)
Base = declarative_base()
metadata = MetaData(engine)

#创建表格，初始化数据库
xlsx_table = Table('xlsx_table', metadata,
    Column('id', Integer, primary_key=True, autoincrement=True),
    Column('idd', String(20)),
    Column('write_off_tax_base', Float),
    Column('write_off_tax', Float),
    Column('red_font_fp_tax_base', Float),
    Column('red_font_fp_tax', Float),
    Column('p2p_non_claimable_tax_base', Float),
    Column('p2p_non_claimable_tax', Float),
    Column('inventory_adj_tax_base', Float),
    Column('inventory_adj_tax', Float),
    Column('other_tax_base', Float),
    Column('other_tax', Float),
    Column('total_tax_base', Float),
    Column('total_tax', Float),
                   )

xls_table = Table('xls_table', metadata,
    Column('id', Integer, primary_key=True, autoincrement=True),
    Column('idd', String(20)),
    Column('write_off_tax_base', Float),
    Column('write_off_tax', Float),
    Column('red_font_fp_tax_base', Float),
    Column('red_font_fp_tax', Float),
    Column('p2p_non_claimable_tax_base', Float),
    Column('p2p_non_claimable_tax', Float),
    Column('inventory_adj_tax_base', Float),
    Column('inventory_adj_tax', Float),
    Column('other_tax_base', Float),
    Column('other_tax', Float),
    Column('total_tax_base', Float),
    Column('total_tax', Float),
                   )

csv_table = Table('csv_table', metadata,
    Column('id', Integer, primary_key=True, autoincrement=True),
    Column('sales_organisation_cd', String(100)),
    Column('apple_id', String(100)),
    Column('cust_id', String(100)),
    Column('legal_name', String(100)),
    Column('price_grp_cd', String(100)),
    Column('auth_description', String(100)),
    Column('billing_block_cd', String(100)),
    Column('order_block_cd', String(100)),
    Column('delivery_block_cd', String(100)),
    Column('posting_block_cd', String(100)),
    Column('sales_block_cd', String(100)),
    Column('marked_for_delete_ind', String(100)),
    Column('acct_status_cd', String(100))
)


#创建数据表，如果数据表存在则忽视！！！
metadata.create_all(engine)


class xlsxdataStore(Base):
    __tablename__ = "xlsx_table"

    id = Column(Integer, primary_key=True, autoincrement=True)
    idd = Column(String(20))
    write_off_tax_base = Column(Float)
    write_off_tax = Column(Float)
    red_font_fp_tax_base = Column(Float)
    red_font_fp_tax = Column(Float)
    p2p_non_claimable_tax_base = Column(Float)
    p2p_non_claimable_tax = Column(Float)
    inventory_adj_tax_base = Column(Float)
    inventory_adj_tax = Column(Float)
    other_tax_base = Column(Float)
    other_tax = Column(Float)
    total_tax_base = Column(Float)
    total_tax = Column(Float)


    def insert_row(self, list):

        # 创建DBSession类型
        DBSession = sessionmaker(bind=engine)
        # 创建session对象
        session = DBSession()
        # 写入数据
        try:
            for i in range(len(list)):
                # session.execute('INSERT INTO xlsx_table (id, write_off_tax_base, write_off_tax) '
                #                 'VALUES (:aa, :bb, :cc)',
                #          ({'aa': list[i][0], 'bb': list[i][1], 'cc': list[i][2]}))
                session.execute('INSERT INTO xlsx_table (idd, write_off_tax_base, write_off_tax, red_font_fp_tax_base, red_font_fp_tax, p2p_non_claimable_tax_base, p2p_non_claimable_tax, inventory_adj_tax_base, inventory_adj_tax, other_tax_base, other_tax, total_tax_base, total_tax) '
                                'VALUES (:aa, :bb, :cc, :dd, :ee, :ff, :gg, :hh, :ii, :jj, :kk, :ll, :mm)',
                         ({'aa': list[i][0], 'bb': list[i][1], 'cc': list[i][2], 'dd': list[i][3], 'ee': list[i][4], 'ff': list[i][5], 'gg': list[i][6], 'hh': list[i][7], 'ii': list[i][8], 'jj': list[i][9], 'kk': list[i][10], 'll': list[i][11], 'mm': list[i][12]}))
                session.commit()
        except:
            session.rollback()
        finally:
            session.close()


class xlsdataStore(Base):
    __tablename__ = "xls_table"

    id = Column(Integer, primary_key=True, autoincrement=True)
    idd = Column(String(20))
    write_off_tax_base = Column(Float)
    write_off_tax = Column(Float)
    red_font_fp_tax_base = Column(Float)
    red_font_fp_tax = Column(Float)
    p2p_non_claimable_tax_base = Column(Float)
    p2p_non_claimable_tax = Column(Float)
    inventory_adj_tax_base = Column(Float)
    inventory_adj_tax = Column(Float)
    other_tax_base = Column(Float)
    other_tax = Column(Float)
    total_tax_base = Column(Float)
    total_tax = Column(Float)


    def insert_row(self, list):

        # 创建DBSession类型
        DBSession = sessionmaker(bind=engine)
        # 创建session对象
        session = DBSession()
        # 写入数据
        try:
            for i in range(len(list)):
                session.execute('INSERT INTO xls_table (idd, write_off_tax_base, write_off_tax) '
                                'VALUES (:aa, :bb, :cc)',
                         ({'aa': list[i][0], 'bb': list[i][1], 'cc': list[i][2]}))
                session.commit()
        except:
            session.rollback()
        finally:
            session.close()


class csvdataStore(Base):
    __tablename__ = "csv_table"

    id = Column(Integer, primary_key=True, autoincrement=True)
    sales_organisation_cd = Column(String(100))
    apple_id = Column(String(100))
    cust_id = Column(String(100))
    legal_name = Column(String(100))
    price_grp_cd = Column(String(100))
    auth_description = Column(String(100))
    billing_block_cd = Column(String(100))
    order_block_cd = Column(String(100))
    delivery_block_cd = Column(String(100))
    posting_block_cd = Column(String(100))
    sales_block_cd = Column(String(100))
    marked_for_delete_ind = Column(String(100))
    acct_status_cd = Column(String(100))


    def insert_row(self, list):

        # 创建DBSession类型
        DBSession = sessionmaker(bind=engine)
        # 创建session对象
        session = DBSession()
        # 写入数据
        try:
            for i in range(len(list)):
                session.execute('INSERT INTO csv_table (sales_organisation_cd, apple_id, cust_id, legal_name, price_grp_cd, auth_description, billing_block_cd, order_block_cd, delivery_block_cd, posting_block_cd, sales_block_cd, marked_for_delete_ind, acct_status_cd) '
                                'VALUES (:aa, :bb, :cc, :dd, :ee, :ff, :gg, :hh, :ii, :jj, :kk, :ll, :mm)',
                         ({'aa': list[i][0], 'bb': list[i][1], 'cc': list[i][2], 'dd': list[i][3], 'ee': list[i][4], 'ff': list[i][5], 'gg': list[i][6], 'hh': list[i][7], 'ii': list[i][8], 'jj': list[i][9], 'kk': list[i][10], 'll': list[i][11], 'mm': list[i][12]}))
                session.commit()
        except:
            session.rollback()
        finally:
            session.close()


if __name__ == '__main__':
    xlsx_file = r'/Users/jimmy/downloads/D186 VAT Transfer out Summary 202006.xlsx'
    xlsxdataStore().insert_row(readData(xlsx_file))
    xls_file = r'/Users/jimmy/downloads/D186 VAT Transfer out Summary 202006.xls'
    xlsdataStore().insert_row(readData(xls_file))
    csv_file = r'/Users/jimmy/downloads/bmt_pp_gmacc_May20_CommaDelimited.csv'
    csvdataStore().insert_row(readData(csv_file))