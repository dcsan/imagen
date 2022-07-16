configs = [

    {
        'name': 'glid3',
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
        'name': 'dalle-mini',
        'model': {
            'n_predictions': 9,
        },
        'params': {
            'model_path': 'borisdayma/dalle-mini',
            'image_prefix': 'dmin'
        },
    },

    {
        'name': 'latdif',
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

    # {
    #     'name': 'pixray-vqgan',
    #     'model': {
    #         'n_predictions': 3,
    #         'drawer': 'vqgan',
    #         'settings': {
    #             'size': [256, 256]
    #         }
    #     },
    #     'params': {
    #         'model_path': 'dribnet/pixray-vqgan',
    #         'image_prefix': 'pixray'
    #     },
    # },

]
