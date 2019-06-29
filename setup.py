from setuptools import setup
from bokeh_wordcloud2 import __VERSION__
with open("README.md", "r") as fh:
    long_description = fh.read()


setup(
    name='bokeh_wordcloud2',
    version=__VERSION__,
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
    description='a bokeh extension that implements a wordcloud (https://wordcloud2-js.timdream.org)',
    classifiers=[
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 2.7",
        "Operating System :: OS Independent",
        "Intended Audience :: Developers",
        "Intended Audience :: Information Technology",
        "Intended Audience :: Other Audience",
        "License :: Freely Distributable",
        "Topic :: Scientific/Engineering :: Information Analysis",
        "Topic :: Software Development :: Widget Sets"
    ]
)
