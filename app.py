from flask import Flask, render_template, request, redirect
import christmasfriend

app = Flask(__name__)
phonenumber = None
password = None


@app.route('/', methods =["GET", "POST"])
def gfg():

    if request.method == "POST":
        global phonenumber
        global password
        # getting input with name = fname in HTML form
        phonenumber = request.form.get("fname")
        # getting input with name = lname in HTML form
        password = request.form.get("lname")
        return redirect("/login")
    return render_template("login.html")


@app.route("/login")
def login():
    print(phonenumber)
    print(password)

    if phonenumber in christmasfriend.dictionary:
        if christmasfriend.dictionary[phonenumber]["Password"] == password:
            return redirect("/ourpage")
        else:
            print("incorrect password")
    else:
        print("Does not exist")


@app.route("/ourpage")
def ourpage():
    return christmasfriend.dictionary[phonenumber]


if __name__ == "__main__":
    app.run(debug=True)
