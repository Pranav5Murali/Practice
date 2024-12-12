import os

# Get the server name (hostname)
hostname = os.uname().nodename
print(f"Hostname: {hostname}")

# Get the current working directory
cwd = os.getcwd()
print(f"Current Working Directory: {cwd}")

# Get the operating system name
os_name = os.name  # 'posix' for Unix-like, 'nt' for Windows
print(f"Operating System: {os_name}")