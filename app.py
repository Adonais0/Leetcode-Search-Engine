from flask import Flask, render_template,request
import model

app = Flask(__name__)

@app.route('/')
def index():
    return '''
        <img src="/static/blockM.png"/>
        <h1>Michigan Sports Info!</h1>
        <ul>
            <li><a href="/bball"> Men's Basketball </a></li>
        </ul>
    '''

@app.route('/bball', methods=['GET', 'POST'])
def bball():
    if request.method == 'POST':
        sortby = request.form['sortby']
        sortorder = request.form['sortorder']
        seasons = model.get_bball_seasons(sortby, sortorder)
    else:
        seasons = model.get_bball_seasons()

    return render_template("seasons.html", seasons=seasons,ballname="bball")

@app.route('/football', methods=['GET', 'POST'])
def football():
    if request.method == 'POST':
        sortby = request.form['sortby']
        sortorder = request.form['sortorder']
        seasons = model.get_football_seasons(sortby, sortorder)
    else:
        seasons = model.get_football_seasons()

    return render_template("seasons.html", seasons=seasons,ballname="football")

@app.route('/hello', methods=['GET', 'POST'])
def hello():
    if request.method=='POST':
        firstname = request.form['firstname']
        lastname = request.form['lastname']
    else:
        firstname = ""
        lastname = ""
    return render_template("hello.html", firstname=firstname, lastname=lastname)

if __name__ == '__main__':
    model.init_bball()
    model.init_football()
    app.run(debug=True)
