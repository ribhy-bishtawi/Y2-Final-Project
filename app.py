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
		if request.method=="get":
			return render_template("register.html")
		else:
			form = request.form
			firstname = form["firstname"]
			lastname = form["lastname"]
			email = form["email"]
			password = form["password"]
			hometown = form["hometown"]
			website = form["website"]
			signupTable = db["signup"]
			entry = { "lastname":lastname, "email": email, "firstname": firstname, password:"password",hometown:"hometown",website:"website"}
			if len(list(signupTable.find(email=email)))==0:
				signupTable.insert(entry)
				return render_template("login.html", email=email, firstname=firstname,lastname=lastname, password=password, hometown=hometown,website=website)
			else:
				return "user already"



# TODO: route to /list

# TODO: route to /feed

# @app.route('/login' ,methods=['POST',"GET"])
# def login():
#         form = request.form
#         password = form["password-l"]
#         email = form["email-l"]
#         loginTable = db["login-n"]
#         entry = {"password": password, "email": email}
#         loginTable.insert(entry)
#         print list(loginTable.all())
#         return render_template("register.html" , email=email ,password=password)
#
#
#
#
# @app.route("/loginn")
# def register():
#     return render_template("register.html")
# # TODO: route to /error

if __name__ == '__main__':
	app.run(port=3000)