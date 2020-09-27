import subprocess

info=subprocess.check_output(['netsh','wlan','show','profiles']).decode('utf-8').split('\n')
wifi_names=[line.split(':')[1][1:-1] for line in info if "All User Profile" in line]

for wifi_name in wifi_names:
     results=subprocess.check_output(['netsh','wlan','show','profile',wifi_name,'key=clear']).decode('utf-8').split('\n')
     results=[line.split(':')[1][1:-1] for line in results if "Key Content" in line]
     try:
          print(f'Name: {wifi_name}, Password: {results[0]}')
     except:
          print(f'Name: {wifi_name}, Password: Cannot be read!!')