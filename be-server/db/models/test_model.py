from sqlalchemy import MetaData, Table, Column, Integer
from ...app import db

class Test_Table(db.Model):
    x = db.Column(db.Integer)
    y = db.Column(db.Integer)
