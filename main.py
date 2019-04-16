from flask import Flask, request, redirect, render_template
import cgi

app = Flask(__name__)

app.config['DEBUG'] = True      # displays runtime errors in the browser, too

@app.route("/welcome")
def welcome():
    user = request.args.get('username')
    return render_template('welcome.html', user = user)  

@app.route("/error", methods = ['POST'])
def signup():
    username = request.form['username']
    password = request.form['password']
    verify = request.form['verify']
    email = request.form['email']

    errorcount = 0
    error = ""
    error1 = ""
    error2 = ""
    error3 = ""
    
    if (not username) or (username.strip() == "") or " " in username or len(username) < 3 or len(username) > 20:
        error = "That's not a valid username"
        errorcount += 1
        username = ""
        
    if (not password) or (password.strip() == "") or " " in password or len(password) < 3 or len(password) > 20:
        error1 = "That's not a valid password"
        errorcount += 1
    
    if (not verify) or (verify.strip() == "") or verify != password:
        error2 = "That's not a valid verify password"
        errorcount += 1

    if len(email) == 0:
        email = ""

    elif " " in email or len(email) < 3 or len(email) > 20 or email.count("@") is not 1 or email.count(".") is not 1:
        error3 = "That's not a valid email"
        errorcount += 1
        email = ""


    if errorcount is not 0:
        return render_template('index.html', email = email, username = username ,error = error, error1 = error1, error2=error2, error3=error3 )
    
    else:
        return redirect("/welcome?username={0}".format(username) )

      

@app.route("/")
def index():  
    return render_template('index.html' )

app.run()
