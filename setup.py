from setuptools import setup

setup(
    name='bokeh_wordcloud2',
    version='1.0',
    packages=['bokeh_wordcloud2'],
    package_data={
        'bokeh_wordcloud2':['typescript/extension_bokeh_wordcloud2.ts'],
    },
    url='https://github.com/joran/bokeh_wordcloud2',
    license='GPL',
    author='joran',
    install_requires=['bokeh>=1.1.0'],
    author_email='joranbeasley@gmail.com',
    description='a bokeh extension that implements [wordcloud2](https://wordcloud2-js.timdream.org)'
)
