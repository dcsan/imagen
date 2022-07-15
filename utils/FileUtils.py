import datetime
import os
import re
import requests


def ensure_dir(fpath):
    exists = os.path.exists(fpath)
    if not exists:
        os.makedirs(fpath)


def fetch_image(output, fpath):
    image_url = output.get('image')  # for dalle mini
    response = requests.get(image_url)
    open(fpath, "wb").write(response.content)


def file_exists(fname):
    fpath = f'renders/{fname}'
    return os.path.isfile(fpath)


def image_url(fname):
    return f'https://revel.alfalabs.xyz/projects/joker-art/photos/{fname}'


def timestamp():
    now = datetime.datetime.now()
    print(now.strftime("%Y-%m-%d %H:%M:%S"))
