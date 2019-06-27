import random

from bokeh.io import show, curdoc
from bokeh.layouts import widgetbox, column
from bokeh.models import ColumnDataSource, Button, Div
from bokeh_wordcloud2 import WordCloud2

data = [
    ['susan',6],
    ['tom',3],
    ['frankie',8],
    ['roger',7],
    ['amy',9],
    ['nicole',10],
    ['joran',5],
    ['mark',4],
    ['brianne',7],
    ['michael',8],
    ['greg',4],
    ['adrian',6],
    ['drew',9]
]
names,weights = zip(*data)
test1 = ColumnDataSource({'names':names,'weights':weights})
sdp = WordCloud2(source=test1,wordCol="names",sizeCol="weights",colors=['pink','blue','green'])
def clicked_word(evt):
    data=test1.data
    if(7 < evt.weight < 20 ):
        new_weight = evt.weight + random.choice([-1,1,1,2])
    elif evt.weight < 7:
        new_weight = evt.weight + random.choice([1,2])
    elif evt.weight < 20:
        new_weight = evt.weight - random.choice([1,2,3])
    weights = list(data['weights'])
    weights[data['names'].index(evt.word)] = new_weight
    test1.data = {'names':data['names'][:],'weights':weights}


button = Div(text="<h1>Click A Word!</h1>")
# button.on_click(callback)
# show(sdp)
sdp.on_click(clicked_word)
curdoc().add_root(column(sdp))
