from flask import Flask, session, redirect, url_for, escape, request, render_template
import dataset
app = Flask(__name__)
app.secret_key = 'A0Zr98j/3yX R~XHH!jmN]LWX/,?RT'

db=dataset.connect("postgres://xsablmlvdcwygk:304f665b117ed37f455b90d9ec7ea4235c2ea5a088b24fb094114343473c3ebb@ec2-54-235-119-27.compute-1.amazonaws.com:5432/d7489ilia0g0mf")

@app.route('/')
@app.route('/home.html')
def homepage():

	if 'email' in session :
		return render_template("home.html")+'Logged in as %s' %(session['email'])
	else:
		return render_template("home.html")


@app.route('/register', methods=['GET', 'POST'])
def registerpage():
	return render_template("reg.html")


@app.route('/signup',  methods=['get','post'] )
def signup():
		if request.method=="get":
			return render_template("reg.html")
		else:
			form = request.form
			firstname = form["firstname"]
			lastname = form["lastname"]
			email = form["email"]
			password = form["password"]
			hometown = form["hometown"]
			website = form["website"]

			signupTable = db["signup"]
			entry = { "lastname":lastname, "email": email, "firstname": firstname, "password":password,"hometown":hometown,"website":website}
			if len(list(signupTable.find(email=email)))==0:
				signupTable.insert(entry)
				return render_template("reg.html", email=email, firstname=firstname,lastname=lastname, password=password, hometown=hometown,website=website)
			else:
				return "user already"

@app.route("/login", methods=['GET', 'POST'])
def login():
		if request.method == "get":
			return render_template("login.html")
		else:
			form = request.form
			email = form["email-l"]
			password=form["password-l"]
			signupTable = db["signup"]
			# print list(signupTable.find(email="moh@mail.com"))
			entry = {"email": email,"password":password}
			if len(list(signupTable.find(email=email,password=password))) > 0 :
				session['email'] = request.form['email-l']
				signupTable.insert(entry)
				return redirect("/home.html")

			else:
				return"false"

@app.route("/login.html", methods=['GET', 'POST'])
def loginn():
	return  render_template("login.html")
@app.route('/reg.html')
def reg():
	return  render_template("reg.html")
@app.route('/logout', methods=['post', 'get'])
def logout():
	session.pop('email', None)
	return redirect("/login.html")




# TODO: route to /list

# TODO: route to /feed


# # TODO: route to /error

if __name__ == '__main__':
	app.run(port=3000)