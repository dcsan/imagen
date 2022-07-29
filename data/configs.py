
configs = [

    {
        'name': 'majdif',
        'active': True,
        'model': {
            'width': 384,
            'height': 384,
            'clip_scale': 16000,
            'latent_scale': 12,
            'model': 'finetuned',
            'output_steps': 0,

        },
        'params': {
            'model_path': 'nightmareai/majesty-diffusion',
            'image_prefix': 'mdif',
            'prompt_fields': [
                'clip_prompts',
                'latent_prompt',
            ]
        }
    },
    {
        'name': 'dalle-mini',
        'active': True,   # dont render
        'model': {
            'n_predictions': 3,
        },
        'params': {
            'model_path': 'borisdayma/dalle-mini',
            'image_prefix': 'dmin'
        },
    },

    {
        'name': 'disco-diffusion',
        'active': True,   # dont render
        'model': {
            'batch_size': 3,
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
        'name': 'latdif',
        'active': True,   # dont render
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

    {
        'name': 'midjourney',
        'active': False,   # dont render
        'params': {
            'model_path': None,
            'image_prefix': 'midj'
        }
    },

    {
        'name': 'stabAI-fast',
        'active': False,   # dont render
        'params': {
            'model_path': None,
            'image_prefix': 'stab'
        }
    },

    {
        'name': 'simulacra',
        'active': False,   # dont render
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
        'name': 'lmd',
        'active': False,   # dont render
        'model': {
            'batch_size': 9,
            'width': 256,
            'height': 256,
        },
        'params': {
            'image_prefix': 'lmdv16'
        }
    },

    {
        'name': 'pixray-vqgan',
        'active': False,   # dont render
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
        'active': False,   # dont render
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
        'name': 'openai-dalle-2',
        'active': False,   # dont render
        'model': {
            'n_predictions': 3,
            'drawer': 'vqgan',
            'settings': {
                'size': [256, 256]
            }
        },
        'params': {
            'image_prefix': 'dal2'
        },
    },

]
