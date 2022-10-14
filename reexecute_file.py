'''
Author: Souvik Mondal
Purpose: Execute the python file which was fired unintentionally multiple times or 
		became Daemon thread and was running in background, can be fired again

Future Scope: Run with scheduler that will kill all threads and reexecute the file
			 after centain time
'''

from subprocess import check_output, CalledProcessError, Popen

# name of a python file
python_file = "check_links_alive.py"

# find pids of the mentioned file if running
try:
	pids = check_output(["pgrep","-f",python_file]).decode().split()
except CalledProcessError as e:
	print("No Process Found")
	pids = []

# execute the file again
Popen(['nohup', 'python3', python_file,'&'])

# kill all the pids
for pid in pids:
	Popen(['kill','-9',pid])

print("Done")