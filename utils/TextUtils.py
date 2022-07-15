import re


def remove_suffix(text):
    return re.sub(r'\.png|.jpg', '', text)


def remove_punctuation(text):
    text2 = re.sub(r'[^\w\s]', '', text)
    return text2


def safe_name(text):
    # replace spaces with -
    text = re.sub(r'\W+', '-', text)
    text = text.lower()
    text = re.sub(r'^-', '', text)  # remove leading -
    text = re.sub(r'--', '-', text)  # remove duplicate -
    return text


def remove_common(text):
    common = [
        'high resolution',
        'photograph',
        'photo',
        'color ',
        'paparazzi',
        'drawing',
        'painting',
        'in the style of',
        'by ',
        'of ',
        'on ',
        'in ',
        'by ',
        'an ',  # before a
        ' a ',
        '^a',
        'and ',
        # ' a ', # removes too many a and space
        'the ',
    ]
    text = text.lower()
    for word in common:
        rex = re.compile(word, re.IGNORECASE)
        text = rex.sub(' ', text)
        text = re.sub(r'\s\s+', ' ', text)
    # two or more spaces
    return text


def min_dir_name(input):
    # minimal directory name
    text = input.lower()
    text = remove_punctuation(text)
    text = remove_common(text)
    parts = text.split(' ')[0:5]
    dir_name = '-'.join(parts)
    dir_name = safe_name(dir_name)
    print('\ninput\t', input, '\ntext:\t', text, '\nname:\t', dir_name)
    return dir_name
