#!/usr/bin/python3
#-*- coding: utf-8 -*-
'''
Created on 13 jun. 2018

@author: artnod
'''

### COMMON CONF ###
LOG_CONF = {
    'log_dir' : 'E:\\', # end with "/" or "\\"
    'max_bytes' : 5000000,
    'backup_count' : 5,
}

### TCP HOOK CONF ###
WEBHOOK_CONF = {
    'webhook_url' : 'https://discordapp.com/api/webhooks/470166603531550721/8qUC-Nd1XXCnuU4zh3QSTdjsujOE8CcLmbnr9OQouU_ohw8t5MmthOvRRodJaoTovKH3',
    'color' : 123123,
    'msg' : '@everyone',
    'message' : {
        'author' : 'Nono Le Petit Robot',
        'author_icon' : 'https://cdn.discordapp.com/icons/378553286627950602/a280e335f326716f64a2c9deda814863.png',
        'thumbnail_on' : 'https://i.pinimg.com/originals/23/4a/6b/234a6b9a897c7e963bf73ef073b94842.jpg',
        'thumbnail_off' : 'http://www.clker.com/cliparts/4/4/1/a/1195429270821624493molumen_multicolor_power_buttons_4.svg.hi.png',
        'footer' : 'https://gamehosting.co/templates/dev/img/games/fivem-fx/fivem-logo-320.png',
    }
}
FIVEM_CONF = {
    'server_name' : 'The Asylum RP',
    'server_ip'   : '5.39.58.1',
    'server_port' : 30120,
    'check_delay' : 5
}

### CMD HOOK CONF ###
ENABLE_HOOK = [
    'TOPHOOK', 'REBOOT15', 'REBOOT10', 'REBOOT5'
]
TOPHOOK = {
    'webhook_url' : 'https://discordapp.com/api/webhooks/470166603531550721/8qUC-Nd1XXCnuU4zh3QSTdjsujOE8CcLmbnr9OQouU_ohw8t5MmthOvRRodJaoTovKH3',
    'color' : 123123,
    'msg' : '@everyone',
    'message' : {
        'author' : {
            'name' : 'Nono Le Petit Robot',
            'icon' : 'https://cdn.discordapp.com/icons/378553286627950602/a280e335f326716f64a2c9deda814863.png',
        },
        'desc_text' : 'Vous souhaitez nous aider à nous faire connaitre et donc, voter pour le serveur ?',
        'fields' : [
            {
                'name' : 'C\'est possible ici une fois toutes les 2h. Merci à vous !',
                'value' : 'https://gta.top-serveurs.net/vote/the-asylum',
            },
        ],
        'thumbnail' : 'https://cdn.discordapp.com/icons/378553286627950602/a280e335f326716f64a2c9deda814863.png',
        'footer' : {
            'text' : 'The Asylum RP',
            'icon' : 'https://gamehosting.co/templates/dev/img/games/fivem-fx/fivem-logo-320.png',
        },
    },
}
REBOOT15 = {
    'webhook_url' : 'https://discordapp.com/api/webhooks/470166603531550721/8qUC-Nd1XXCnuU4zh3QSTdjsujOE8CcLmbnr9OQouU_ohw8t5MmthOvRRodJaoTovKH3',
    'color' : 16711680,
    'msg' : '@everyone',
    'message' : {
        'author' : {
            'name' : 'Nono Le Petit Robot',
            'icon' : 'https://cdn.discordapp.com/icons/378553286627950602/a280e335f326716f64a2c9deda814863.png',
        },
        'desc_text' : '**Alerte Météo**',
        'fields' : [
            {
                'name' : 'Un ouragan va s\'abattre sur Los Santos!',
                'value' : 'Tempête dans **15 minutes**!',
            },
        ],
        'thumbnail' : 'http://icons.iconarchive.com/icons/icons8/ios7/128/Weather-Storm-icon.png',
        'footer' : {
            'text' : 'The Asylum RP',
            'icon' : 'https://gamehosting.co/templates/dev/img/games/fivem-fx/fivem-logo-320.png',
        },
    },
}
REBOOT10 = {
    'webhook_url' : 'https://discordapp.com/api/webhooks/470166603531550721/8qUC-Nd1XXCnuU4zh3QSTdjsujOE8CcLmbnr9OQouU_ohw8t5MmthOvRRodJaoTovKH3',
    'color' : 16711680,
    'msg' : '@everyone',
    'message' : {
        'author' : {
            'name' : 'Nono Le Petit Robot',
            'icon' : 'https://cdn.discordapp.com/icons/378553286627950602/a280e335f326716f64a2c9deda814863.png',
        },
        'desc_text' : 'Alerte Météo',
        'fields' : [
            {
                'name' : 'Un ouragan va s\'abattre sur Los Santos!',
                'value' : 'Tempête dans **10 minutes**!',
            },
        ],
        'thumbnail' : 'http://icons.iconarchive.com/icons/icons8/ios7/128/Weather-Storm-icon.png',
        'footer' : {
            'text' : 'The Asylum RP',
            'icon' : 'https://gamehosting.co/templates/dev/img/games/fivem-fx/fivem-logo-320.png',
        },
    },
}
REBOOT5 = {
    'webhook_url' : 'https://discordapp.com/api/webhooks/470166603531550721/8qUC-Nd1XXCnuU4zh3QSTdjsujOE8CcLmbnr9OQouU_ohw8t5MmthOvRRodJaoTovKH3',
    'color' : 16711680,
    'msg' : '@everyone',
    'message' : {
        'author' : {
            'name' : 'Nono Le Petit Robot',
            'icon' : 'https://cdn.discordapp.com/icons/378553286627950602/a280e335f326716f64a2c9deda814863.png',
        },
        'desc_text' : 'Alerte Météo',
        'fields' : [
            {
                'name' : 'Un ouragan va s\'abattre sur Los Santos!',
                'value' : 'Tempête dans **5 minutes**!',
            },
        ],
        'thumbnail' : 'http://icons.iconarchive.com/icons/icons8/ios7/128/Weather-Storm-icon.png',
        'footer' : {
            'text' : 'The Asylum RP',
            'icon' : 'https://gamehosting.co/templates/dev/img/games/fivem-fx/fivem-logo-320.png',
        },
    },
}