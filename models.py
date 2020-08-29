from app import db


class Employee(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(128), unique=True, nullable=False)
    email = db.Column(db.String(128), unique=True, nullable=False)
    created_time = db.Column(db.DateTime, default=db.func.now())


class Company(db.Model):
    cid = db.Column(db.Integer, primary_key=True)
    cname = db.Column(db.String(128), unique=True, nullable=False)
    clocation = db.Column(db.String(128), unique=False, nullable=False)
    created_time = db.Column(db.DateTime, default=db.func.now())


class City(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(128))
    population = db.Column(db.Integer, default=0)
    created_time = db.Column(db.DateTime, default=db.func.now())


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)  # primary keys are required by SQLAlchemy
    email = db.Column(db.String(100), unique=True)
    password = db.Column(db.String(100))
    name = db.Column(db.String(1000))