# https://replicate.com/nicholascelestin/latent-diffusion/examples

import os
import time
import replicate
from utils.ErrorUtils import get_traceback
from utils.FileUtils import fetch_image, ensure_dir
from utils.MiscUtils import flatten, unroll
from utils.TextUtils import min_dir_name
from pprint import pp

verbose = False


def single(prompt, config, retries=0):
    if config.get('skip'):
        print('skipping', prompt, config.get('name'))
        return

    if render_exists(prompt, config):
        print('render exists', prompt, config.get('name'))
        return

    print('single:', config)

    try:
        print('predicting:', prompt)
        prediction = make_prediction(prompt, config)
        print('dumping', prompt)
        dump_images(prediction, prompt, config)
    except Exception as e:
        print('exception: on prompt:', prompt)
        print('exception: ', get_traceback(e))
        retries += 1
        if retries < 5:
            delay = 5 * retries
            print('retrying in', delay, 'seconds')
            time.sleep(delay)
            single(prompt, config, retries)
        else:
            print('ERROR giving up', prompt)
            # raise e


def render_exists(prompt, config):
    image_prefix = config['params']['image_prefix']
    count = 1
    min_path = min_dir_name(prompt)
    render_path = f'output/renders/{min_path}'
    fname = f'{image_prefix}-{count}.png'
    fpath = f'{render_path}/{fname}'
    test = os.path.exists(fpath)
    print('render exists', test, fpath)
    return test


def make_prediction(prompt, config):
    model_path = config['params']['model_path']
    if not model_path:
        print('no model path')
        return

    model = replicate.models.get(model_path)

    model_options = config['model']

    input = {
        'prompt': prompt,
    } | model_options
    print('input', input)

    prediction = replicate.predictions.create(
        version=model.versions.list()[0],
        input=input,
    )

    print('status:', prediction.status)
    if verbose:
        pp(dict(prediction))
    print('waiting:', prompt)
    prediction.wait()
    print('done')
    return prediction


def dump_images(prediction, prompt, config):
    image_prefix = config['params']['image_prefix']
    count = 0
    min_path = min_dir_name(prompt)
    render_path = f'output/renders/{min_path}'
    ensure_dir(render_path)

    print('\nprediction.output', prediction.output)
    output = unroll(prediction.output)  # sometimes we get a list of lists

    for item in output:
        print('single output', item)
        count += 1
        # fname = safe_name(fname)
        # fname = f'{prompt}_{count}.png'
        fname = f'{image_prefix}-{count}.png'
        fpath = f'{render_path}/{fname}'
        fetch_image(item, fpath)
        print(f' {count} rendered {fpath}')
