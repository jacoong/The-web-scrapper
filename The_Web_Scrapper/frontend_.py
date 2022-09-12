from logging import exception
from flask import Flask, redirect, render_template, request, send_file, flash
from main import start_scrapping
from save import save_to_file
app = Flask("test_App")
app.config["SECRET_KEY"] = "ABCD"
db={}

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/report")
def react():

    word= request.args.get('word')
    if word:
        word= word.lower()
        store_data = db.get(word)
        if store_data:
            jobs = store_data
        else:
            jobs = start_scrapping(word)
            db[word] = jobs
            if (len(db[word]) ==0):
                return redirect("/sorry")

            
    return render_template("/report.html", word = word, number = len(jobs), jobs =jobs)


@app.route("/download")
def datasave():
    try:
        word = request.args.get('word')
        if word:
            word= word.lower()
            db_value = db[word]
            if db_value:
                save_to_file(db_value)
                return send_file("jobs.csv",mimetype='text/csv',attachment_filename='jobs_file.csv',# 다운받아지는 파일 이름. 
                     as_attachment=True)
        else:
            raise Exception()
    except:
            return redirect("/")


@app.route("/sorry")
def sorry():
    return render_template("sorry.html")
        

    
app.run(debug=True)