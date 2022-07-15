import datetime
import replicate
from pprint import pp
from utils.LatDif import single
from utils.LogPage import LogPage

from utils.ImageUtils import image_url, remove_suffix

# model_path = "dribnet/pixray-vqgan"
model_path = 'nicholascelestin/latent-diffusion'


# main()
# show_list()
# runner("rainbows and unicorns nightmare")
# asyncio.run(waiter())
# multi()

# ldif()

lines = [
    # "rainbows and unicorns nightmare",
    # 'An octopus riding a unicorn',
    # 'A pretty girl putting on makeup',
    # 'a realistic beautiful woman, night time, wavy hairstyle, white hair, character concept art, created by Ross Tran, intricate accurate details, artstation trending, octane render, cinematic color grading, muted colors, soft light, cinematic, 8K',
    'a realistic beautiful woman, night time, wavy hairstyle, white hair, concept art',
    'A high resolution photo of a rainy Tokyo street scene at night with lots of neon lights reflections',
    'Time travelers',
    'Two ships passing in the night',
    'photograph of a panda riding a bicycle'
]

for text in lines:
    single(text, batch_size=1)
