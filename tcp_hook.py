#!/usr/bin/python3
#-*- coding: utf-8 -*-
'''
Created on 15 oct. 2018

@author: artnod
'''

import time, logging, logging.handlers
import win32serviceutil, win32service, win32event, servicemanager
from Webhook.Webhook import CheckPorthook
from settings import WEBHOOK_CONF, FIVEM_CONF, LOG_CONF

class AppServerSvc (win32serviceutil.ServiceFramework):  
    _svc_name_ = "Python TCP Checker"
    _svc_display_name_ = "PythonTCPChecker"

    def __init__(self,args):
        win32serviceutil.ServiceFramework.__init__(self,args)
        self.hWaitStop = win32event.CreateEvent(None,0,0,None)
        # Set up a specific logger with our desired output level
        self.my_logger = logging.getLogger('discord_hook')
        self.my_logger.setLevel(logging.DEBUG)
        # create file handler which logs even debug messages
        self.fhandler = logging.handlers.RotatingFileHandler(
            '{}tcp_hook.log'.format(LOG_CONF['log_dir']), 
            maxBytes = LOG_CONF['max_bytes'], 
            backupCount = LOG_CONF['backup_count']
        )
        self.fhandler.setLevel(logging.INFO)
        # create console handler with a higher log level
        self.chandler = logging.StreamHandler()
        self.chandler.setLevel(logging.DEBUG)
        # create formatter and add it to the handler
        self.formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
        self.fhandler.setFormatter(self.formatter)
        self.chandler.setFormatter(self.formatter)
        # add the handler to logger
        self.my_logger.addHandler(self.fhandler)
        self.my_logger.addHandler(self.chandler)

    def SvcStop(self):
        self.ReportServiceStatus(win32service.SERVICE_STOP_PENDING)
        win32event.SetEvent(self.hWaitStop)

    def SvcDoRun(self):
        self.ReportServiceStatus(win32service.SERVICE_RUNNING)
        servicemanager.LogMsg(servicemanager.EVENTLOG_INFORMATION_TYPE, servicemanager.PYS_SERVICE_STARTED, (self._svc_name_,''))
        self.my_logger.info("Service Is Starting")
        self.main()

    def main(self):
        rc = None
        while rc != win32event.WAIT_OBJECT_0:
            instances = []
            instances.append(CheckPorthook(FIVEM_CONF['server_ip'], FIVEM_CONF['server_port'], FIVEM_CONF['server_name'], WEBHOOK_CONF['webhook_url']))
            while True:
                for instance in instances:
                    instance.process()
                time.sleep(FIVEM_CONF['check_delay'])
            rc = win32event.WaitForSingleObject(self.hWaitStop, (30 * 1000))

if __name__ == '__main__':  
    win32serviceutil.HandleCommandLine(AppServerSvc)