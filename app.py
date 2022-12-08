from flask import Flask, render_template, request, redirect
import csv

app = Flask(__name__)
phonenumber = None
password = None

googleFormCsv = 'names.csv'
ShuffledCsv = 'FinalResult.csv'


#opening google font csv and converting to list
with open(googleFormCsv) as f:
    reader = csv.DictReader(f)
    googleFormData = list(reader)


#making list of phone numbers
with open(googleFormCsv) as f:
    reader = csv.DictReader(f)
    Data = {"Phone": []}
    for record in reader:
        Data["Phone"].append(record["Phone"])


#making list of phone numbers
GoogleFormDataNumbers = []
for i in range(0, len(Data["Phone"])):
    GoogleFormDataNumbers.append(Data["Phone"][i])

with open(ShuffledCsv) as f:
    reader = csv.DictReader(f)
    ShuffledData = list(reader)

FinalRealData = {}
for i in range(len(GoogleFormDataNumbers)):
    FinalRealData[GoogleFormDataNumbers[i]] = googleFormData[i]

FinalShuffledData = {}
for i in range(len(GoogleFormDataNumbers)):
    FinalShuffledData[GoogleFormDataNumbers[i]] = ShuffledData[i]

print(googleFormData)
print(Data)
print(GoogleFormDataNumbers)
print(FinalShuffledData["1839280640"])
print(FinalRealData["1839280640"]["Name"])



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

    if phonenumber in FinalShuffledData:
        if FinalShuffledData[phonenumber]["Password"] == password:
            return redirect("/ourpage")
        else:
            print("incorrect password")
    else:
        print("Does not exist")
    return "ERROR"


@app.route("/ourpage")
def ourpage():
    return FinalShuffledData[phonenumber]


if __name__ == "__main__":
    app.run(debug=True)
