#Import logging module
import logging

## Configure logger using basicConfig()
# level : Severity level
# filename : File to which the log message to be written
# filemode : Filename mode, the default is append
# format : log message format

logging.basicConfig(filename = "a1_logs.log",
                    format='%(asctime)s %(message)s',
                    level = logging.DEBUG,
                    filemode='a')

## various test messages
## debug --> info --> warning ---> error ---> critical
logging.debug('This is a debug message')
logging.info('This is an info message')
logging.warning('This is a warning message')
logging.error('This is an error message')
logging.critical('This is a critical message')
