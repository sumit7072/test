from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app=Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"]="mysql+pymysql://root:12345@localhost/pydb"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS']=False
db=SQLAlchemy(app)


shopprod = db.Table('SHOP_PRODUCTS',
    db.Column('sid', db.Integer, db.ForeignKey('SHOP_INFO.id'), primary_key=True),
    db.Column('pid', db.Integer, db.ForeignKey('PRODUCT_INFO.id'), primary_key=True)
)

class Shop(db.Model):
    __tablename__="SHOP_INFO"
    id= db.Column("id",db.Integer(),primary_key=True)
    sname= db.Column("Shop_Name",db.String(60))
    sadr= db.Column("Shop_Adrs",db.String(60))
    sowner= db.Column("Shop_Owner",db.String(60),unique=True)
    product=db.relationship("Product",secondary=shopprod,lazy='subquery',backref=db.backref('shop',lazy=True))

class Product(db.Model):
    __tablename__="PRODUCT_INFO"
    id=db.Column("id",db.Integer(),primary_key=True)
    pname=db.Column("Prod_Name",db.String(60))
    pqty=db.Column("Prod_Quantity",db.Integer())


db.create_all()

