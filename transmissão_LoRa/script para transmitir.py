from lorapy import start_lora, send_packet
from datetime import datetime


modulo = start_lora(SF=7)

file_path = "/home/rafaella/Desktop/raspberry5/experimentos/paq8px-master/paq8px-master/build/compress/teste_60"


with open(file_path, "rb") as f:
   data = f.read()

print(len(message))
    
send_packet(lora=modulo, packet=data)

