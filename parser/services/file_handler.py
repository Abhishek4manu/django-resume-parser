import os
from django.core.files.storage import default_storage

UPLOAD_DIR = "resumes"

def save_temp_file(file):
    file_path = default_storage.save(f"{UPLOAD_DIR}/{file.name}", file)
    return default_storage.path(file_path)

def delete_file(path):
    if os.path.exists(path):
        os.remove(path)
