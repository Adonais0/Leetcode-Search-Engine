from flask import Flask, render_template,request
from algorithm import *

app = Flask(__name__)

@app.route('/')
def index():
    if request.method == 'POST':
        searchContent = request.form['searchContent']
        print(searchContent)
    return render_template("index.html")


@app.route('/result', methods =['GET','POST'])
def result():
    if request.method == 'POST':
        searchContent = request.form['searchContent']
        print(searchContent)

    problems=search_and_show(searchContent)

    return render_template("result.html", problems = problems)

if __name__ == '__main__':

    app.run(debug=True)
