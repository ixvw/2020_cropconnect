from app import app
import os
from pathlib import Path

def imgPath(filename):
    # check whether we are running on the server
    if not app.config["LOCAL"] == "True":
        print("running on the server! serving/storing img from/to resources...")
        return(app.config["FARMIMGPATH"] + filename)
    else:
        print("running locally, serving/storing img from/to static...")
        APP_FOLDER = os.path.dirname(os.path.abspath(app.instance_path))
        return("/static/farmimgs/"+str(filename))