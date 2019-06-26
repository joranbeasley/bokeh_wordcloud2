from bokeh.io import show
from bokeh.layouts import column, row
from bokeh.models import ColumnDataSource, Div
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
test_source = ColumnDataSource({'names':names, 'weights':weights})

label1 = Div(text="<h2>Just Blue</h2>")
just_blue = WordCloud2(width=400, height=400, source=test_source, wordCol="names", sizeCol="weights", colors="blue")

label2 = Div(text="<h2>Random Colors</h2>")
some_random_colors=['pink','blue','green']
random_colors = WordCloud2(width=400, height=400, source=test_source, wordCol="names", sizeCol="weights", colors=some_random_colors)

label3 = Div(text="<h2>Specific Colors(By Gender)</h2>")
colors_by_gender = ['pink','blue','pink','blue','pink','pink','blue','blue','pink','blue','blue','blue','blue']
test_source2 = ColumnDataSource({"names":names,"weights":weights,"color":colors_by_gender})
gendered_cloud = WordCloud2(width=400, height=400, source=test_source2, wordCol="names", sizeCol="weights", colors="color")


page = column([row([
    column([label1,just_blue]),
    column([label2,random_colors]),
    column([label3,gendered_cloud])
    ]),
    row([Div(width=400,text="""<pre>
WordCloud2(source=test_source, 
           wordCol="names", 
           sizeCol="weights", 
           colors="blue")# single color    
    </pre>"""),
        Div(width=400,text="""<pre>
WordCloud2(source=test_source, 
           wordCol="names", 
           sizeCol="weights", 
           # random choices
           colors=['pink','blue','green'])    
    </pre>"""),
        Div(width=400,text="""<pre>
colors_by_gender = ['pink','blue','pink','blue',
'pink','pink','blue','blue','pink','blue',
'blue','blue','blue']
test_source2 = ColumnDataSource({"names":names,
                                 "weights":weights,
                                 "color":colors_by_gender})
WordCloud2(source=test_source, 
           wordCol="names", 
           sizeCol="weights", 
           colors="color") # column name    
    </pre>"""),

         ])
])
show(page)
