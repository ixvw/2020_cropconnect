from app import app


def allowedImg(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in app.config("ALLOWED_EXTENSIONS")
