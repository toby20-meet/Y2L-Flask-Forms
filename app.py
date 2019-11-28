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
		databases.Add_To_Cart(submition)
	product_names = allofthem()
	return render_template("store.html",pn = product_names)

@app.route('/about')
def about():
	return render_template('about.html')

@app.route('/cart')
def cart(String):
	products_added = all_in_cart()
	return render_template('cart.html',pd = products_added)
#####################


if __name__ == '__main__':
    app.run(debug=True)