import sys
import logging
import config
from logging.config import dictConfig

logging_config = dict(
    version=1,
    formatters={
        'verbose': {
            'format': ("[%(asctime)s.%(msecs)03d %(process)d ] %(levelname)s "
                       "[%(name)s:%(filename)s:%(funcName)s:%(lineno)s] %(message)s"),
            'datefmt': "%d/%b/%Y %H:%M:%S",
        },
        'simple': {
            'format': '%(levelname)s %(message)s',
        },
    },
    handlers={
        'api-logger': {'class': 'logging.handlers.RotatingFileHandler',
                       'formatter': 'verbose',
                       'level': logging.DEBUG,
                       'filename': config.common_folder_path + 'logs/ui_automation.log',
                       'maxBytes': 52428800,
                       'backupCount': 7},
        'batch-process-logger': {'class': 'logging.handlers.RotatingFileHandler',
                                 'formatter': 'verbose',
                                 'level': logging.DEBUG,
                                 'filename': config.common_folder_path + 'logs/batch.log',
                                 'maxBytes': 52428800,
                                 'backupCount': 7},
        'console': {
            'class': 'logging.StreamHandler',
            'level': 'DEBUG',
            'formatter': 'simple',
            'stream': sys.stdout,
        },
    },
    loggers={
        'api_logger': {
            'handlers': ['api-logger', 'console'],
            'level': logging.DEBUG
        },
        'batch_process_logger': {
            'handlers': ['batch-process-logger', 'console'],
            'level': logging.DEBUG
        }
    }
)

dictConfig(logging_config)

api_logger = logging.getLogger('api_logger')
batch_process_logger = logging.getLogger('batch_process_logger')
