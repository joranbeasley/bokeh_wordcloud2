import os
import sys

try:
    tag = sys.argv[1]
except:
    pass
else:
    msg = "autotag" if len(sys.argv) < 3 else sys.argv[2]
    os.system("git tag \"%s\" -m \"%s\""%(tag,msg))
version = ".".join(os.popen("git describe --long").read().strip().split("-",1))
version_short = version.split("-",1)[0]
templ = """import os
from .bokeh_wordcloud2 import WordCloud2

__VERSION_FULL__ = "{version_full}"
__VERSION__ = "{version_short}"
"""
fpath = os.path.join(os.path.dirname(__file__),"bokeh_wordcloud2","__init__.py")
with open(fpath,"wb") as f:
    f.write(templ.format(version_full=version,version_short=version_short))
with open(fpath,"rb") as f:
    print(f.read())
try:
    xinput = raw_input
except:
    xinput = input
if xinput("Would you like to deploy to pypi?").lower().startswith("y"):
   os.system("python setup.py sdist")
   os.system("twine upload dist/*")
