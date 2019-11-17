import logging
format = '%(asctime)s - %(name)s - %(filename)s - %(levelname)s - %(levelno)d - %(message)s'
logging.basicConfig(format=format, level=logging.DEBUG)
logger = logging.getLogger()
handler = logging.FileHandler("loki.log", mode="w")
handler.setLevel(logging.DEBUG)
shandler = logging.StreamHandler()
formatter = logging.Formatter(format)
handler.setFormatter(formatter)
shandler.setFormatter(formatter)

logger.addHandler(handler)
logger.addHandler(shandler)

'''logger.info("start reading from the data base")
result = {"venky":30,"loki":35}
logger.debug("result: %s",result)
logger.info("updating the data from the data base")
logger.info("finishing updating records")'''
