import os
import re

from utils.ImageUtils import safe_name


def ensure_dir(fpath):
    exists = os.path.exists(fpath)
    if not exists:
        os.makedirs(fpath)


def remove_common(text):
    common = [
        'photo',
        'color',
        'photograph',
        'paparazzi',
        'drawing',
        'painting',
        'by ',
        'in the style of',
        'of ',
        'a ',
        'the'
    ]
    text = text.lower()
    for word in common:
        text = re.sub(word, '', text)

    return text


def min_dir_name(text):
    # minimal directory name
    text = remove_common(text)
    parts = text.split(' ')[0:3]
    out = '-'.join(parts)
    out = safe_name(out)
    return out
