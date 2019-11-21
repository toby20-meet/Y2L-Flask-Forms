from flask import Flask, request, redirect, url_for, render_template, request
from flask import session as login_session
from databases import *


app = Flask(__name__)
app.secret_key = "MY_SUPER_SECRET_KEY"


##### Code here ######
@app.route('/')
def home():
	return render_template("home.html")

@app.route('/store')
def store():
	if request.method == 'POST':
		databases.Add_To_Cart(submition)
	product_names = allofthem()
	return render_template("store.html",pn = product_names)

@app.route('/about')
def about():
	return render_template('about.html')

@app.route('/cart/<String>')
def cart(String):
	Add_To_Cart(String)
	return render_template('cart.html')
#####################


if __name__ == '__main__':
    app.run(debug=True)