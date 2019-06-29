import os
import sys
fpath = os.path.join(os.path.dirname(__file__),"bokeh_wordcloud2","__init__.py")

def ask_deploy():
    try: # python 2.7 ...
        xinput = raw_input
    except:
        xinput = input
    return xinput("Would you like to deploy to pypi?").lower().startswith("y")
def deploy_to_pypi_if_desired():
    if ask_deploy():
        os.system("python setup.py sdist")
        os.system("twine upload dist/*")

try:
    tag = sys.argv[1]
except:
    pass
else:
    if tag == "deploy":
        print("Deploy:")
        with open(fpath, "rb") as f:
            print(f.read())
        deploy_to_pypi_if_desired()
        sys.exit()

    msg = "autotag" if len(sys.argv) < 3 else sys.argv[2]
    os.system("git tag \"%s\" -m \"%s\""%(tag,msg))

version = ".".join(os.popen("git describe --long").read().strip().split("-",1))
version_short = version.split("-",1)[0]
templ = """import os
from .bokeh_wordcloud2 import WordCloud2

__VERSION_FULL__ = "{version_full}"
__VERSION__ = "{version_short}"
"""

with open(fpath,"wb") as f:
    f.write(templ.format(version_full=version,version_short=version_short))
with open(fpath,"rb") as f:
    print(f.read())
deploy_to_pypi_if_desired()
