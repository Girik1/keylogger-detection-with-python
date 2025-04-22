# keylogger-detection-with-python

How This Works:
Process List: The psutil.process_iter() function iterates over all running processes on the system and collects their information, such as pid (process ID) and name.

Suspicious Processes: We maintain a list of known keylogger process names in suspicious_processes. These are just examples; you should research actual keylogger names or add more known keyloggers to the list.

Detection: The script compares each running process name against the list of known keyloggers. If any match is found, it flags that process as suspicious.

Output: If a suspicious process is found, it outputs the PID (Process ID) and name of the process. If no suspicious processes are detected, it informs the user that the system appears clean.
