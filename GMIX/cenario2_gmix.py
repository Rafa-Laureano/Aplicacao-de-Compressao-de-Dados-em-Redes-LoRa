
# -*- coding: utf-8 -*-
import subprocess
import os
import time
import numpy as np

# Função para retornar as mensagens baseadas em um índice
def get_message(idx):
    messages = [
        "Sensor3-TEMP-not",
        "Sensor4-HUM-ok",
        "Sensor5-TEMP-ok",
        "Sensor2-GAS-low",
        "Sensor3-PRES-not",
        "Sensor3-POS-high",
        "Sensor2-HUM-low",
        "Sensor4-PRES-ok",
        "Sensor1-POS-high",
        "Sensor5-GAS-not",
        "Sensor5-PRES-not",
        "Sensor1-PRES-ok",
        "Sensor4-PRES-warning",
        "Sensor2-HUM-warning",
        "Sensor5-GAS-high",
        "Sensor1-HUM-warning",
        "Sensor4-PRES-ok",
        "Sensor5-POS-warning",
        "Sensor2-POS-high",
        "Sensor3-GAS-low",
        "Sensor2-POS-warning",
        "Sensor1-TEMP-not",
        "Sensor1-POS-ok",
        "Sensor2-GAS-high",
        "Sensor5-GAS-warning",
        "Sensor3-PRES-ok",
        "Sensor2-TEMP-low",
        "Sensor5-GAS-warning",
        "Sensor3-PRES-high",
        "Sensor2-HUM-warning",
        "Sensor1-TEMP-high",
        "Sensor1-GAS-ok",
        "Sensor5-POS-warning",
        "Sensor3-HUM-not",
        "Sensor1-TEMP-not",
        "Sensor3-TEMP-warning",
        "Sensor3-POS-warning",
        "Sensor3-POS-ok",
        "Sensor3-POS-low",
        "Sensor2-GAS-warning",
        "Sensor5-PRES-warning",
        "Sensor3-HUM-high",
        "Sensor3-POS-warning",
        "Sensor1-HUM-ok",
        "Sensor5-PRES-high",
        "Sensor1-POS-not",
        "Sensor1-PRES-high",
        "Sensor4-POS-warning",
        "Sensor1-PRES-high",
        "Sensor4-GAS-not",
        "Sensor3-POS-high",
        "Sensor4-GAS-ok",
        "Sensor2-HUM-ok",
        "Sensor1-PRES-high",
        "Sensor4-POS-ok",
        "Sensor2-POS-low",
        "Sensor2-GAS-high",
        "Sensor5-POS-ok",
        "Sensor3-TEMP-low",
        "Sensor3-GAS-not",
        "Sensor2-PRES-high",
        "Sensor5-GAS-low",
        "Sensor3-GAS-high",
        "Sensor3-POS-not",
        "Sensor2-HUM-warning",
        "Sensor3-TEMP-high",
        "Sensor1-GAS-low",
        "Sensor1-POS-high",
        "Sensor1-HUM-ok",
        "Sensor1-PRES-warning",
        "Sensor5-POS-low",
        "Sensor4-HUM-not",
        "Sensor5-TEMP-high",
        "Sensor2-TEMP-warning",
        "Sensor4-GAS-warning",
        "Sensor4-POS-low",
        "Sensor1-HUM-low",
        "Sensor3-TEMP-not",
        "Sensor4-HUM-ok",
        "Sensor5-TEMP-ok",
        "Sensor2-GAS-low",
        "Sensor3-PRES-not",
        "Sensor3-POS-high",
        "Sensor2-HUM-low",
        "Sensor4-PRES-ok",
        "Sensor1-POS-high",
        "Sensor5-GAS-not",
        "Sensor5-PRES-not",
        "Sensor1-PRES-ok",
        "Sensor4-PRES-warning",
        "Sensor2-HUM-warning",
        "Sensor5-GAS-high",
        "Sensor1-HUM-warning",
        "Sensor4-PRES-ok",
        "Sensor5-POS-warning",
        "Sensor2-POS-high",
        "Sensor3-GAS-low",
        "Sensor2-POS-warning",
        "Sensor1-TEMP-not",
        "Sensor1-POS-ok",
        "Sensor2-GAS-high",
        "Sensor5-GAS-warning",
        "Sensor3-PRES-ok",
        "Sensor2-TEMP-low",
        "Sensor5-GAS-warning",
        "Sensor3-PRES-high",
        "Sensor2-HUM-warning",
        "Sensor1-TEMP-high",
        "Sensor1-GAS-ok",
        "Sensor5-POS-warning",
        "Sensor3-HUM-not",
        "Sensor1-TEMP-not",
        "Sensor3-TEMP-warning",
        "Sensor3-POS-warning",
        "Sensor3-POS-ok",
        "Sensor3-POS-low",
        "Sensor2-GAS-warning",
        "Sensor5-PRES-warning",
        "Sensor3-HUM-high",
        "Sensor3-POS-warning",
        "Sensor1-HUM-ok",
        "Sensor5-PRES-high",
        "Sensor1-POS-not",
        "Sensor1-PRES-high",
        "Sensor4-POS-warning",
        "Sensor1-PRES-high",
        "Sensor4-GAS-not",
        "Sensor3-POS-high",
        "Sensor4-GAS-ok",
        "Sensor2-HUM-ok",
        "Sensor1-PRES-high",
        "Sensor4-POS-ok",
        "Sensor2-POS-low",
        "Sensor2-GAS-high",
        "Sensor5-POS-ok",
        "Sensor3-TEMP-low",
        "Sensor3-GAS-not",
        "Sensor2-PRES-high",
        "Sensor5-GAS-low",
        "Sensor3-GAS-high",
        "Sensor3-POS-not",
        "Sensor2-HUM-warning",
        "Sensor3-TEMP-high",
        "Sensor1-GAS-low",
        "Sensor1-POS-high",
        "Sensor1-HUM-ok",
        "Sensor1-PRES-warning",
        "Sensor5-POS-low",
        "Sensor4-HUM-not",
        "Sensor5-TEMP-high",
        "Sensor2-TEMP-warning",
        "Sensor4-GAS-warning",
        "Sensor4-POS-low",
        "Sensor1-HUM-low",
        "Sensor3-TEMP-not",
        "Sensor4-HUM-ok",
        "Sensor5-TEMP-ok",
        "Sensor2-GAS-low",
        "Sensor3-PRES-not",
        "Sensor3-POS-high",
        "Sensor2-HUM-low",
        "Sensor4-PRES-ok",
        "Sensor1-POS-high",
        "Sensor5-GAS-not",
        "Sensor5-PRES-not",
        "Sensor1-PRES-ok",
        "Sensor4-PRES-warning",
        "Sensor2-HUM-warning",
        "Sensor5-GAS-high",
        "Sensor1-HUM-warning",
        "Sensor4-PRES-ok",
        "Sensor5-POS-warning",
        "Sensor2-POS-high",
        "Sensor3-GAS-low",
        "Sensor2-POS-warning",
        "Sensor1-TEMP-not",
        "Sensor1-POS-ok",
        "Sensor2-GAS-high",
        "Sensor5-GAS-warning",
        "Sensor3-PRES-ok",
        "Sensor2-TEMP-low",
        "Sensor5-GAS-warning",
        "Sensor3-PRES-high",
        "Sensor2-HUM-warning",
        "Sensor1-TEMP-high",
        "Sensor1-GAS-ok",
        "Sensor5-POS-warning",
        "Sensor3-HUM-not",
        "Sensor1-TEMP-not",
        "Sensor3-TEMP-warning",
        "Sensor3-POS-warning",
        "Sensor3-POS-ok",
        "Sensor3-POS-low",
        "Sensor2-GAS-warning",
        "Sensor5-PRES-warning",
        "Sensor3-HUM-high",
        "Sensor3-POS-warning",
        "Sensor1-HUM-ok",
        "Sensor5-PRES-high",
        "Sensor1-POS-not",
        "Sensor1-PRES-high",
        "Sensor4-POS-warning",
        "Sensor1-PRES-high",
        "Sensor4-GAS-not",
        "Sensor3-POS-high",
        "Sensor4-GAS-ok",
        "Sensor2-HUM-ok",
        "Sensor1-PRES-high",
        "Sensor4-POS-ok",
        "Sensor2-POS-low",
        "Sensor2-GAS-high",
        "Sensor5-POS-ok",
        "Sensor3-TEMP-low",
        "Sensor3-GAS-not",
        "Sensor2-PRES-high",
        "Sensor5-GAS-low",
        "Sensor3-GAS-high",
        "Sensor3-POS-not",
        "Sensor2-HUM-warning",
        "Sensor3-TEMP-high",
        "Sensor1-GAS-low",
        "Sensor1-POS-high",
        "Sensor1-HUM-ok",
        "Sensor1-PRES-warning",
        "Sensor5-POS-low",
        "Sensor4-HUM-not",
        "Sensor5-TEMP-high",
        "Sensor2-TEMP-warning",
        "Sensor4-GAS-warning",
        "Sensor4-POS-low",
        "Sensor1-HUM-low",
        "Sensor5-PRES-ok"
    ]
    return messages[idx]

