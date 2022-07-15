import datetime
import replicate
from pprint import pp
from utils.TextUtils import min_dir_name
from utils.LatDif import single
from utils.LogPage import LogPage


# model_path = "dribnet/pixray-vqgan"
model_path = 'nicholascelestin/latent-diffusion'


# main()
# show_list()
# runner("rainbows and unicorns nightmare")
# asyncio.run(waiter())
# multi()

# ldif()

lines = [
    'A panda riding a bicyle',
    'A pretty girl putting on makeup',
    "rainbows and unicorns nightmare",
    'An octopus riding a skateboard',
    'a realistic beautiful woman, night time, wavy hairstyle, white hair, character concept art, created by Ross Tran, intricate accurate details, artstation trending, octane render, cinematic color grading, muted colors, soft light, cinematic, 8K',
    # 'a realistic beautiful woman, night time, wavy hairstyle, white hair, concept art',
    'A high resolution photo of a rainy Tokyo street scene at night with lots of neon lights reflections',
    'Time travelers',
    'Two ships passing in the night',
    'photograph of a panda riding a bicycle',
    'The definition of beauty',
    'A high resolution photo of a girl putting make up on in the mirror looking at herself',
    'A color paparazzi photo of Mick Jagger eating a hamburger national inquirer cover',
    "establishing shot: the criminal's lair, laid deep in the mountains, shot from above from a helicopter. bats are flying out of the windows. dark and foggy background. dusky sky approaching sunset",
    "a still of Kermit the Frog in Mad Max Fury Road",
    "Muppets in Mad Max Fury Road",
    "A huge octopus climbing up the Empire State building",
    "an octopus riding a skateboard",
    "photograph of a panda riding a bicycle",
    "Ghostbusters inside a glass jar, insanely detailed, epic lighting, cinematic composition, hyperrealistic, 8k render",
    "a new type of fish discovered in the deepest darkest sea, neon lighting vivid saturated palette",
    "For sale baby shoes, never worn    ",
    "It was a dark and stormy night",
    "a paparazzi photograph of Jesus going into a nightclub. Flash photography, blurred people",
    "an invention for keeping everyone happy",
    "how a panic attack feels",
    "calm, psychedelic",
    "The court jester cyberpunk playing card illustration",
    "noah's ark painting by picasso",
    "noah's ark painting by Jack Kirby",
    "Cubist Art, create a painting or sculpture that is abstract and geometric in style. The work should be composed of basic shapes and have aflat, two-dimensional appearance. The colors should be bold and primary colors.",
]


# model_path = 'nicholascelestin/latent-diffusion'

# passed to model
config = {
    'model': {
        'n_predictions': 3,
    },
    'params': {
        'model_path': 'borisdayma/dalle-mini',
        'image_prefix': 'dmin'
    }
}

# batch_size=3, width=size, height=size
# internal

# TODO - wrap in a retry block
for text in lines:
    # min_dir_name(text)
    single(text, config)
