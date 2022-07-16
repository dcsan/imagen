from utils.ImageGen import generate
import replicate

drawers = [
    'vqgan',
    # 'pixel',
    # 'vdiff',
    # 'fft',
    # 'fast_pixel',
    # 'line_sketch',
    # 'clipdraw',
]


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
        generate(text, model)


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

            generate(t, model, options={'source': source}, meta=meta)


def multi():
    model = replicate.models.get("pixray/text2image")
    version = model.versions.list()[0]
    print('model', model)
    print('using model version:', version.id)
    # print('schema', version.openapi_schema)

    logpage = LogPage('multi.html')

    targets = [
        '',
        'kylie.png',
        'vgirl.png',
        'kguy-1.png',
        'kgirl-1.png',
        'katy.png',
        'clothes-1.png',
        'logotype.png',
        'no-makeup.png',

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
        'The girl has one hand on her hip as she admires herself in the mirror. She has on a pink dress and she looks very pretty. She is trying on makeup and she looks very excited about it.',
        'beautiful girl make up',
        'beautiful girl make up photograph',
        'beautiful girl make up photograph vogue',
        'beautiful girl make up photograph richard avedon',
        'beautiful girl make up photograph annie leibowitz',
        'beautiful girl make up photograph in style of manray',
        'beautiful girl make up photograph by manray',
        'beautiful girl trying on make up photograph detail vogue',
        'beautiful girl selling makeup on instagram photograph',
        'beautiful girl selling makeup on instagram photograph extreme detail narrow depth of field',
        'partying at a wild nightclub',
        'partying at a wild nightclub photograph',
        'a group of friends partying at a crowded nightclub with balloons and lights in the background photograph',
        'a group of friends partying at a crowded nightclub with balloons and lights in the background photograph portrait',
        'a boy skateboarding and jumping in the air photograph',
        'drinking cocktails at a bar with a beautiful sunset',
        'two cute dogs',
        'eating pizza on the moon',
        'a man sky diving and drinking a cocktail photograph',
        'a cyberpunk pirate'
    ]

    logpage.line('starting')

    for target in targets:
        for text in texts:
            logpage.line(f"<h1>{text}</h1>")
            style_url = ''
            options = {
                'aspect': 'square',
                # 'custom_loss': 'aesthetic',
                'quality': 'best',
                # 'size': [128, 128],
                'size': [256, 256],
                'iterations': 60,
            }
            meta = {
                'use_cache': True,
                'tags': 'style-none',
                'drawer': 'vqgan'
            }
            if target:
                style_url = image_url(target)
                options = options | {
                    'target_images': style_url,
                }
                meta = meta | {
                    'tags': f'_style-{sane(target)}',
                }

            logpage.line(f"text: {text} ")
            logpage.line(f'meta: <pre>{meta}</pre>')
            logpage.line(f'options: <pre>{options}</pre>')
            render = generate(f"{text}", model, options, meta)
            fname = render.get('fname')
            duration = render.get('duration')
            startup = render.get('startup')
            rendering = render.get('rendering')
            logpage.line(f'startup: {startup}')
            logpage.line(f'rendering: {rendering}')
            logpage.line(f'duration: {duration}')
            logpage.line(f"<img src='{fname}' />")
            logpage.line(f"style: {target} ")
            if style_url:
                logpage.line(
                    f'<img src="{style_url}" height="250px" width="250px" />')
            logpage.line('<hr/>')

            print(f'\trendered one: output/renders/{rendering}')

    logpage.line('done')
    logpage.close()


def ldif():
    # https://replicate.com/nicholascelestin/latent-diffusion
    model_path = 'nicholascelestin/latent-diffusion'
    model = replicate.models.get(model_path)
    version = model.versions.list()[0]
    print('model', model)
    print('using model version:', version.id)
    print('schema', version.openapi_schema)
    texts = [
        'An octopus riding a bicycle',
        'beautiful girl make up',
    ]
    for text in texts:
        render = generate(f"{text}", model)
        fname = render.get('fname')
        duration = render.get('duration')
        startup = render.get('startup')
        rendering = render.get('rendering')
