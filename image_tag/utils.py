import hashlib
import os
from tensorflow.keras.utils import get_file


def get_hash(filename):
    '''This Function checks the sha256sum integrity of downloaded model'''
    print(get_hash.__doc__)
    sha256_hash = hashlib.sha256()
    with open(filename, "rb") as f:
        for byte_block in iter(lambda: f.read(4096), b""):
            sha256_hash.update(byte_block)

    return sha256_hash.hexdigest()


def download_model(url, file_path, file_sha256):
    '''THis FUnction downloads the model from given path'''
    print(download_model.__doc__)
    if os.path.exists(file_path) and get_hash(file_path) == file_sha256:
        print("File already exists")
    else:
        get_file(origin=url, fname=file_path, cache_dir=".", cache_subdir="")
