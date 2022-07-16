import datetime
import replicate
from pprint import pp
from utils.TextUtils import min_dir_name
from utils.LatDif import single
from utils.LogPage import LogPage

from data.prompts import lines
from data.configs import configs


def main():
    for prompt in lines:
        print('\n\n------ prompt:', prompt)

        for config in configs:
            print('config:')
            pp(config)
            min_dir_name(prompt)
            single(prompt, config)
            print('\n')
        print('\n')


main()
