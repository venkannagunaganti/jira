from datetime import datetime
from pathlib import Path
class LogFile:
#writing to the log file function
  path = 'C:/Users/vgunaganti/PycharmProjects/jira/file.txt'
  msg = ''
  with open(path, 'w') as file:
    file.write(msg)
    @staticmethod
    def write_to_log_file(msg,line_number):
        p = Path(LogFile.path)
        file_name = p.name
        time_stamp = datetime.fromtimestamp(p.stat().st_mtime).isoformat()
        with open(LogFile.path,'a+') as file:
            file.write(time_stamp+' '+str(line_number)+' '+file_name+' '+msg+'\n')
    @staticmethod
    def print_line(path,line_number):
        with open(path,'r') as file:
            lines=file.readlines()
            file.close()
            line=lines[line_number-1]
            print(line+'')
class Crititcal:
# function to write critical msg
    @staticmethod
    def critical(msg,line_number):
        LogFile.write_to_log_file(msg,line_number)
class Debug:
    @staticmethod
    def debug(msg,line_number):
        LogFile.write_to_log_file(msg,line_number)
class Error:
#funtion to pass error message
    @staticmethod
    def err(msg,line_number):
        LogFile.write_to_log_file(msg,line_number)
class Warning:
#function to pass warning message
    @staticmethod
    def warn(msg,line_number):
        LogFile.write_to_log_file(msg,line_number)

class Information:
#function to pass information
    @staticmethod
    def info(msg,line_number):
        LogFile.write_to_log_file(msg,line_number)


