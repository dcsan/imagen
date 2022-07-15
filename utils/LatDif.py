# https://replicate.com/nicholascelestin/latent-diffusion/examples

import replicate
from utils.FileUtils import ensure_dir, min_dir_name
from utils.ImageUtils import fetch_image, remove_suffix, safe_name


model_path = 'nicholascelestin/latent-diffusion'


# TODO - wrap in a retry block

def single(prompt, batch_size=1, width=256, height=256):
    model = replicate.models.get(model_path)
    # pred = model.predict(prompts="rainbow mountain")
    prediction = replicate.predictions.create(
        version=model.versions.list()[0],
        input={
            "prompt": prompt,
            'batch_size': batch_size,
            'width': width,
            'height': height,
        }
    )

    print('status:', prediction.status)
    print(dict(prediction))
    print('\nwaiting')
    prediction.wait()
    print('done')
    print('output', prediction.output)

    min_path = min_dir_name(prompt)
    render_path = f'renders/{min_path}'
    ensure_dir(render_path)

    count = 0
    for image in prediction.output:
        count += 1
        # fname = safe_name(fname)
        # fname = f'{prompt}_{count}.png'
        fname = f'ldif-{count}.png'
        fpath = f'{render_path}/{fname}'
        fetch_image(image, fpath)
        print(f' {count} rendered {fpath}')
