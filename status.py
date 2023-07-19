import JiraTask
from pathlib import Path
from datetime import datetime
#messages
critical_msg="CRITICAL:the internet is not working"
debug_msg="DEBUG:This is just a harmless debug message"
error_message="ERROR:this is an error message"
warning_message="WARNING:this is warning message"
info="INFO:this is info"
file=JiraTask.LogFile.path
line_number=1
p = Path(JiraTask.LogFile.path)
file_name = p.name
time_stamp = datetime.fromtimestamp(p.stat().st_mtime).isoformat()
#functions calling
JiraTask.Crititcal().critical(critical_msg,line_number)
JiraTask.Debug().debug(debug_msg,line_number)
JiraTask.Information().info(info,line_number)
JiraTask.Warning().warn(warning_message,line_number)
JiraTask.Error().err(error_message,line_number)
# LogFile.print_line(status.path,status.line_number)