from app import app
import os
from pathlib import Path
import sys


def imgPath(filename):
    APP_FOLDER = os.path.dirname(os.path.abspath(app.instance_path))

    # check whether we are running on the server
    if sys.path[0] == "/var/www/cropconnect/":
        print("running on the server! serving/storing img from/to resources...")
        return("resources/" + filename)
    else:
        print("running locally, serving/storing img from/to static...")
        return(os.path.join(APP_FOLDER, Path("app/static/farmimgs/" + filename)))