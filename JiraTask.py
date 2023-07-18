import  status
class LogFile:
    @staticmethod
    def write_to_log_file(path,msg):
        with open(path,'a+') as file:
            file.write(status.file_name+' '+msg+' '+status.time_stamp+' '+'\n')

class Error:
    @staticmethod
    def err(path,msg):
        LogFile.write_to_log_file(path,msg)

class Warning:
    @staticmethod
    def warn(path,msg):
        LogFile.write_to_log_file(path,msg)

class Information:
    @staticmethod
    def info(path,msg):
        LogFile.write_to_log_file(path,msg)

error=Error()
warning=Warning()
information=Information()
error_message=status.error_message
warning_message=status.warning_message
info=status.info
error.err(status.path,error_message)
warning.warn(status.path,warning_message)
information.info(status.p,info)
