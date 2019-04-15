from flask import Flask, request, redirect, render_template
import cgi

app = Flask(__name__)

app.config['DEBUG'] = True      # displays runtime errors in the browser, too

@app.route("/welcome", methods = ['POST'])
def signup():
    username = request.form['username']
    password = request.form['password']
    verify = request.form['verify']
    email = request.form['email']

    errorpath = "/?error="
    errorcount = 0

    if (not username) or (username.strip() == "") or " " in username or len(username) < 3 or len(username) > 20:
        error = "That's not a valid username"
        errorcount += 1
        errorpath = errorpath + error

    elif (not password) or (password.strip() == "") or " " in password or len(password) < 3 or len(password) > 20:
        error1 = "That's not a valid password"
        errorcount += 1
        errorpath = errorpath + error1

    elif (not verify) or (verify.strip() == ""):
        error2 = "That's not a valid verify password"
        errorcount += 1
        errorpath = errorpath + error2

    elif " " in email or len(email) < 3 or len(email) > 20:
        error3 = "That's not a valid email"
        errorcount += 1
        errorpath = errorpath + error3

    elif errorcount > 0:
        return redirect(errorpath)
    
    username_escaped = cgi.escape(username, quote=True)

    return render_template('welcome.html', user = username_escaped)

@app.route("/")
def index():
    encoded_error = request.args.get("error")
    return render_template('index.html', error=encoded_error and cgi.escape(encoded_error, quote=True))

app.run()
