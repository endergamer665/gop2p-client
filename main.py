import requests
import socket

url = 'http://localhost:8080/devs'

def getReq():
    response = requests.get(url)

    if response.status_code == 200:
        print("connecton succsesfull")
        print(response.json())

    elif response.status_code !=200:
        print("connection unsuccsesfull", response.status_code)


hostname = socket.gethostname()
print("Device name:",hostname)

ip_address = socket.gethostbyname(hostname)
print("ip address:", ip_address)

private_ip = socket.get
print("private ip:", private_ip)

#response = requests.POST(url)

#if 