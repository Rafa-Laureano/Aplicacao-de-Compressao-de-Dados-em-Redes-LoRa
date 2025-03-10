from lorapy import start_lora, receive_packet
from datetime import datetime
import time

modulo = start_lora(SF=7)

while True:
	pacote = receive_packet(lora=modulo)
	if pacote:
		print(pacote)
		horario = datetime.now().strftime("%H:%M:%S:%f")
		print(f"horario: {horario}")
		break
		

