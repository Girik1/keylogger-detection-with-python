import psutil
import os

# List of common keylogger processes (this can be expanded)
suspicious_processes = [
    "keylogger.exe",  # Example process names (change according to real keylogger names)
    "freekeylogger.exe",
    "spykeylogger.exe",
    "claviskeylogger.exe",
    "logkeys.exe",
    "keyghost.exe",
]

def get_running_processes():
    """Returns a list of all running processes."""
    running_processes = []
    for proc in psutil.process_iter(['pid', 'name']):
        running_processes.append(proc.info)
    return running_processes

def detect_suspicious_processes():
    """Detects any suspicious process that may indicate a keylogger."""
    running_processes = get_running_processes()
    suspicious_found = []
    
    for process in running_processes:
        process_name = process['name'].lower()
        
        # Check if the process name matches any suspicious patterns
        for suspicious in suspicious_processes:
            if suspicious.lower() in process_name:
                suspicious_found.append(process)
    
    return suspicious_found

def main():
    suspicious_processes_found = detect_suspicious_processes()
    
    if suspicious_processes_found:
        print("Suspicious processes detected! Possible keylogger(s):")
        for proc in suspicious_processes_found:
            print(f"PID: {proc['pid']}, Process Name: {proc['name']}")
    else:
        print("No suspicious processes detected. System appears clean.")
        
if __name__ == "__main__":
    main()
