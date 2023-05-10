import pyfiglet
import sys
import socket
from datatime import datatime

ascii_banner = pyfiglet.figlet_format("PORT SCANNER FROM PYTHON 3")
print(ascii_banner)

if len(sys.argv) == 2:
    target = socket.gethostbyname(sys.argv[1])
else:
  print("Invalid amount of Argument you must enter the IP")
