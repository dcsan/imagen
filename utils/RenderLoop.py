import time
import replicate
from pprint import pp
from utils.TextUtils import min_dir_name
from utils.LatDif import single
from utils.LogPage import LogPage

from data.configs import configs
from data.prompts import storylines


def render_many(lines=[]):

    start = time.time()

    for config in configs:
        if not config.get('active'):
            print('skipping', config.get('name'))
            continue

        for prompt in lines:
            print('\n\n------ prompt:', prompt)

            print('\n---- name:', config.get('name'))
            print('\n---- config:', config)
            min_dir_name(prompt)
            single(prompt, config)
            pp(config)
            print('\n')

    print('done full duration', time.time() - start)
