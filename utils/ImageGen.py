import pprint
import re
import time

from utils.FileUtils import fetch_image, file_exists

pp = pprint.PrettyPrinter(indent=4)


def generate(prompts, model, options={}, meta={'use_cache': True}):
    drawer = meta.get('drawer') or 'vqgan'

    quality = ['draft', 'normal', 'better', 'best'][3]
    aspect = ['square', 'portrait', 'widescreen'][0]
    size = meta.get('size') or [256, 256]
    iterations = meta.get('iterations') or 80

    name = prompts[0:40] + str(len(prompts))
    name = re.sub(r'\W+', '-', name)
    tags = meta.get('tags') or ''
    fname = f"{name}_{drawer}_{quality}_{tags}.png"
    if file_exists(fname) and meta.get('use_cache'):
        print(f"{fname} already exists")
        return {
            'fname': fname,
            'duration': 0,
        }
    else:
        print(f'rendering {fname}')

    settings = {
        # "prompts": prompts,
        # "drawer": drawer,
        "iterations": iterations,
        "aspect": aspect,
        "size": size,
        "quality": quality,
        # 'vqgan_model': 'wikiart_16384',
        'custom_loss': 'aesthetic',
    }
    settings = {**settings, **options}
    print('drawer:', drawer)
    print('settings:')
    pp.pprint(settings)
    last = ""

    print('prompts:', prompts)

    start = round(time.time())
    startup = 0
    for image in model.predict(
        prompts=prompts,
        drawer=drawer,
        settings=settings,
    ):
        duration = round(time.time() - start)
        if startup == 0:
            startup = duration
        last = image
        print(duration, image)

    fetch_image(last, fname)
    print('prompts:', prompts)
    print('duration:', round(duration))
    print(f"saved to {fname}")
    print('drawer:', drawer)
    print('\nfinal > ', last, '\n')
    return {
        'fname': fname,
        'startup': startup,
        'rendering': duration - startup,
        'duration': duration,
    }
