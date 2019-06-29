from bokeh.io import show
from bokeh.models import ColumnDataSource, CustomJS
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
js=CustomJS(code="""
console.log("SIZE:",cb_data.size)
modifier = (cb_obj.height>cb_obj.width?cb_obj.height:cb_obj.width)/1024
return Math.pow(cb_data.size, 3.3) *  modifier
""")
test1 = ColumnDataSource({'names':names,'weights':weights})
sdp = WordCloud2(source=test1,wordCol="names",sizeCol="weights",colors=['pink','blue','green'],
                 weightFactor=10,width=1400,height=200)
show(sdp)
