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



@app.route('/', methods =["GET", "POST"])
def gfg():

    message = "Enter your Phone Number and Password "

    if request.method == "POST":
        # getting input with name = fname in HTML form
        phonenumber = request.form.get("fname")
        # getting input with name = lname in HTML form
        password = request.form.get("lname")

        if phonenumber in FinalRealData:
            if FinalRealData[phonenumber]["Password"] == password:
                return render_template("result.html", **FinalShuffledData[phonenumber])
            else:
                message = "Incorrect password. If you forgot your password please check your mail we have send a copy of your form responce to your mail."
                render_template("index.html", message = message )

        else:
            message = "You have not registered for Christmas Friend."
            render_template("index.html", message = message )
    return render_template("index.html", message = message )



if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000)
