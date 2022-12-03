import logging
from datetime import datetime
import os

#making the directory name for our logdirectory
LOG_DIR = "my_personel_logs"

#creating the log names on the fly(streaming names)
CURRENT_TIME_STAMP = f"{datetime.now().strftime('%Y-%M-%d_%H-%M-%S')}"

#creating the actual name of the every log file with the help of above code.
LOG_FILE_NAME = f"log_{CURRENT_TIME_STAMP}.log"

#make directory if that directory doesn't exist
os.makedirs(LOG_DIR,exist_ok=True)

#joining the log_dir/log_file_name as a folder
CORRECT_PATH = os.path.join(LOG_DIR,LOG_FILE_NAME)

#creating the logging configuring to our wish
logging.basicConfig(filename=CORRECT_PATH,
filemode='w',
format='[%(asctime)s] %(name)s - %(levelname)s: %(message)s',
level=logging.INFO
)