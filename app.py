from flask import Flask, render_template, request, redirect, url_for
import dataset

app = Flask(__name__)
db=dataset.connect("postgres://xsablmlvdcwygk:304f665b117ed37f455b90d9ec7ea4235c2ea5a088b24fb094114343473c3ebb@ec2-54-235-119-27.compute-1.amazonaws.com:5432/d7489ilia0g0mf")

@app.route('/')
@app.route('/home')
def homepage():
	return render_template('home.html')

# TODO: route to /list

# TODO: route to /feed

@app.route('/login' ,methods=['POST',"GET"])
def login():
    form = request.form
    password = form["password-l"]
    email = form["email-l"]
    loginTable = db["login-n"]
    entry = {"password": password, "email": email}
    loginTable.insert(entry)
    print list(loginTable.all())
    return render_template("register.html" , email=email ,password=password)


    if loginTable.find(email='email'):
        print "already in use"


@app.route("/register")
def register():
    return render_template("register.html")
# TODO: route to /error

if __name__ == "__main__":
    app.run(port=3000)











