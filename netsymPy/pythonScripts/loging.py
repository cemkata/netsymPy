from bottle import Bottle, request, response
import logging
from datetime import datetime



def log_to_access(fn):
    logger = logging.getLogger('myapp')

    # set up the logger
    logger.setLevel(logging.INFO)
    file_handler = logging.FileHandler('./log/access.log')
    #TODO
    #TimedRotatingFileHandler('access.log', 'd', 7)
    formatter = logging.Formatter('%(msg)s')
    file_handler.setLevel(logging.DEBUG)
    file_handler.setFormatter(formatter)
    logger.addHandler(file_handler)

    '''
    Wrap a Bottle request so that a log line is emitted after it's handled.
    (This decorator can be extended to take the desired logger as a param.)
    '''
    def _log_to_logger(*args, **kwargs):
        request_time = datetime.now()
        actual_response = fn(*args, **kwargs)
        # modify this to log exactly what you need:
        logger.info('%s %s %s %s %s' % (request.remote_addr,
                                        request_time,
                                        request.method,
                                        request.url,
                                        response.status))
        return actual_response
    return _log_to_logger

def configErrorsLogging(inStr, toExit=True):
    f = open('./log/starting.log', 'w')
    f.write(inStr+'\n')
    f.close()
    if toExit:
       exit(1)

__author__ = 'Most Wanted'


class LoggingPlugin(object):
    """
    Allows to write log for bottle applications
    """

    def __init__(self):
        #todo: add stream and format parameters
        self.app = None
        self.logger = None
        self.levels = {
            'debug': 50,
            'error': 40,
            'warning': 30,
            'critical': 20,
            'info': 10,
            'none': 0,
        }

    def setup(self, app, appname="myapp", logLevel = 'info'):
        self.app = app
        logger = logging.getLogger(__name__)
        logger.setLevel(logging.DEBUG)
        formatter = logging.Formatter('%(name)s:%(asctime)s:[%(levelname)s] %(message)s')
        formatter.datefmt = '%d/%m/%y %H:%M'
        #handler = logging.StreamHandler()
        handler = logging.FileHandler('./log/' + appname + '.log')
        handler.setFormatter(formatter)
        logger.addHandler(handler)
        self.logger = logger
        self.app.log = self.log
        self.logLevel = self.levels.get(logLevel)

    def log(self, msg, level=None):

        cur_level = self.levels.get(level, self.logLevel)
        if cur_level < self.logLevel:
           self.logger.log(cur_level, msg)

    def apply(self, callback, route):
        return callback



class EmptyLoggingPlugin(object):
    """
    Empty logging plugin
    """
    def __init__(self):
        pass

    def log(self, msg, level):
        pass

    def apply(self, callback, route):
        return callback
