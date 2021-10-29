import inspect
import logging
import logging.handlers as handlers


def custom_logger(loglevel=logging.DEBUG, file_name="book_search_test.log"):
    # Gets the name of the class / method from where this method is called
    logger_name = inspect.stack()[1][3]
    logger = logging.getLogger(logger_name)
    # By default, log all messages
    logger.setLevel(logging.DEBUG)

    file_handler = logging.FileHandler(file_name, mode='a')
    # file_handler = logging.FileHandler("{0}.log".format(logger_name),
    #                                                     mode='w')
    file_handler.setLevel(loglevel)

    formatter = logging.Formatter('%(asctime)s - ' +
                                  ' %(name)s - %(module)s - ' +
                                  '%(funcName)s - %(levelname)s: ' +
                                  '%(message)s',
                                  datefmt='%m/%d/%Y %I:%M:%S %p')
    logHandler = handlers.TimedRotatingFileHandler(file_name, when='M',
                                                   interval=1, backupCount=2)
    # file_handler.setFormatter(formatter)
    # logger.addHandler(file_handler)
    logHandler.setLevel(loglevel)
    logHandler.setFormatter(formatter)
    logger.addHandler(logHandler)

    return logger
