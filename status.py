from pathlib import Path
from datetime import datetime
msg=''
path='C:/Users/vgunaganti/PycharmProjects/jira/file.txt'
with open(path,'w') as file:
    file.write(msg)
line_number=3
error_message="this is an error message"
warning_message="this is warning message"
info="this is info"
p=Path(path)
file_name=p.name
time_stamp=datetime.fromtimestamp(p.stat().st_mtime).isoformat()