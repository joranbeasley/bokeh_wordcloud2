from bokeh.io import show
from bokeh.layouts import column, row
from bokeh.models import ColumnDataSource, Div, CustomJS
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
just_blue = WordCloud2(width=400, height=400, background="#DEDEDE",
                       source=test_source, wordCol="names", sizeCol="weights", color="blue")

label2 = Div(text="<h2>Random Colors</h2>")
some_random_colors=['pink','blue','green']
random_colors = WordCloud2(width=400, height=400, source=test_source, background="#EFEFEF",
                           wordCol="names", sizeCol="weights", color=some_random_colors)

label3 = Div(text="<h2>Specific Colors(By Gender)</h2>")
colors_by_gender = ['pink','blue','pink','blue','pink','pink','blue','blue','pink','blue','blue','blue','blue']
test_source2 = ColumnDataSource({"names":names,"weights":weights,"color":colors_by_gender})
gendered_cloud = WordCloud2(width=400, height=400, source=test_source2, background="#EFEFEF",
                            wordCol="names", sizeCol="weights", color="color")


colors_fun = CustomJS(code='''
    if( cb_data.word.indexOf("o") >= 0) return "red"
    return "blue"
    ''')
color_callback_ex=WordCloud2(source=test_source, background="#DEDEDE", width=400, height=400,
           wordCol="names",
           sizeCol="weights",
           color=colors_fun) # column name
label4 = Div(text="<h2>Colors from JS Callback</h2>")



page = column([row([
    column([label1,just_blue]),
    column([label2,random_colors])]),
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
    </pre>""")]),
    row([
        column([label3,gendered_cloud]),
        column([label4,color_callback_ex]),
    ]),
    row([
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
    Div(width=400,text="""<pre>
    colors_fun = CustomJS(code='''
    if cb_data.word.indexOf("o") >= 0:
       return "red"
    return "blue"
    ''')
    
    WordCloud2(source=test_source, 
               wordCol="names", 
               sizeCol="weights", 
               colors=colors_fun) # column name    
        </pre>"""),
         ])
])
show(page)
