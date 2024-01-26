from flask import Flask, render_template, request , session , redirect, url_for ,jsonify
import pickle
import json
import authentication

import filemanagement
app = Flask(__name__)

app.secret_key = 'your_secret_key' 
succsscred=False
@app.route('/signup')
def signup():
    return render_template('signup.html')

@app.route('/submit', methods=['POST'])
def submit():
    username = request.form.get('username')
    password1 = request.form.get('password1')
    password2 = request.form.get('password2')
    
    if authentication.is_registered(username):
        return render_template("usernameexist.html")
    else:
        authentication.register(username, password1)
        
        session['username'] = username
        session['password'] = password1
        
        filemanagement.create_file(username)
        
        
        
        return render_template("registered.html")

@app.route('/login')
def login():
    return render_template("login.html")
    
@app.route('/loginauth', methods=["POST"])
def loginauth():
    if 'username' in session and 'password' in session:
        return render_template("home.html", name=session['username'])
    
    username = request.form.get('username')
    password = request.form.get('password')
    
    if authentication.user_good(username, password):
        session['username'] = username
        session['password'] = password
        
        succsscred = True
        
        return redirect(url_for('home_page'))
    
    return render_template("login.html" , msg = "wrong credentials")

    
@app.route('/')
def home_page():
    if ('username' in session and 'password' in session ) or succsscred:


        username = session["username"]
        file_path = f"userfile/{username}.json"
        with open(file_path, 'r') as file:
            userdata = json.load(file)
            
        # print(userdata)
        return render_template("home.html", name=session['username'] , data = (userdata))
    else:
        return redirect(url_for('login'))



@app.route('/print_data', methods=['POST'])
def print_data():
    data = request.json
    
    data = {"tasks":data}
    username = session["username"]
    file_path = f"userfile/{username}.json"
    with open(file_path, 'w') as file:
        json.dump(data, file)
    return 'Data updated successfully'    
    



@app.route('/logout')

def logout():
    
    if ('username' in session or 'password' in session ):
        session.pop("username")
        session.pop("password")
        succsscred = False

        return redirect(url_for('login'))
    return redirect(url_for('login'))

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)

