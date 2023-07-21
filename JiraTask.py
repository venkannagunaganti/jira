from datetime import datetime
from pathlib import Path
import Message
class LogFile:
#writing to the log file function
  path = 'C:/Users/vgunaganti/PycharmProjects/jira/file.txt'
  p = Path(path)
  time_stamp = datetime.fromtimestamp(p.stat().st_mtime).isoformat()
  msg = ''
  with open(path, 'w') as file:
    file.write(msg)
    @staticmethod
    def write_to_log_file(file_name,msg,line_number):

        with open(LogFile.path,'a+') as file:

            file.write(LogFile.time_stamp+' '+str(file_name)+':'+str(line_number)+' '+msg+'\n')
def msg(file_name,msg,line_no):


    match msg:
        case Message.critical_msg:
            LogFile.write_to_log_file(file_name,Message.critical_msg,line_no)
        case Message.debug_msg:
            LogFile.write_to_log_file(file_name,Message.debug_msg,line_no)
        case Message.warning_message:
            LogFile.write_to_log_file(file_name,Message.warning_message,line_no)
        case Message.info:
            LogFile.write_to_log_file(file_name,Message.info,line_no)
        case Message.error_message:
            LogFile.write_to_log_file(file_name,Message.error_message,line_no)
        case Message.Display:
            print(f"{LogFile.time_stamp} {file_name}:{line_no} {Message.Display}")




