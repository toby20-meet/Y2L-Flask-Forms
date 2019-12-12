from model import *


from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

def run_therm():
	engine = create_engine('sqlite:///database.db')
	Base.metadata.create_all(engine)
	DBSession = sessionmaker(bind=engine)
	session = DBSession()
	return session

def addProduct(product_name,product_price,picture_link,product_description):
	session = run_therm()
	new_product = Product(name = product_name,price = product_price,picture_link=picture_link,description=product_description)
	session.add(new_product)
	session.commit()

def editProduct(product_id,change_var,new_vlaue):
	session = run_therm()
	product_object = session.query(Product).filter_by(Id = product_id).first()
	setattr(product_object,change_var,new_vlaue)
	session.commit()

def delProduct(product_id):
	session = run_therm()
	product_object = session.query(Product).filter_by(Id = product_id)
	product_object.delete()
	session.commit()

def allofthem():
	session = run_therm()
	return session.query(Product).all()

def bringProduct(product_id):
	session = run_therm()
	return session.query(Product).filter_by(Id = product_id).first()

def Add_To_Cart(productID):
	session = run_therm()
	newly_added = Cart(productID = productID)
	session.add(newly_added)
	session.commit()
def all_in_cart():
	session = run_therm()
	return session.query(Cart).all()

print allofthem()[1].Id
editProduct(17,'price',0.00)
print allofthem()[1].price

