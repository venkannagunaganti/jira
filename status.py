import JiraTask

critical_msg="CRITICAL:the internet is not working"
debug_msg="DEBUG:This is just a harmless debug message"
error_message="ERROR:this is an error message"
warning_message="WARNING:this is warning message"
info="INFO:this is info"
file=JiraTask.LogFile.path
line_number=1

critical=JiraTask.Crititcal()
debug=JiraTask.Debug()
error=JiraTask.Error()
warning=JiraTask.Warning()
information=JiraTask.Information()
critical.critical(critical_msg,line_number)
debug.debug(debug_msg,line_number)
information.info(info,line_number)
warning.warn(warning_message,line_number)
error.err(error_message,line_number)


# LogFile.print_line(status.path,status.line_number)