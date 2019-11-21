from model import *


from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


engine = create_engine('sqlite:///database.db')
Base.metadata.create_all(engine)
DBSession = sessionmaker(bind=engine)
session = DBSession()

def addProduct(product_name,product_price,picture_link,product_description):
	new_product = Product(name = product_name,price = product_price,picture_link=picture_link,description=product_description)
	session.add(new_product)
	session.commit()

def editProduct(product_id,change_var,new_vlaue):
	product_object = session.query(Product).filter_by(Id = product_id)
	product_object.change_var = new_vlaue
	session.commit()

def delProduct(product_id):
	product_object = session.query(Product).filter_by(Id = product_id)
	product_object.delete()
	session.commit()

def allofthem():
	return session.query(Product).all()

def bringProduct(product_id):
	return session.query(Product).filter_by(Id = product_id)

def Add_To_Cart(productID):
	newly_added = Cart(productID = productID)
	session.add(newly_added)
	session.commit()
