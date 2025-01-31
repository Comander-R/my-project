from flask import Flask, render_template, request

app = Flask(__name__)

class user:
    def __init__(self,email,username,password,age,number):
        self.email = email
        self.username = username
        self.password = password
        self.age = age
        self.number = number

list = []
user1 = user("non","non","non","non","non")
user2 = user("non","non","non","non","non")
user3 = user("non","non","non","non","non")

@app.post("/user_profile")
def register_post():
    email = request.form.get("email")
    username = request.form.get("username")
    password = request.form.get("password")
    age = request.form.get("age")
    number =  request.form.get("number")
    return render_template("template","user.html")

@app.route("/<name>")
def way(name):
    return render_template( name = name )

if __name__ == "__main__":
    app.run(debug=False)