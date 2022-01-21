from src.date import dateFormatted

import csv
import sys
import yaml
import os


stream = open("./config.yaml", 'r')
c = yaml.safe_load(stream)

last_log_is_progress = False

COLOR = {
    'blue': '\033[94m',
    'default': '\033[99m',
    'grey': '\033[90m',
    'yellow': '\033[93m',
    'black': '\033[90m',
    'cyan': '\033[96m',
    'green': '\033[92m',
    'magenta': '\033[95m',
    'white': '\033[97m',
    'red': '\033[91m'
}

def logger(message, progress_indicator = False, color = 'default'):
    global last_log_is_progress
    color_formatted = COLOR.get(color.lower(), COLOR['default'])

    formatted_datetime = dateFormatted()
    formatted_message = "[{}] => {}".format(formatted_datetime, message)
    formatted_message_colored  = color_formatted + formatted_message + '\033[0m'

    
    # Start progress indicator and append dots to in subsequent progress calls
    if progress_indicator:
        if not last_log_is_progress:
            last_log_is_progress = True
            formatted_message = color_formatted + "[{}] => {}".format(formatted_datetime, '⬆️ Processing last action..')
            sys.stdout.write(formatted_message)
            sys.stdout.flush()
        else:
            sys.stdout.write(color_formatted + '.')
            sys.stdout.flush()
        return

    if last_log_is_progress:
        sys.stdout.write('\n')
        sys.stdout.flush()
        last_log_is_progress = False    

    print(formatted_message_colored)

    if (c['save_log_to_file'] == True):
        logger_file = open("./logs/logger.log", "a", encoding='utf-8')
        logger_file.write(formatted_message + '\n')
        logger_file.close()

    return True
    
def loggerRegisterBcoin(bcoin):
 
  current_date = dateFormatted()
  with open('./logs/bcoin.csv', 'a+', encoding='UTF8', newline='') as f:
 
    writer = csv.writer(f)
   
    writer.writerows([[current_date, bcoin]])
    	
  #logger_file = open("./logs/bcoin.log", "a", encoding='utf-8')
  #logger_file.write(dateFormatted() + ' '+ bcoin +'\n')
  #logger_file.close()
  loggerRegisterBcoinDate()
  
def loggerRegisterBcoinDate():
  logger_file = open("./logs/bcoin_date.log", "w", encoding='utf-8')
  logger_file.write(dateFormatted('%Y-%m-%d'))
  logger_file.close()
def getLastBcoinDate():
  exists = os.path.exists("./logs/bcoin_date.log")
  
  if exists == False:
    return ''
    
  logger_file = open("./logs/bcoin_date.log", "r+", encoding='utf-8')
  date_logged =  logger_file.read()
  logger_file.close()
  return date_logged
   
def loggerMapClicked():
  logger('🗺️ New Map button clicked!')
  logger_file = open("./logs/new-map.log", "a", encoding='utf-8')
  logger_file.write(dateFormatted() + '\n')
  logger_file.close()
