# utils/helpers.py
import os

def allowed_file(filename: str, allowed_extensions={"pdf"}) -> bool:
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in allowed_extensions

def init_directories(dirs):
    for d in dirs:
        if not os.path.exists(d):
            os.makedirs(d)
