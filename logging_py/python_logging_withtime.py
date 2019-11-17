import logging
format = '%(asctime)s - %(name)s - %(filename)s - %(levelname)s - %(levelno)d - %(message)s'
logging.basicConfig(format=format, level=logging.DEBUG)
logger = logging.getLogger()
logger.info("reading from the data base")
result = {"venky":30,"loki":35}
logging.debug("result is: %s",result)
logger.info("closing the data base")
