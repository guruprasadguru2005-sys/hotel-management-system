from sqlite3 import IntegrityError

from flask import Flask, redirect, render_template, request, url_for

import sqlite3

app = Flask(__name__)

#Login page
@app.route("/")
def login():
    return render_template("hotel.html")

#check Login
@app.route("/login", methods=["POST"])
def check_login():
    username = request.form["username"]
    password = request.form["password"]
    
    conn = sqlite3.connect("hotel.db")
    cursor = conn.cursor()
    cursor.execute(
        "SELECT * FROM users WHERE username=? AND password=?",
        (username, password)
    )
    
    user = cursor.fetchone()
    
    conn.close()
    if user:
        return redirect(url_for("homepage"))
    else:
        return render_template("hotel.html", show_modal=True)

#Signup page 
@app.route("/signuppage")
def signuppage():
    return render_template("hotel-signup-page.html")
#Save sign up 
@app.route("/signup", methods=["POST"])
def signup():
    username = request.form["username"]
    password = request.form["password"]
    confirm_password = request.form["confirm_password"]
    
    if password != confirm_password:
        return render_template("hotel-signup-page.html", password_error=True
                               )
    
    conn = sqlite3.connect("hotel.db")
    cursor = conn.cursor()
    
    try:
        cursor.execute(
            "INSERT INTO users(username, password) VALUES(?, ?)",
            (username, password)
        )
        conn.commit()
        conn.close()
        return render_template("hotel.html",signup_success=True)
    except IntegrityError:
        conn.close()
        return render_template("hotel-signup-page.html",username_exists=True
        )
    
    
@app.route("/homepage")
def homepage():
    return render_template("hotel_homepage.html")


@app.route("/menu")
def menu():
    return render_template("hotel_menu.html")



if __name__ == "__main__":
    app.run(debug=True)
    
    
#Roti
#Veg Biriyani
#Panner rice 
#jeera Rice
#palak Pulav