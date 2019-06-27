from bokeh.io import show
from bokeh.layouts import row, column
from bokeh.models import ColumnDataSource, CustomJS, Div
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
div = Div(text="")
div1 = Div(text="")
sdp.click = CustomJS(args={'div':div},code="""
console.log(`you clicked ${cb_data.word}`)
div.text = `you clicked ${cb_data.word}`
""")
sdp.hover = CustomJS(args={'div':div1},code="""
console.log(`HOV: ${cb_data.word}`)
div.text = `HOVER: ${cb_data.word}`
""")
div3 = Div(text="""
<pre>
sdp = WordCloud2(source=test1,wordCol="names",sizeCol="weights",colors=['pink','blue','green'])
div = Div(text="")
div1 = Div(text="")
sdp.click = CustomJS(args={'div':div},code='''
console.log(`you clicked ${cb_data.word}`)
div.text = `you clicked ${cb_data.word}`
''')
sdp.hover = CustomJS(args={'div':div1},code='''
console.log(`HOV: ${cb_data.word}`)
div.text = `HOVER: ${cb_data.word}`
''')
</pre>
""")
show(column([row([sdp,column([div,div1])]),div3]))
