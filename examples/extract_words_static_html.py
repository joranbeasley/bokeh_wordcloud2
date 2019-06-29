from bokeh.io import show
from bokeh.layouts import column
from bokeh.models import ColumnDataSource, Div

from bokeh_wordcloud2 import WordCloud2

titles = ['lorem ipsum dolor sit amet',
          'consectetur adipiscing elit',
          'cras iaculis semper odio',
          'eu posuere urna vulputate sed',
          'quisque hendrerit', 'felis ac condimentum laoreet',
          'nunc dolor bibendum lorem',  'a egestas velit eros ut dui',
          'sed facilisis urna ultrices gravida maximus',  'morbi sed nisl fermentum',
          'laoreet dui viverra', 'dignissim metus quisque lobortis eros placerat',
          'imperdiet lobortis', 'nisi mi porttitor odio quis ultrices diam metus ac dolor',
          'pellentesque tristique cursus nisl at pretium',  'sed lorem leo vulputate nec aliquet eu',
          'tempor eu purus', 'ut nec ex pretium', 'pellentesque mi quis', 'ornare dolor',
          'donec pulvinar cursus diam quis accumsan', 'fusce porta finibus nisl sed aliquet',
          'nam aliquet', 'dolor id consectetur consectetur', 'mi sapien iaculis velit',
          'sed gravida justo metus sed lorem', 'pellentesque varius libero eu orci tempor consectetur',
          'suspendisse lacinia fringilla quam at hendrerit', 'cras eu laoreet enim',
          'sed luctus', 'ligula dignissim dapibus maximus', 'ligula orci dictum elit',
          'eget dictum dui lorem sed augue', 'proin orci purus', 'fermentum a feugiat non',
          'pretium id eros', 'fusce mauris dui', 'elementum vel justo at', 'iaculis luctus ligula',
          'sed eget velit cursus', 'posuere magna quis', 'tristique lectus', 'ut bibendum',
          'tortor at porta sodales', 'mauris libero congue dui', 'eu consectetur urna augue a nunc',
          'duis a odio ac quam imperdiet fermentum vitae nec elit',
          'sed suscipit erat sed imperdiet posuere', 'ut imperdiet dolor non turpis porttitor efficitur',
          'vestibulum porttitor at arcu sit amet auctor', 'nam congue erat quam',
          'sed vulputate mauris bibendum in', 'pellentesque est quam', 'tempor at est eget',
          'ullamcorper consequat dolor', 'duis facilisis ante lorem', 'id vehicula nisi venenatis sit amet',
          'nunc iaculis a mauris eu molestie', 'aenean auctor eros nec dolor viverra',
          'vitae placerat enim euismod', 'lorem ipsum dolor sit amet', 'consectetur adipiscing elit',
          'sed neque nisi', 'vulputate non sollicitudin at', 'finibus tristique augue', 'ut neque purus',
          'accumsan vestibulum urna sit amet', 'egestas imperdiet est', 'donec ut suscipit lorem',
          'in hendrerit turpis', 'mauris et tincidunt elit', 'et molestie est', 'sed ut posuere sem',
          'et molestie lacus', 'nullam metus lorem', 'fermentum quis lorem nec', 'lobortis dignissim velit',
          'phasellus et nulla vitae dolor facilisis vulputate', 'phasellus accumsan est vel ex posuere',
          'vitae tristique libero venenatis', 'pellentesque maximus dui eros',
          'consequat pretium velit lacinia eu', 'mauris efficitur ac leo varius egestas',
          'quisque tincidunt ornare arcu', 'in gravida lacus rhoncus sit amet', 'pellentesque elementum fringilla diam',
          'etiam vulputate', 'est id porttitor sodales', 'ligula diam faucibus neque',
          'vitae lobortis elit massa at odio', 'posuere ac urna',
          'nam consectetur turpis quis metus malesuada pellentesque eget et urna',
          'curabitur vitae enim quis ante luctus finibus', 'fusce accumsan nibh a lectus tincidunt',
          'quis tristique sem laoreet', 'duis elit erat', 'congue eget scelerisque et', 'viverra ut est',
          'sed vulputate mi id nisl mattis imperdiet', 'donec pharetra ultricies egestas',
          'proin varius varius pretium', 'proin lacinia euismod mi', 'quis vestibulum orci finibus ut',
          'donec ac nisl ut arcu pulvinar condimentum non eu velit', 'etiam id egestas arcu',
          'donec ullamcorper at lacus ut porta', 'nulla nulla urna', 'aliquet vel iaculis sed',
          'cras ut diam gravida', 'semper velit eget', 'convallis erat', 'nullam rhoncus nec mauris non dignissim',
          'aliquam sed risus non justo luctus iaculis', 'fusce sed fringilla turpis', 'a sagittis metus',
          'pellentesque blandit in augue ultricies fermentum', 'integer finibus congue sollicitudin',
          'nunc consequat nisi est', 'non tempus massa tempus nec', 'nullam cursus orci a iaculis bibendum',
          'praesent auctor lacus eget semper auctor', 'praesent nulla neque',
          'scelerisque facilisis dignissim sed', 'porttitor sed purus', 'suspendisse placerat felis felis',
          'at pellentesque turpis accumsan vitae',
          'pellentesque ac blandit sapien',
          'pellentesque volutpat finibus sem',
          'vitae mollis ligula malesuada ut']

test1 = ColumnDataSource({'titles':titles})
sdp = WordCloud2(source=test1,wordCol="titles",color=['pink','blue','green'])
show(column([sdp,
             Div(text="""
<pre>
titles = ['lorem ipsum dolor sit amet',
          'consectetur adipiscing elit',
          ... (ALOT MORE) ...
          'cras iaculis semper odio',
          'eu posuere urna vulputate sed']
test1 = ColumnDataSource({'titles':titles})  
WordCloud2(source=test1,wordCol="titles",colors=['pink','blue','green'])        
 </pre>
             """)]))
