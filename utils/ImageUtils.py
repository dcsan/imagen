import datetime
import os
import re
import requests


def fetch_image(url, fpath):
    response = requests.get(url)
    open(fpath, "wb").write(response.content)


def file_exists(fname):
    fpath = f'renders/{fname}'
    return os.path.isfile(fpath)


def remove_suffix(text):
    return re.sub(r'\.png|.jpg', '', text)


def safe_name(text):
    text = re.sub(r'\W+', '-', text)
    text = text.lower()
    text = re.sub(r'^-', '', text)  # remove leading -
    text = re.sub(r'--', '-', text)  # remove duplicate -
    return text


def image_url(fname):
    return f'https://revel.alfalabs.xyz/projects/joker-art/photos/{fname}'


def timestamp():
    now = datetime.datetime.now()
    print(now.strftime("%Y-%m-%d %H:%M:%S"))
