import logging
import os
from datetime import datetime

##created a string LOG_FILE
LOG_FILE=f"{datetime.now().strftime('%d_%m_%Y_%H_%M_%S')}.log"
## Creating a log folder inside the current project folder 
logs_path=os.path.join(os.getcwd(),"logs")
## Creates the logs folder 
os.makedirs(logs_path,exist_ok=True)
## Path of the log file 
LOG_FILE_PATH=os.path.join(logs_path,LOG_FILE)
logging.basicConfig(
    filename=LOG_FILE_PATH,
    level=logging.INFO,
    format="[ %(asctime)s ] %(lineno)d %(name)s - %(levelname)s - %(message)s"
)