from sqlalchemy import Column, String, Integer, DECIMAL
from sqlalchemy.ext.declarative import declarative_base
Base = declarative_base()


class Zf070(Base):

    __tablename__ = 'zf070'

    id = Column(Integer, primary_key=True)
    Invoice = Column(String(255), nullable=True)
    no = Column(String(255), nullable=True)
    company = Column(String(255), nullable=True)
    code = Column(String(255), nullable=True)
    tax_amt_in_lc = Column(DECIMAL(19, 2), nullable=True)
    sales_order = Column(String(255), nullable=True)
    tax_code = Column(String(255), nullable=True)
    item = Column(Integer, nullable=True)
    year = Column(Integer, nullable=True)
    period = Column(Integer, nullable=True)
    posting_date = Column(String(255), nullable=True)
    doc_created = Column(String(255), nullable=True)
    payment_date = Column(String(255), nullable=True)
    billing_type = Column(String(255), nullable=True)
    invoice_date = Column(String(255), nullable=True)
    billed_quantity = Column(String(255), nullable=True)
    tax_base_amt_in_lctax = Column(DECIMAL(19, 2), nullable=True)
    amt_in_lccurrency = Column(DECIMAL(19, 2), nullable=True)
    tax_base_amt_in_gctax = Column(DECIMAL(19, 2), nullable=True)
    amt_in_gc_lcur2 = Column(DECIMAL(19, 2), nullable=True)
    store = Column(String(255), nullable=True)
    store_name1 = Column(String(255), nullable=True)
    store_name2 = Column(String(255), nullable=True)
    postal_code = Column(String(255), nullable=True)
    store_address_street = Column(String(255), nullable=True)
    trs_key = Column(String(255), nullable=True)
    checking_in_lc = Column(DECIMAL(19, 2), nullable=True)
    checking_in_gc = Column(DECIMAL(19, 2), nullable=True)
    tax_gross_amt_in_doc = Column(DECIMAL(19, 2), nullable=True)
    curr = Column(String(255), nullable=True)
    tax_rate = Column(DECIMAL(19, 2), nullable=True)
    gl_account = Column(String(255), nullable=True)
    material = Column(String(255), nullable=True)
    material_description = Column(String(255), nullable=True)
    material_group = Column(String(255), nullable=True)
    material_group_description = Column(String(255), nullable=True)
    product_hierarchy = Column(String(255), nullable=True)
    product_hierarchy_description = Column(String(255), nullable=True)

