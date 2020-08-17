from sqlalchemy import Column, String, Integer
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


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