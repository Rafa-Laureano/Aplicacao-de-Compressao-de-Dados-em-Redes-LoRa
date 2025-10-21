# -*- coding: utf-8 -*-

import subprocess
import psutil
import csv
import os
import time
import threading
import tracemalloc
from collections import deque

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

def concatenate_messages(up_to_idx):
    return "\n".join(get_message(i) for i in range(up_to_idx))

def write_temp_file(data, filename):
    with open(filename, "w") as f:
        f.write(data)

def monitor_resources(process, stop_event, cpu_readings, mem_readings, sampling_interval=1):
    """Monitora continuamente o consumo de CPU e memória"""
    while not stop_event.is_set():
        process.cpu_percent(interval=None)
        time.sleep(sampling_interval)
        cpu = process.cpu_percent(interval=None)
        if cpu > 0:
            cpu_readings.append(cpu)  # in %
        mem = process.memory_info().rss / (1024 * 1024)
        if mem > 0:
            mem_readings.append(mem)  # in MB
        

def run_compression(process_command, num_repetitions):
    """Executa a compressão múltiplas vezes com monitoramento preciso"""
    total_cpu = 0
    total_mem = 0
    max_mem = 0
    
    # Inicia o monitoramento
    stop_event = threading.Event()
    cpu_readings = deque()
    mem_readings = deque()    
    
    process = psutil.Process()
            
    monitor_thread = threading.Thread(
        target=monitor_resources,
        args=(process, stop_event, cpu_readings, mem_readings)
    )
    monitor_thread.start()      
    
    for _ in range(num_repetitions):
            
        # Executa o processo
        process = subprocess.Popen(process_command,
                                   stdout=subprocess.PIPE,
                                   stderr=subprocess.PIPE)           
                                     
        process.wait()
           
    # Para o monitoramento
    stop_event.set()
    monitor_thread.join()
    
    # Calcula estatísticas
    if cpu_readings:
        avg_cpu = sum(cpu_readings) / len(cpu_readings)
    else:
        avg_cpu = 0
      
    if mem_readings:
        avg_mem = sum(mem_readings) / len(mem_readings)
        max_mem = max(mem_readings)
    else:
        avg_mem = 0
        max_mem = 0
    
    return avg_cpu, avg_mem, max_mem

def main():
    temp_input_file = "temp_input.txt"
    output_csv = "consumo_diversificado_bsc.csv"
    num_repetitions = 1000
    
    with open(output_csv, "w", newline='') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(["Num_Messages", "Avg_CPU_Percent", "Avg_Memory_MB", "Max_Memory_MB"])
        
        for num_msg in range(1, 170):
            try:
                data = concatenate_messages(num_msg)
                output_file = f"bsc_compressed_{num_msg}.bin"
                
                # Escreve arquivo temporário
                write_temp_file(data, temp_input_file)
                
                # Comando de compressão
                compress_cmd = ['./bsc-m03', 'e', temp_input_file, output_file]
                
                # Executa e monitora
                start_time = time.time()
                avg_cpu, avg_mem, max_mem = run_compression(compress_cmd, num_repetitions)
                elapsed_time = time.time() - start_time
                
                # Escreve resultados
                writer.writerow([
                    num_msg,
                    round(avg_cpu, 2),
                    round(avg_mem, 4),
                    round(max_mem, 2)
                ])
                csvfile.flush()
                
                print(f"Processado {num_msg} mensagens ({num_repetitions}x) - "
                      f"CPU: {avg_cpu:.2f}% - "
                      f"Mem: {avg_mem:.4f}MB (max: {max_mem:.2f}MB) - "
                      f"Tempo: {elapsed_time:.2f}s")
                
                # Limpeza
                if os.path.exists(temp_input_file):
                    os.remove(temp_input_file)
                if os.path.exists(output_file):
                    os.remove(output_file)
                    
            except Exception as e:
                print(f"Erro ao processar {num_msg} mensagens: {str(e)}")
                continue
    
    print(f"Monitoramento concluído. Resultados em {output_csv}")

if __name__ == "__main__":
    main()
