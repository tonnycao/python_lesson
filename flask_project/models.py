from flask_sqlalchemy import SQLAlchemy
from flask_login import UserMixin

db = SQLAlchemy()

class CsvTable(db.Model):
    __tablename__ = "csv_table"

    id = db.Column(db.Integer, primary_key=True)
    sales_organisation_cd = db.Column(db.Integer, nullable=True)
    apple_id = db.Column(db.Integer, nullable=True)
    cust_id = db.Column(db.Integer, nullable=True)
    legal_name = db.Column(db.String(255), nullable=True)
    price_grp_cd = db.Column(db.String(255), nullable=True)
    auth_description = db.Column(db.String(255), nullable=True)
    billing_block_cd = db.Column(db.String(255), nullable=True)
    order_block_cd = db.Column(db.String(255), nullable=True)
    delivery_block_cd = db.Column(db.String(255), nullable=True)
    posting_block_cd = db.Column(db.String(255), nullable=True)
    sales_block_cd = db.Column(db.String(255), nullable=True)
    marked_for_delete_ind = db.Column(db.String(255), nullable=True)
    acct_status_cd = db.Column(db.String(255), nullable=True)

    def __init__(self, sales_organisation_cd, apple_id, cust_id, legal_name,
                 price_grp_cd, auth_description, billing_block_cd, order_block_cd,
                 delivery_block_cd, posting_block_cd, sales_block_cd,
                 marked_for_delete_ind, acct_status_cd):
        self.sales_organisation_cd = sales_organisation_cd
        self.apple_id = apple_id
        self.cust_id = cust_id
        self.legal_name = legal_name
        self.price_grp_cd = price_grp_cd
        self.auth_description = auth_description
        self.billing_block_cd = billing_block_cd
        self.order_block_cd = order_block_cd
        self.delivery_block_cd = delivery_block_cd
        self.posting_block_cd = posting_block_cd
        self.sales_block_cd = sales_block_cd
        self.marked_for_delete_ind = marked_for_delete_ind
        self.acct_status_cd = acct_status_cd


class User(UserMixin, db.Model):
    __tablename__ = "user"
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(24), nullable=False)
    password = db.Column(db.String(24), nullable=False)

    def __init__(self, username, password):
        self.username = username
        self.password = password
