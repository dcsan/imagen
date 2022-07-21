import re


def remove_suffix(text):
    return re.sub(r'\.png|.jpg', '', text)


def remove_punctuation(text):
    text2 = re.sub(r'[^\w\s]', '', text)
    return text2


def clean_text(text):
    text = remove_punctuation(text)
    text = text.lower()
    return text


def safe_name(text):
    # replace spaces with -
    text = re.sub(r'\W+', '-', text)
    text = text.lower()
    text = re.sub(r'^-', '', text)  # remove leading -
    text = re.sub(r'--', '-', text)  # remove duplicate -
    return text


def remove_common(text):
    common = [
        'a',
        'an',  # before a
        'at',  # before a
        'and',
        'by',
        'color',
        'drawing',
        'high',
        'resolution',
        'in',
        'in the style of',
        'of',
        'for',
        'on',
        'or',
        'establishing',
        'shot',
        'painting',
        'paparazzi',
        'photo',
        'photograph',
        'the',
        'still',
        'insanely',
        'detailed',
        'that',
        'is',

        # '(\b|^)the\b',
        # '(\b|^)by\b',
        # '(\b|^)of',
        # '(\b|^)on',
        # '(\b|^)in',
        # '(\b|^)an',  # before a
        # '(\b|^)and',
        # # ' a', # removes too many a and space
        # '(\b|^)the',
        # '(\b|^)a\b',
        # '(\b|^)a\b',
        # '^a',  # the line above _should_ get this but it doesnt :(
    ]
    text = clean_text(text)
    text_words = text.split(' ')
    text = [word for word in text_words if word not in common]
    # for word in common:
    #     for out in text:
    #         if
    # rex = re.compile(word, re.IGNORECASE)
    # text = rex.sub(' ', text)
    # text = re.sub(r'\s\s+', ' ', text)
    # two or more spaces
    return ' '.join(text)


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
