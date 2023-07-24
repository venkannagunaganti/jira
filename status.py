import JiraTask
import Message
import inspect
import os
#messages
path="C:/Users/vgunaganti/PycharmProjects/jira/status.py"
file_name=os.path.basename(path)
@staticmethod
def line_num():
    file=inspect.currentframe()
    i=inspect.getframeinfo(file.f_back)
    return i.lineno

#functions calling
JiraTask.msg(file_name,Message.critical_msg,line_num())
JiraTask.msg(file_name,Message.debug_msg,line_num())
JiraTask.msg(file_name,"Message.warning_message",line_num())
JiraTask.msg(file_name,Message.info,line_num())
JiraTask.msg(file_name,Message.error_message,line_num())
JiraTask.msg(file_name,Message.Display,line_num())