# Função para concatenar mensagens até o índice especificado
def concatenate_messages(up_to_idx):
    concatenated = ""
    for i in range(up_to_idx):
        concatenated += get_message(i) + "\n"
    return concatenated

# Função para escrever dados em um arquivo temporário
def write_temp_file(data, filename):
    with open(filename, "w") as f:
        f.write(data)

# Função para executar o compressor
def compress(input_filename, output_filename):
    subprocess.run(["./gmix", "-c", input_filename, output_filename], capture_output=True, text=True)

# Nome do arquivo temporário
temp_input_file = "temp_input.txt"

num_of_msg =  169

num_of_rep = 169

# Abre o arquivo para salvar os tempos de compressão
tempo = np.zeros((num_of_rep,))
with open("tempos_gmix_diversificado169.txt", "w") as tempo_file:
    # Executa a compressão de 1 até 169 mensagens, repetindo cada uma 1000 vezes
    for i in range(num_of_msg, num_of_msg+1):
        data_to_compress = concatenate_messages(i)
        output_file = f"compressed_{i}.bin"
        # Escreve os dados a serem comprimidos no arquivo temporário
        write_temp_file(data_to_compress, temp_input_file)

        for k in range(num_of_rep):
            start_time = time.time()
            compress(temp_input_file, output_file)
            end_time = time.time()
            tempo[k] = end_time - start_time
            
        for k in range(num_of_rep): 
            # Salva o tempo no arquivo
            tempo_file.write(f"Tempo para {i} mensagens: {tempo[k]:.15f} segundos\n")
        tempo_file.write(f"Tempo medio para {i} mensagens: {np.mean(tempo):.15f} segundos\n")
print("Compressao de grupos de mensagens concluida com sucesso.")
