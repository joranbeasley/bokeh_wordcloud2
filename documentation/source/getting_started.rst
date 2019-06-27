Getting Started
===============

Installation
------------
the easiest way to install is with pip

.. code-block:: bash

   # install from pipi
   pip install bokeh_wordcloud2

   # install from github
   pip install git+https://github.com/joranbeasley/bokeh_wordcloud2.git#bokeh_wordcloud

   # clone and build
   git clone pip git+https://github.com/joranbeasley/bokeh_wordcloud2.git
   cd bokeh_wordcloud2
   pip install .  # alternatively `python setup.py install`

Examples
--------
First Word Cloud
~~~~~~~~~~~~~~~~
here is a super simple word cloud to get you started

| you can find this example at
  `Simple Example Source <https://github.com/joranbeasley/bokeh_wordcloud2/tree/master/examples/simple_counts_static_html.py>`_
| you can see its html here
  `Simple Example HMTL <_static/simple_counts_static_html.html>`_

.. code-block:: python
   :linenos:

   from bokeh.io import show
   from bokeh.models import ColumnDataSource
   from bokeh_wordcloud2 import WordCloud2

   data = [
       ['susan',6], ['tom',3], ['frankie',8],
       ['roger',7], ['amy',9], ['nicole',10],
       ['joran',5], ['mark',4], ['brianne',7],
       ['michael',8], ['greg',4], ['adrian',6],
       ['drew',9]
   ]
   names,weights = zip(*data)
   test1 = ColumnDataSource({'names':names,'weights':weights})
   # we will specify just "blue" for the color
   wordcloud = WordCloud2(source=test1,wordCol="names",sizeCol="weights",colors="blue")
   show(wordcloud)

when you run the application you should see a webpage open with your newly created Wordcloud

.. raw:: html
   :file: _static/simple_counts_static_html.html

Using a corpus instead
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

if you dont specify a ``sizeCol``, then it will extract all the words from the ``wordCol``
and use the counts as a size

.. raw:: html
   :file: _static/extract_words_static_html.html

| you can find this example at
  `Example Source <https://github.com/joranbeasley/bokeh_wordcloud2/tree/master/examples/extract_words_static_html.py>`_


.. code-block:: python

   from bokeh.io import show
   from bokeh.models import ColumnDataSource
   from bokeh_wordcloud2 import WordCloud2
   titles = ['lorem ipsum dolor sit amet',
             'consectetur adipiscing elit',
             ... (ALOT MORE) ...
             'cras iaculis semper odio',
             'eu posuere urna vulputate sed']
   test2 = ColumnDataSource({'titles':titles})
   # we will randomly select from 3 colors
   wc = WordCloud2(source=test2,wordCol="titles",colors=['pink','blue','green'])
   show(wc)

Color Options
~~~~~~~~~~~~~

for the color options we can pass in a single color that will be assigned to all words ::

   # all the words are pink
   WordCloud2(source=test2,wordCol="titles",colors='pink')

or we can pass in a list, and randomly select from it::

   # pick a random color
   random_colors=['pink','blue']
   WordCloud2(source=test2, wordCol="titles", colors=random_colors)

or if our datasource has a column for colur we can pass in the name of that (only works if you specify sizeCol) ::

   colors = [['red','green','blue','purple'][i%4]
               for i in range(len(test1.data['words']))]
   test1.data['colorsCol']  = colors # assign a new column
   WordCloud2(source=test1,wordCol="names",sizeCol="weights",
              colors="colorsCol")  # use our column name instead

or we can supply a javascript callback that returns a string, but we name it slightly differently ::

   colorFun = CustomJS(code="""
   console.log("PICKING A COLOR FOR:",cb_obj)
   console.log("Got Word:",cb_data['word'],cb_data['weight'],cb_data['fontSize'])
   return "red" # dont forget to RETURN a value
   """)

   WordCloud2(source=test1,wordCol="names",sizeCol="weights",colorsFun=colorFun)


| you can find this example at
  `Color Options <https://github.com/joranbeasley/bokeh_wordcloud2/tree/master/examples/simple_options_colors.py>`_
| you can see its html here
  `Color Options HMTL <_static/simple_options_colors.html>`_

Clicks And Hovers
~~~~~~~~~~~~~~~~~
you can subscribe to either clicks or hovers with a javascript object

.. raw:: html
   :file: _static/js_callbacks.html

| you can find this example at
  `JS Callbacks <https://github.com/joranbeasley/bokeh_wordcloud2/tree/master/examples/js_callbacks.py>`_
| you can see its html here
  `JS Callbacks HMTL <_static/js_callbacks.html>`_

Python Click Callback
~~~~~~~~~~~~~~~~~~~~~

.. note::

   this only applies when running bokeh server `bokeh run my_app.py`

you can also subscribe to the click handler in python if you are running with bokeh server ::

   wordcloud = WordCloud2(source=test1, wordCol="names", sizeCol="weights", colors=['pink', 'blue', 'green'])

   def clicked_word(evt):
       print("GOT:",evt)
       data=test1.data
       if(7 < evt.weight < 20 ):
           new_weight = evt.weight + random.choice([-1,1,1,2])
       elif evt.weight < 7:
           new_weight = evt.weight + random.choice([1,2])
       elif evt.weight < 20:
           new_weight = evt.weight - random.choice([1,2,3])
       weights = list(data['weights'])
       weights[data['names'].index(evt.word)] = new_weight
       # make sure to reassign back to data a new dict, or the difference might not be noticed
       test1.data = {'names':data['names'][:],'weights':weights}

   # subscribe to the click event
   wordcloud.on_click(clicked_word)
   curdoc().add_root(column(wordcloud))

| you can find this example at
  `Bokeh Server Example <https://github.com/joranbeasley/bokeh_wordcloud2/tree/master/examples/python_callbacks_server.py>`_
| *since you must be running with* ``bokeh serve app.py`` * I cannot show you the html*
