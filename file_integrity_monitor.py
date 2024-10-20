import hashlib
import os
import time

# Specify the file to monitor
file_to_monitor = "example.txt"
log_file = "logs/integrity_log.txt"

def get_file_hash(filepath):
    """Returns the MD5 hash of the given file."""
    with open(filepath, "rb") as f:
        file_hash = hashlib.md5(f.read()).hexdigest()
    return file_hash

def monitor_file():
    """Monitors the specified file for changes and logs modifications."""
    if not os.path.exists(file_to_monitor):
        print(f"{file_to_monitor} does not exist. Exiting.")
        return

    last_hash = get_file_hash(file_to_monitor)
    print(f"Monitoring changes to {file_to_monitor}...")

    while True:
        time.sleep(10)  # Check every 10 seconds
        current_hash = get_file_hash(file_to_monitor)
        if current_hash != last_hash:
            with open(log_file, "a") as log:
                log.write(f"File changed: {file_to_monitor}, at {time.ctime()}\n")
            print(f"Change detected in {file_to_monitor}!")
            last_hash = current_hash

if __name__ == "__main__":
    monitor_file()
