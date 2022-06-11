import re
import datetime
import time
import replicate
from async_wrap_iter import async_wrap_iter
import asyncio
import pprint
from utils.PageBox import PageBox

from utils.image_utils import fetch_image, file_exists, image_url, sane

pp = pprint.PrettyPrinter(indent=4)


def main():
    model = replicate.models.get("dribnet/pixray-vqgan")
    # pred = model.predict(prompts="rainbow mountain")
    prediction = replicate.predictions.create(
        version=model.versions.list()[0],
        input={
            "prompt": "Watercolor painting of an underwater submarine"
        }
    )

    print(prediction)
    print('status:', prediction.status)
    print(dict(prediction))
    print('waiting')
    prediction.wait()
    print('done')
    print('output', prediction.output)


def runner(prompts, model, options={}, meta={'use_cache': True}) -> str:
    drawers = [
        'vqgan',
        # 'pixel',
        # 'vdiff',
        # 'fft',
        # 'fast_pixel',
        # 'line_sketch',
        # 'clipdraw',
    ]
    drawer = drawers[0]

    quality = ['draft', 'normal', 'better', 'best'][3]
    aspect = ['square', 'portrait', 'widescreen'][0]
    size = [256, 256]
    iterations = 80

    name = re.sub(r'\W+', '-', prompts)
    fname = f"{name}_{drawer}_{quality}_{meta['tags']}.png"
    if file_exists(fname) and meta.get('use_cache'):
        print(f"{fname} already exists")
        return fname
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

    start = time.time()
    for image in model.predict(
        prompts=prompts,
        drawer=drawer,
        settings=settings,
    ):
        duration = time.time() - start
        last = image
        print(round(duration), image)

    fetch_image(last, fname)
    print('prompts:', prompts)
    print('duration:', round(duration))
    print(f"saved to {fname}")
    print('drawer:', drawer)
    print('\nfinal > ', last, '\n')
    return last


def timestamp():
    now = datetime.datetime.now()
    print(now.strftime("%Y-%m-%d %H:%M:%S"))


def show_list():
    items = replicate.predictions.list()
    for item in items:
        elem = replicate.predictions.get(item.id)
        pp.pprint(dict(elem))
        # pp.pprint(elem.output)
        # print(elem.urls, )


# async def waiter():
#     await runner("rainbows and unicorns nightmare")

def singles():
    texts = [
        'drinking cocktails at a bar with beautiful sunset',
        'two cute dogs',
        'partying at a wild nightclub',
    ]
    model = replicate.models.get("pixray/text2image")

    for text in texts:
        runner(text, model)


def filter_images():
    sources = [
        # sources
        '',
        'dogs.png',
        'dude-car.png',
        'katy.png',
    ]
    text = [
        'in the style of Andy Warhol'
    ]
    model = replicate.models.get("pixray/text2image")

    for source in sources:

        for t in text:
            options = {
                # 'target_images': image,
                'init_image': image_url(source),
                # 'target_images': style_url,
            }

            meta = {
                'use_cache': True,
                'tags': f'init-{sane(source)}',
            }

            runner(t, model, options={'source': source}, meta=meta)


def multi():
    model = replicate.models.get("pixray/text2image")
    version = model.versions.list()[0]
    print('model', model)
    print('using model version:', version.id)

    logpage = PageBox()

    # print('schema', version.openapi_schema)
    # for k, v in version:
    #     print('\n-----', k, v)

    # pp.pprint(version.openapi_schema)

    # pp.pprint(model)
    # pp.pprint(dict(model))
    # model = replicate.models.get("pixray/api")
    # runner("cyberpunk pirate", model)
    # runner("a clown playing cards in a smoky room | film noir", model)
    # runner("a circus clown playing poker in a smoky room | anime", model)
    # runner("spiders coming out of a teddy bear's eyes", model)
    # runner("astronaut on mars | video glitch #artstation", model)
    # runner("astronaut on mars | video glitch #anime", model)
    # runner("ducks by the pond in an english country town #artstation", model)
    # runner("a court jester juggling for the queen | seurat", model)
    # runner("a court jester juggling for the queen | picasso", model)
    # text = 'a court jester juggling for the queen'
    # text = 'a ginger cat lost in a sci fi city in the rain Japanese print'

    targets = [
        '',
        'art-nouveau.png',
        'const-1.jpg',
        'papercut.jpg',
        'fairey.jpg',
        'popart.png',

        # 'clown-sticker-1.png',
        'jester-1-256.jpg',
        # 'jester-1.jpg',
        # 'jester-2.jpg',
        'joker-card-1.jpg',
        # 'joker-card-3.jpg',
        # 'scary-clown-1.jpg',
        # 'scary-clown-2.jpg',
        'scary-clown-3.jpg',

        # backgrounds / filter effects
        'cocktail-fire.png',
        'steampunk.jpg',
        'cyberpunk.jpg',
        'sunset.jpg',

        # 'const-2.jpg',

    ]

    # sources = [
    #     # sources
    #     '',
    #     'dogs.png',
    #     'dude-car.png',
    #     'katy.png',
    #     'kgirl-1.png',
    #     'kguy-1.png',
    #     'kguy-2.png',
    #     'kylie.png',
    #     'minaj-1.png',
    #     'nails.png',
    #     'no-makeup.png',
    #     'paris-girl.png',
    #     'vgirl.png',
    # ]

    texts = [
        'drinking cocktails at a bar with a beautiful sunset',
        'two cute dogs',
        'partying at a wild nightclub',
        'beautiful girl trying on make up',
        'a boy skateboarding and jumping in the air',
        'eating pizza on the moon',
        'sky diving and drinking a cocktail',
    ]

    logpage.add('starting')

    for text in texts:
        for target in targets:
            if target:
                style_url = image_url(target)

                options = {
                    'target_images': style_url,
                }

                meta = {
                    'use_cache': True,
                    'tags': f'_style-{sane(target)}',
                }
            else:
                options = {}
                meta = {
                    'use_cache': True,
                    'tags': '_style-none',
                }

            logpage.add(f"text: {text} ")
            logpage.add(f"style: {target} ")
            last = runner(f"{text}", model, options, meta)
            logpage.add(f"<img src='{last}' />")
            logpage.add('<hr/>')

    logpage.add('done')
    logpage.close()


# main()
# show_list()
# runner("rainbows and unicorns nightmare")
# asyncio.run(waiter())
multi()
