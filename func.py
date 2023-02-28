import socket  
import os


hostname = socket.gethostname()
ip_address = socket.gethostbyname(hostname)

command = os.system('ipconfig')
