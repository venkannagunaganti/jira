import  status
import inspect
class LogFile:
    #writing to the log file

    @staticmethod
    def write_to_log_file(path,msg,line_number):


        with open(path,'a+') as file:


            file.write(status.file_name+' '+msg+' '+status.time_stamp+' '+'\n')
    @staticmethod
    def print_line(path,line_number):
        with open(path,'r') as file:
            lines=file.readlines()
            file.close()
            line=lines[line_number-1]
            print(line+'')

class Error:
    #funtion to print error message
    @staticmethod
    def err(path,msg,line_number):
        LogFile.write_to_log_file(path,msg,line_number)

class Warning:
    #function to print warning message
    @staticmethod
    def warn(path,msg,line_number):
        LogFile.write_to_log_file(path,msg,line_number)

class Information:
    #function to print information
    @staticmethod
    def info(path,msg,line_number):
        LogFile.write_to_log_file(path,msg,line_number)

error=Error()
warning=Warning()
information=Information()
error_message=status.error_message
warning_message=status.warning_message
info=status.info
error.err(status.path,error_message,status.line_number)
warning.warn(status.path,warning_message,status.line_number)
information.info(status.path,info,status.line_number)
LogFile.print_line(status.path,status.line_number)
