# imagen
image generator using various Text2Image models

The goal is to compare across a range of different prompt types:
- made up - 'panda riding a bicycle'
- artistic - detailed prompts with styles
- concepts - 'how does a panic attack feel'
- style transfer - xx in style of Warhol
- photos, drawings, illustrations, diagrams
- other types of imaginative prompts

Often using replicate API
https://replicate.com/docs/api/getting-started-public

- See list of models in [data/configs.py](./data/configs.py)
- Renders get saved into [output/renders](./output/renders)
- Markdown gallery like [this one](./gallery-3.md)

# Setup

get an API key from replicate and export it
https://replicate.com/docs/api/getting-started-public

for example

`cp .env.example .env`

edit the `.env` file to add your key then

`source .env`

```bash
# first time: install virtual env:
python3 -m venv venv

# activate venv
source venv/bin/activate

# install pip modules
pip install -r requirements.txt

```

# Running

`make run`

This will execute the `run` command inside the [Makefile](./Makefile)

Depending on what's configured, it should output images into `renders/`

Have a look at the `cli.py` to see what commands are available.

# Output

Renders get saved into [output/renders](./output/renders)

Another command makes a markdown gallery like [this one](./gallery-3.md)

Full link to anchor example:

https://github.com/dcsan/imagen/blob/main/gallery-3.md#octopus-riding-skateboard-22826850

# References

settings:
https://dazhizhong.gitbook.io/pixray-docs/docs/primary-settings

<img src='docs/pixray-options.jpg' />

## artstyles:

https://bardotbrush.com/30-art-styles-to-try-in-procreate/

