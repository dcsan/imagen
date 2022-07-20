from data.prompts import lines
from data.configs import configs
from utils.FileUtils import ensure_dir
from utils.TextUtils import min_dir_name, safe_name
from utils.presenter.MdPage import MdPage
from os.path import exists


def add_models(dump):
    dump.line('\n## Models \n')
    for config in configs:
        algo = config['name']
        model_path = config['params'].get('model_path')
        if model_path is None:
            dump.line(f'- {algo}')
        else:
            model_url = f'https://replicate.com/{model_path}'
            dump.line(f'- [{algo}](#{model_url}')


def add_prompt_list(dump):
    dump.line('\n## Prompts\n')
    for prompt in lines:
        link = min_dir_name(prompt)
        dump.line(f'1. [{link}](#{link})')


def create_readme():
    max_pix = 6
    size = 150
    filename = f'output-{max_pix}.md'

    dump = MdPage(filename)
    dump.line('# Preview')
    add_models(dump)
    add_prompt_list(dump)

    for prompt in lines:
        # big prompt
        link = min_dir_name(prompt)

        dump.line(f'\n## {link} ')
        dump.line(f'> [{prompt}]\n')
        # fpath = f'{min_dir_name(prompt)}'

        min_path = min_dir_name(prompt)
        # relative to app
        render_path = f'output/renders/{min_path}'
        ensure_dir(render_path)

        for config in configs:
            algo = config['name']
            # algo
            dump.line(f'\n\n{algo}\n')
            # anchor tag
            # dump.line(f'[{prompt}](#{link})')
            # eg 'simu' or 'glid'
            image_prefix = config["params"]["image_prefix"]
            for count in range(1, max_pix+1):
                image_path = f'{render_path}/{image_prefix}-{count}.png'
                file_exists = exists(image_path)
                if file_exists:
                    # image = f'{config["params"]["image_prefix"]}-{count}.png'
                    # dump.line(f'![img_{count}]({fpath}/{image}) ')
                    image_tag = f'<img alt="{link}" src="{image_path}" width="{size}px" />'
                    image_link = f'<a href="{image_path}">{image_tag}</a>'
                    dump.line(image_link)  # cannot have newlines
                else:
                    # dump.line(f'\n> no file: algo: {algo} / {image_path}\n')
                    dump.line(f'[end]')
                    break

    dump.close()


create_readme()
