configs = [

    {
        'name': 'midjourney',
        'skip': True,   # dont render
        'model': {
            'batch_size': 9,
            'width': 256,
            'height': 256,
        },
        'params': {
            'model_path': None,
            'image_prefix': 'midj'
        }
    },

    {
        'name': 'simulacra',
        'skip': True,   # dont render
        'model': {
            'n_predictions': 3,
            'drawer': 'vqgan',
            'settings': {
                'size': [256, 256]
            }
        },
        'params': {
            'model_path': 'dribnet/pixray-vqgan',
            'image_prefix': 'simu'
        },
    },

    {
        'name': 'disco-diffusion',
        'skip': False,   # dont render
        'model': {
            'batch_size': 5,
            'width': 256,
            'height': 256,
            'steps': 250,
            'display_rate': 250,
            'diffusion_model': '256x256_diffusion_uncond',
        },
        'params': {
            'model_path': 'nightmareai/disco-diffusion',
            'image_prefix': 'disco'
        }
    },

    {
        'name': 'pixray-vqgan',
        'skip': True,   # dont render
        'model': {
            'n_predictions': 3,
            'drawer': 'vqgan',
            'settings': {
                'size': [256, 256]
            }
        },
        'params': {
            'model_path': 'dribnet/pixray-vqgan',
            'image_prefix': 'pixray'
        },
    },

    {
        'name': 'glid3',
        'skip': True,   # dont render
        # passed to model
        'model': {
            'seed': 1,  # fixed seed
            'batch_size': 9,
            'width': 256,
            'height': 256,
            'guidance_scale': 5,
            'aesthetic_rating': 9,
            'aesthetic_weight': 0.9,
        },
        # used internally
        'params': {
            'model_path': 'afiaka87/glid-3-xl',
            'image_prefix': 'glid3',
        }
    },

    {
        'name': 'latdif',
        'skip': True,   # dont render
        'model': {
            'batch_size': 9,
            'width': 256,
            'height': 256,
        },
        'params': {
            'model_path': 'nicholascelestin/latent-diffusion',
            'image_prefix': 'ldif'
        }
    },

    # seems to bring down replicate frequently
    {
        'name': 'dalle-mini',
        'skip': True,   # dont render
        'model': {
            'n_predictions': 9,
        },
        'params': {
            'model_path': 'borisdayma/dalle-mini',
            'image_prefix': 'dmin'
        },
    },

    {
        'name': 'openai-dalle-2',
        'skip': True,   # dont render
        'model': {
            'n_predictions': 3,
            'drawer': 'vqgan',
            'settings': {
                'size': [256, 256]
            }
        },
        'params': {
            'image_prefix': 'opai-dalle'
        },
    },

]
