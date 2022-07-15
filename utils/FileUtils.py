import os
import re

from utils.ImageUtils import safe_name


def ensure_dir(fpath):
    exists = os.path.exists(fpath)
    if not exists:
        os.makedirs(fpath)


def min_dir_name(text):
    # minimal directory name
    parts = text.split(' ')[0:3]
    out = '-'.join(parts)
    out = safe_name(out)
    return out
