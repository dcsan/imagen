import datetime
import replicate
from pprint import pp
from utils.TextUtils import min_dir_name
from utils.LatDif import single
from utils.LogPage import LogPage

from data.prompts import lines
from data.configs import configs


def main():

    for config in configs:
        if config.get('skip'):
            print('skipping', prompt, config.get('name'))
            continue

        for prompt in lines:
            print('\n\n------ prompt:', prompt)

            print('\n---- name:', config.get('name'))
            print('\n---- config:', config)
            min_dir_name(prompt)
            single(prompt, config)
            pp(config)
            print('\n')


main()
