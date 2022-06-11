import os
import re
import requests


def fetch_image(url, name):
    response = requests.get(url)
    fpath = f'renders/{name}'
    open(fpath, "wb").write(response.content)


def file_exists(fname):
    fpath = f'renders/{fname}'
    return os.path.isfile(fpath)


def sane(text):
    return re.sub(r'\.png|.jpg', '', text)


def image_url(fname):
    return f'https://revel.alfalabs.xyz/projects/joker-art/photos/{fname}'
