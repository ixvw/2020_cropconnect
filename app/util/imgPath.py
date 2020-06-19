from app import app
import os
from pathlib import Path

def imgPath(filename):
    APP_FOLDER = os.path.dirname(os.path.abspath(app.instance_path))
    return(os.path.join(APP_FOLDER, Path("app/static/farmimgs/" + filename)))