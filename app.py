from flask import Flask, session, redirect, url_for, escape, request, render_template
import dataset
import time

app = Flask(__name__)
app.secret_key = 'A0Zr98j/3yX R~XHH!jmN]LWX/,?RT'
db=dataset.connect("postgres://xsablmlvdcwygk:304f665b117ed37f455b90d9ec7ea4235c2ea5a088b24fb094114343473c3ebb@ec2-54-235-119-27.compute-1.amazonaws.com:5432/d7489ilia0g0mf")

# def reset_db():
# 	posts=db["newfeeds"]
# 	posts.drop()
# reset_db()
# print crash()

@app.route('/')
@app.route('/home')

def homepage():  
	if 'username' in session :
		return render_template("home.html")
	else:    
		return render_template("home.html")
# +'Logged in as %s' %(session['username'])

@app.route('/register', methods=['GET', 'POST'])
def registerpage():
	return render_template("register.html")


@app.route('/list', methods=['GET', 'POST'])
def listpage():
	if 'username' in session :
		usersall=db["signup"]
		users=list(usersall.all())
		return render_template("list.html", users=users)

	else:
		
		return render_template("login.html")


@app.route('/feed', methods=['get', 'post'])
def akakakakaka():
	if 'username' in session :
		newfeed=db["newfeeds"]
		feedb=list(newfeed.all())[::-1] 
		return render_template("feed.html" ,feedb=feedb)
	else:
		return render_template("login.html")

@app.route('/newfeeds', methods=['get', 'post'])
def feedpage():   
	if 'username' in session:
		if request.method==['get']:
			newfeed=db['newfeeds']
			feedb= list(newfeed.all())[::-1]
			return render_template("feed.html",feedb=feedb)
		else:        
			form = request.form
			username=session['username']
			posts = form["post"]     
			newfeed=db["newfeeds"]
			time_string = time.strftime('%l:%M %p on %b %d, %Y')
			entry = { "post":posts,"username":username,"time_string":time_string}
			newfeed.insert(entry)   
			feedb=list(newfeed.all())[::-1] 
			return render_template("feed.html", feedb=feedb,username=username,posts=posts,time=time)
	else:
		return redirect("/login")




	
@app.route("/login", methods=['GET', 'POST'])
def log():
	return render_template("login.html")

@app.route('/logout', methods=['post', 'get'])
def logout():
	session.pop('username', None)
	return redirect("/login")


@app.route('/signup',  methods=['get','post'] )
def signup():

		if request.method=="get":
			return render_template("register.html")
		else:
			form = request.form
			firstname = form["firstname"]
			lastname = form["lastname"]
			username = form["username"]
			email = form["email"]
			password = form["password"]
			hometown = form["hometown"]
			website = form["website"]
			#male=form['male']
			gender = form["select"]
			print form
			signupTable = db["signup"]
			genderr = list(signupTable.all())
			entry = {"gender":gender , "username": username, "lastname":lastname, "email": email, "firstname": firstname, "password":password,"hometown":hometown,"website":website}
			if len(list(signupTable.find(username=username)))==0:
				session['username'] = request.form['username']
				signupTable.insert(entry)
				return render_template("login.html", gender=gender ,email=email, firstname=firstname,lastname=lastname, username=username, password=password, hometown=hometown,website=website,genderr=genderr)
			else:
				session['error'] =  True
				error = session['error']
				return render_template("register.html",error=error)
@app.route("/logi", methods=['GET', 'POST'])
def login():

		if request.method == "get":
			return render_template("login.html")
		else:
			form = request.form
			username = form["username"]
			password=form["password-l"]
			signupTable = db["signup"]
			# print list(signupTable.find(email="moh@mail.com"))
			if len(list(signupTable.find(username=username,password=password))) > 0 :
				session['username'] = request.form['username']
				return redirect("/list")

			else:
				session['error'] =  True
				error = session['error']
				return render_template("login.html",error = error)
if __name__ == '__main__':
	app.run(port=3000)
	# test1

