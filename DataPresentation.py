from flask import Flask, render_template,request
from DataProcessing import *
import plotly.plotly as py
import plotly.graph_objs as go
import plotly

app = Flask(__name__)

@app.route('/')
def index():
    hero_pic=""
    myhero="nochosen"
    xx=""
    return render_template("hero.html", heros=HEROS,hero_pic=hero_pic,myhero=myhero,results=xx)

@app.route('/hero',methods=['GET','POST'])
def hero():
    if request.method=='POST':
        myhero=request.form['hero']
        results=process_top_10_decks(myhero)
        xx=[]
        yy=[]
        for each in results:
            deckname=str(each.get_deckname())
            deckscore=int(each.get_deckscore())
            xx.append(deckname)
            yy.append(deckscore)
        Data = [go.Bar(x=xx,y=yy)]
        fig = go.Figure(data=Data)
        hero_pic = plotly.offline.plot(fig, show_link=False, output_type="div", include_plotlyjs="static/plotly-latest.min.js")
    else:
        hero_pic=""
        myhero="nochosen"
        xx=""
    return render_template("hero.html", heros=HEROS,hero_pic=hero_pic,myhero=myhero,results=xx)

@app.route('/deck',methods=['GET','POST'])
def deck():
    deckname='Jade Druid Deck List Guide (Post Nerf) – Kobolds – April 2018'
    chartname=""
    if request.method=='POST':
        deckname=request.form['deckname']
        chartname=request.form['chartname']
        mychart=getchart(deckname,chartname)
    else:
        mychart=""
    return render_template("deckanalysize.html", deckname=deckname,chartname=chartname,mychart=mychart)

def getchart(deckname,chartname):
    if chartname=="crystal_usage":
        result1=process_crystal_usage(deckname,'Class')
        x1=[]
        y1=[]
        for each in result1:
            x1.append(each[0])
            y1.append(each[1])
        trace1 = go.Bar(x=x1,y=y1,name='Class')
        result2=process_crystal_usage(deckname,'Neutral')
        x2=[]
        y2=[]
        for each in result2:
            x2.append(each[0])
            y2.append(each[1])
        trace2 = go.Bar(x=x2,y=y2,name='Neutral')
        data = [trace1, trace2]
        layout = go.Layout(barmode='stack')
        fig = go.Figure(data=data, layout=layout)
        mychart = plotly.offline.plot(fig, show_link=False, output_type="div", include_plotlyjs="static/plotly-latest.min.js")
    elif chartname=="attack_health":
        result1=process_attack_or_health_usage(deckname,'Attack')
        x1=[]
        y1=[]
        for each in result1:
            x1.append(each[0])
            y1.append(each[1])
        trace1 = go.Scatter(x=x1,y=y1,name='Attack',connectgaps=True)
        result2=process_attack_or_health_usage(deckname,'Health')
        x2=[]
        y2=[]
        for each in result2:
            x2.append(each[0])
            y2.append(each[1])
        trace2 = go.Scatter(x=x2,y=y2,name='Health',connectgaps=True)
        data = [trace1, trace2]
        fig = dict(data=data)
        mychart = plotly.offline.plot(fig, show_link=False, output_type="div", include_plotlyjs="static/plotly-latest.min.js")
    elif chartname=="race_barchart":
        result1=process_race_composition(deckname)
        x1=[]
        y1=[]
        for each in result1:
            x1.append(each[0])
            y1.append(each[1])
        trace = go.Pie(labels=x1, values=y1)
        fig = [trace]
        mychart = plotly.offline.plot(fig, show_link=False, output_type="div", include_plotlyjs="static/plotly-latest.min.js")
    else:
        mychart = ""
    return mychart

if __name__ == '__main__':

    app.run(debug=True)
