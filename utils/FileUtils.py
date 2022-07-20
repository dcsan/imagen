import datetime
import os
import re
import requests


def ensure_dir(fpath):
    exists = os.path.exists(fpath)
    if not exists:
        os.makedirs(fpath)


def fetch_image(output, fpath):
    if type(output) == str:
        image_url = output
    elif type(output) == dict:
        # all models are different ><
        image_url = output.get('image') or \
            output.get('url') or \
            output.get('file')
    else:
        raise Exception(f'unknown output type: {type(output)}', output)

    if not image_url:
        raise Exception('cannot find image url', output)

    print('fetching', image_url, 'to', fpath)
    response = requests.get(image_url)
    open(fpath, "wb").write(response.content)


def file_exists(fname):
    fpath = f'output/renders/{fname}'
    return os.path.isfile(fpath)


def image_url(fname):
    return f'https://revel.alfalabs.xyz/projects/joker-art/photos/{fname}'


def timestamp():
    now = datetime.datetime.now()
    print(now.strftime("%Y-%m-%d %H:%M:%S"))
