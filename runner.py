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
    "rainbows and unicorns nightmare",
    'An octopus riding a unicorn',
    'A pretty girl putting on makeup',
]

for text in lines:
    single(text, batch_size=3)
