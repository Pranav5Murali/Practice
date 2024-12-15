import platform
import os
import socket
import psutil
print("start")
def find_git_repositories(start_path='/home/user1'):
    """ Walk through directories starting from 'start_path' and find Git repositories """
    for dirpath, dirnames, filenames in os.walk(start_path):
        if '.git' in dirnames:  # Check if the directory contains a '.git' folder
            print(f"Git repository found: {dirpath}")
            break  # Stop after finding the first Git repo

def get_system_info():
    # Create a dictionary to store the system information
    system_info = {}

    # Get hostname
    system_info['hostname'] = socket.gethostname()

    # Get OS details
    system_info['os'] = platform.system()
    system_info['os_version'] = platform.version()
    system_info['os_release'] = platform.release()
    system_info['os_distribution'] = platform.linux_distribution() if hasattr(platform, 'linux_distribution') else 'N/A'

    # Get CPU information
    system_info['cpu'] = platform.processor()
    system_info['cpu_cores'] = psutil.cpu_count(logical=False)
    system_info['logical_cpu_cores'] = psutil.cpu_count(logical=True)
    
    # Get RAM information
    system_info['total_memory'] = psutil.virtual_memory().total / (1024 ** 3)  # in GB
    system_info['available_memory'] = psutil.virtual_memory().available / (1024 ** 3)  # in GB

    # Get disk information
    system_info['total_disk'] = psutil.disk_usage('/').total / (1024 ** 3)  # in GB
    system_info['used_disk'] = psutil.disk_usage('/').used / (1024 ** 3)  # in GB
    system_info['free_disk'] = psutil.disk_usage('/').free / (1024 ** 3)  # in GB

    # Get IP address (just the local address for the VM)
    system_info['ip_address'] = socket.gethostbyname(socket.gethostname())

    return system_info

find_git_repositories()
# Get and print the system info
info = get_system_info()
print(info)
