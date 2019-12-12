from flask import Flask, request, redirect, url_for, render_template, request
from flask import session as login_session
from databases import *


app = Flask(__name__)
app.config['SECRET_KEY'] = 'super-secret-key'
app.secret_key = "MY_SUPER_SECRET_KEY"


##### Code here ######
@app.route('/')
def home():
	return render_template("home.html")

@app.route('/store', methods = ['GET','POST'])
def store():
	if request.method == 'POST':
		submition = int(request.form['product_id'])
		Add_To_Cart(submition)
	product_names = allofthem()
	return render_template("store.html",pn = product_names)

@app.route('/about')
def about():
	return render_template('about.html')

@app.route('/cart')
def cart():
	products_added = all_in_cart()
	sending = []
	for i in products_added:
		sending.append(bringProduct(i.productID))
	return render_template('cart.html',pd = sending)

@app.route('/portal', methods = ['POST','GET'])
def portal():
	if request.method == 'POST':
		change_type = request.form['types']
		new_value = request.form['new_value']
		product_id = request.form['product_id']
		editProduct(product_id,change_type,new_value)
	product_names = allofthem()
	return render_template('portal.html',pn = product_names)

@app.route('/login', methods = ['POST','GET'])
def login():
	usernames = ['Toby']
	passwords = ['20']
	if request.method == 'POST':
		entered_name = request.form['username']
		entered_password = request.form['password']
		if(entered_name in usernames and entered_password in passwords):
			return redirect(url_for("portal"))

	return render_template('login.html')

#####################


if __name__ == '__main__':
    app.run(debug=True)