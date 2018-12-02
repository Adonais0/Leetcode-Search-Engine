from flask import Flask, render_template,request

app = Flask(__name__)

@app.route('/')
def index():
    hero_pic=""
    myhero="nochosen"
    xx=""
    return render_template("hero.html", heros=HEROS,hero_pic=hero_pic,myhero=myhero,results=xx)

# @app.route('/hero',methods=['GET','POST'])
# def hero():
#     if request.method=='POST':
#         myhero=request.form['hero']
#         results=process_top_10_decks(myhero)
#         xx=[]
#         yy=[]
#         for each in results:
#             deckname=str(each.get_deckname())
#             deckscore=int(each.get_deckscore())
#             xx.append(deckname)
#             yy.append(deckscore)
#         Data = [go.Bar(x=xx,y=yy)]
#         fig = go.Figure(data=Data)
#         hero_pic = plotly.offline.plot(fig, show_link=False, output_type="div", include_plotlyjs="static/plotly-latest.min.js")
#     else:
#         hero_pic=""
#         myhero="nochosen"
#         xx=""
#     return render_template("hero.html", heros=HEROS,hero_pic=hero_pic,myhero=myhero,results=xx)

# @app.route('/deck',methods=['GET','POST'])
# def deck():
#     deckname='Jade Druid Deck List Guide (Post Nerf) – Kobolds – April 2018'
#     chartname=""
#     if request.method=='POST':
#         deckname=request.form['deckname']
#         chartname=request.form['chartname']
#         mychart=getchart(deckname,chartname)
#     else:
#         mychart=""
#     return render_template("deckanalysize.html", deckname=deckname,chartname=chartname,mychart=mychart)



if __name__ == '__main__':

    app.run(debug=True)
