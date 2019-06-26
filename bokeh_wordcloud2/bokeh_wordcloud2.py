import math
from bokeh.core.property.container import Array, List
from bokeh.core.property.either import Either
from bokeh.core.property.instance import Instance
from bokeh.core.property.primitive import String, Float, Int
from bokeh.events import Event
from bokeh.models import DataSource, CDSView, Widget, CustomJS, Callback, ColumnDataSource,Button



class WordClick(Event):
    '''
    Custom Event that is fired when the user clicks a word
    '''
    event_name = 'word_click_event'
    word=None
    weight=None
    def __init__(self, model,word,weight):
        if model is not None and not isinstance(model, WordCloud2):
            msg ='{clsname} event only applies to button models'
            raise ValueError(msg.format(clsname=self.__class__.__name__))
        self.word=word
        self.weight=weight

        super(WordClick, self).__init__(model=model)
    def __str__(self):
        return "<WordClickEvent word=%r weight=%r>"%(self.word,self.weight)
    def __repr__(self):
        return str(self)

class _WordCloud2Meta(Widget):
    __implementation__ = "typescript/extension_bokeh_wordcloud2.ts"
    __javascript__ = [
        "https://ajax.googleapis.com/ajax/libs/jquery/2.1.1/jquery.min.js",
        "https://cdnjs.cloudflare.com/ajax/libs/wordcloud2.js/1.0.6/wordcloud2.min.js",
        "https://raw.githubusercontent.com/timdream/wordcloud2.js/gh-pages/src/wordcloud2.js",

    ]

class WordCloud2(_WordCloud2Meta):
    source = Instance(DataSource, help="""
        The source of data for the widget.
        """)

    view = Instance(CDSView, help="""
        A view into the data source to use when rendering table rows. A default view
        of the entire data source is created if a view is not passed in during
        initialization.
        """)

    sizeCol = String(help="the column of the weights, if unspecified it will count word occurences")
    wordCol = String(help="the column with the words in it")
    colors = Either(String,List(String),help="a single color, a list of colors to randomly choose from, or a column name with colors in it")
    colorsFun = Instance(CustomJS,help="a customjs function that will determine the colors (see `cb_obj`)")
    fontWeight = String(default="normal",help="the font weight to use")
    fontWeightFun = Instance(CustomJS,help="a customjs function that will determine the fontWeight(see `cb_obj`)")
    classes = String(help="a class name or function to use ... only works if using DOM elements, which are currently unsupported... so this does nothing for now")
    classesFun = Instance(CustomJS,help="see `classes`")

    rotateRatio = Float(help="the odds of a given word rotating between 0-1",default=1)
    minRotation = Float(help="the minimum amount(in radians) to rotate",default=0)
    maxRotation = Float(help="the max amount(in radians) to rotate",default=math.pi/2.0)
    rotationSteps = Int(help="the number of slices to cut the rotation range into",default=32)
    shape = String(help="the shape of the wordcloud ENUM(circle, cartoid, diamond, square, triangle-forward, triangle, pentagon, star)",default="square")

    hover = Instance(CustomJS)
    click = Instance(Callback)
    def __init__(self, **kw):
        super(WordCloud2, self).__init__(**kw)
        if "view" not in kw:
            self.view = CDSView(source=self.source)
    def on_click(self,python_callback):
        self.on_event(WordClick, python_callback)

