import logging
import logging.config
import os

from from_root import from_root
from datetime import datetime

LOG_FILE = f"{datetime.now().strftime('%m_%d_%Y_%I:%M:%S %p')}.log"
logs_path = os.path.join(from_root(),"logs",LOG_FILE)

os.makedirs(logs_path, exist_ok= True)

LOG_FILE_PATH = os.path.join(logs_path, LOG_FILE)

logging.basicConfig(
    filename= LOG_FILE_PATH,
    format= "[%(asctime)s] %(name)s - %(levelname)s - %(message)s",
    level= logging.DEBUG
)