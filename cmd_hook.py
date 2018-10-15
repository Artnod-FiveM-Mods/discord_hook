#!/usr/bin/python3
#-*- coding: utf-8 -*-
'''
Created on 13 jun. 2018

@author: artnod
'''
import sys, logging, logging.handlers
from Webhook.Webhook import Simplehook
from settings import LOG_CONF, ENABLE_HOOK, TOPHOOK, REBOOT15, REBOOT10, REBOOT5

# Set up a specific logger with our desired output level
my_logger = logging.getLogger('cmd_hook')
my_logger.setLevel(logging.DEBUG)
# create file handler which logs even debug messages
fhandler = logging.handlers.RotatingFileHandler(
    '{}discord_hook.log'.format(LOG_CONF['log_dir']), 
    maxBytes = LOG_CONF['max_bytes'], 
    backupCount = LOG_CONF['backup_count']
)
fhandler.setLevel(logging.INFO)
# create console handler with a higher log level
chandler = logging.StreamHandler()
chandler.setLevel(logging.DEBUG)
# create formatter and add it to the handler
formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
fhandler.setFormatter(formatter)
chandler.setFormatter(formatter)
# add the handler to logger
my_logger.addHandler(fhandler)
my_logger.addHandler(chandler)

if __name__ == '__main__':
    my_logger.info('Start Command Hook')
    if len(sys.argv) > 1:
        myargrs = sys.argv[1:]
        for myarg in myargrs:
            if myarg in ENABLE_HOOK:
                my_logger.info('Send message {}'.format(myarg))
                message = Simplehook(vars()[myarg])
                message.sendMessage()
            else:
                my_logger.warn('Webhook {} not enable!'.format(myarg))
    else:
        my_logger.warn('Webhook not found!')