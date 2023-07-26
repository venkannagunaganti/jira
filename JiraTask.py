import os.path
from datetime import datetime
from pathlib import Path
import Message



Log_file:str
class LogFile:
#writing to the log file function
  @staticmethod
  def create_file(filename):
      Log_file= filename
  p=os.path.abspath(__file__)
  path=Path(p).parent
  name="status.py".split(".")
  x=name[0]
  y=".log"
  path=path.joinpath(x+y)
  path=f"{path}"
  msg = ''
  with open(path, 'w') as file:
     file.write(msg)
  p = Path(path)
  time_stamp = datetime.fromtimestamp(p.stat().st_mtime).isoformat()


  @staticmethod
  def write_to_log_file(file_name,line_number,msg_type,msg):

        with open(LogFile.path,'a+') as file:

            file.write(f"{LogFile.time_stamp} {file_name}:{line_number} {msg_type}:{msg}\n")
@staticmethod
def msg(file_name,line_no,msg_type,msg):
    match msg_type:
        case Message.critical_type:
            LogFile.write_to_log_file(file_name,line_no,Message.critical_type,msg)
        case Message.debug_type:
            LogFile.write_to_log_file(file_name,line_no,Message.debug_type,msg)
        case Message.warning_type:
            LogFile.write_to_log_file(file_name,line_no,Message.warning_type,msg)
        case Message.info_type:
            LogFile.write_to_log_file(file_name,line_no,Message.info_type,msg)
        case Message.error_type:
            LogFile.write_to_log_file(file_name,line_no,Message.error_type,msg)
        case Message.display_type:
            print(f"{LogFile.time_stamp} {file_name}:{line_no} {Message.display}")

        case unknown_command:
            print(f"invalid message:{unknown_command} at lineno:{line_no}")




