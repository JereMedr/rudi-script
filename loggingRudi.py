import logging
from datetime import datetime

dt = datetime.now()
nombreArchivo = dt.strftime("%Y%m%d_%H%M%S") + ".log"
logging.basicConfig(filename= './logs/'+nombreArchivo , encoding='utf-8', level=logging.DEBUG, 
                filemode='w',
                format='%(asctime)s %(levelname)s %(message)s', datefmt='%m/%d/%Y %I:%M:%S %p'
                )

def logInfo(msg):
    logging.info(msg)

def logDebug(msg):
    logging.debug(msg)

def logWarning(msg):
    logging.warning(msg)

def logError(msg):
    logging.error(msg)

def logCritical(msg):
    logging.critical(msg)

def logException(msg):
    logging.exception(msg)

def log(msg):
    logging.log(msg)
