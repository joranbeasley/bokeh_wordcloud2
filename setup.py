from setuptools import setup

with open("README.md", "r") as fh:
    long_description = fh.read()
setup(
    name='bokeh_wordcloud2',
    version='1.0',
    packages=['bokeh_wordcloud2'],
    package_data={
        'bokeh_wordcloud2':['typescript/extension_bokeh_wordcloud2.ts'],
    },
    url='https://bokeh-wordcloud2.readthedocs.io',
    long_description=long_description,
    long_description_content_type="text/markdown",
    license='GPL',
    author='joran beasley',
    install_requires=['bokeh>=1.1.0'],
    author_email='joranbeasley@gmail.com',
    description='a bokeh extension that implements [wordcloud2](https://wordcloud2-js.timdream.org)'
)
