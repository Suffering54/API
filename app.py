from flask import Flask, render_template, url_for, request

from models.user import User



app = Flask(__name__)  # '   main   '



@app.route('/')

def hello_method():

    return render_template('login.html')



@app.route('/login')

def login_user():

    email = request.form['email']

    password = request.form['password']



    if User.login_valid(email, password):

        #User.login(email)

        pass



    return render_template('profile.html')



if __name__ == '__main__':

    app.debug = True

    app.run(port=4995)
