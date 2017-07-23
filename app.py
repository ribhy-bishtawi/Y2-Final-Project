from flask import Flask, render_template, request, redirect, url_for
import dataset

app = Flask(__name__)

db=dataset.connect("postgres://xsablmlvdcwygk:304f665b117ed37f455b90d9ec7ea4235c2ea5a088b24fb094114343473c3ebb@ec2-54-235-119-27.compute-1.amazonaws.com:5432/d7489ilia0g0mf")

@app.route('/')
@app.route('/home')
def homepage():
	return render_template('/home.html')


@app.route('/register', methods=['GET', 'POST'])
def registerpage():
	return render_template("register.html")


@app.route('/signup',  methods=["get","post"] )
def signup():
	if request.method =="GET":
		return render_template("login.html")
	else:
		form = request.form 
		firstname = form["firstname"]
		lastname = form["lastname"]
		email = form["email"]
		password = form["password"]
		hometown = form["hometown"]
		website = form["website"]
		signupTable = db["signup"]
		entry = { "name":name, "email": email, "message": message }
		signupTable.insert(entry)
		print list(signupTable.all())
		return render_template("login.html", firstname=firstname, lastname=lastname, email=email , password=password, hometown=hometown, website=website )

# TODO: route to /list

# TODO: route to /feed

# TODO: route to /register

# TODO: route to /error

if __name__ == '__main__':
	app.run(port=3000)