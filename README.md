# imagen
image generator

using replicate API
https://replicate.com/docs/api/getting-started-public

# Models:
various text2image modeals

-  Pixray
https://replicate.com/pixray/text2image

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

Have a look at the `runner.py` to see what will be run.


# Docs

settings:
https://dazhizhong.gitbook.io/pixray-docs/docs/primary-settings

<img src='docs/pixray-options.jpg' />

artstyles:

https://bardotbrush.com/30-art-styles-to-try-in-procreate/

