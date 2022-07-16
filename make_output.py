from data.prompts import lines
from data.configs import configs
from utils.FileUtils import ensure_dir
from utils.TextUtils import min_dir_name
from utils.presenter.MdPage import MdPage


def create_readme():
    dump = MdPage()
    output = '# Preview'
    for prompt in lines:
        dump.line(f'\n\n# {prompt} \n\n')
        fpath = f'{min_dir_name(prompt)}'

        min_path = min_dir_name(prompt)
        render_path = f'output/renders/{min_path}'
        ensure_dir(render_path)

        for config in configs:
            dump.line(f'\n\n### {config["name"]} \n')
            for count in range(1, 10):
                image = f'{config["params"]["image_prefix"]}-{count}.png'
                dump.line(f'\n![img_{count}]({fpath}/{image}) ')

    dump.close()


create_readme()
