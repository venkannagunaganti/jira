import JiraTask,Message,inspect,os

#fetching the path and file name
path=os.path.abspath(__file__)
file_name=os.path.basename(path)

#fetching the line number
@staticmethod
def line_num():
    file=inspect.currentframe()
    i=inspect.getframeinfo(file.f_back)
    return i.lineno

#functions calling
JiraTask.create_log_file(file_name)
JiraTask.msg(file_name,line_num(),
             Message.critical_type,Message.critical)
JiraTask.msg(file_name,line_num(),
             Message.debug_type,Message.debug)
JiraTask.msg(file_name,line_num(),
             Message.warning_type,Message.warning)
JiraTask.msg(file_name,line_num(),
             Message.info_type,Message.info)
JiraTask.msg(file_name,line_num(),
             Message.error_type,Message.error)
JiraTask.msg(file_name,line_num(),
             Message.display_type,Message.display)
JiraTask.msg(file_name,line_num(),
             Message.critical_type,Message.critical)
JiraTask.msg(file_name,line_num(),
             Message.debug_type,Message.debug)
JiraTask.msg(file_name,line_num(),
             Message.warning_type,Message.warning)





