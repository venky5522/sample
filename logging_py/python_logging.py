import logging
logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)
logger.info("reading from the data base")
result = {"venky":30,"loki":35}
logger.debug("result: %s",result)
logger.info("updating the data base")
logger.info("closing the data base")
