from pathlib import Path
import subprocess

# Path to the cloned repository and the target Python script
repo_path = Path("/home/user1/target")  # Adjust the path as needed
script_path = repo_path / "Test.py"

# Ensure the script exists
if script_path.exists() and script_path.is_file():
    # Execute the script using subprocess
    result = subprocess.run(["python3", str(script_path)], capture_output=True, text=True)
    
    # Print the script's output
    print("Script Output:")
    print(result.stdout)
else:
    print(f"Script {script_path} not found!")
