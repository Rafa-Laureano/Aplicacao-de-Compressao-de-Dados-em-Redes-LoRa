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
        "LM99124BX",
        "RA79102AN",
        "ZK21218PZ",
        "JH90142IU",
        "KO29145PE",
        "JU63751UG",
        "ZS14005VW",
        "CR75870ML",
        "CQ44911WY",
        "AZ99681GT",
        "HM93709FU",
        "CF48562GO",
        "IJ37790SB",
        "WK52167KU",
        "GJ64365PD",
        "VW93466BK",
        "KP69315HA",
        "WC85653YM",
        "FD06296JN",
        "BR52316MS",
        "AD93196LN",
        "ZP44334UM",
        "PR64170HJ",
        "DP63260SV",
        "NX68144SY",
        "VL07118PF",
        "FJ22579YZ",
        "SR70495TY",
        "UV13847XP",
        "YH62129TX",
        "XA94664NC",
        "SO09109EC",
        "FN69876OQ",
        "PX06905NJ",
        "MR32395LR",
        "WQ42274HY",
        "KC70290FE",
        "LK42235PL",
        "JM59893UX",
        "LX16753EE",
        "IW98061MQ",
        "OX56942FB",
        "GZ30642XM",
        "UI89924DI",
        "VM40257JL",
        "ZJ11514VI",
        "XA94664NC",
        "SO09109EC",
        "FN69876OQ",
        "VB31101AS",
        "AA14521MN",
        "HT36446KD",
        "XU22957ZD",
        "JF31756HN",
        "PW62698GL",
        "OG38266HT",
        "EC56788GB",
        "DH45078FG",
        "QW13163AG",
        "KQ16591PK",
        "ZX52165OJ",
        "CR08027KX",
        "HK06481RR",
        "QK09643ZX",
        "TU11860SV",
        "PS66620UZ",
        "QK40957CK",
        "ME07298NM",
        "KK26234PZ",
        "LG77445YV",
        "FZ02224ZX",
        "IR55608PK",
        "EB23886XQ",
        "MB39721UM",
        "AO99916AQ",
        "GR53996OW",
        "SA30272BB",
        "PH25185JJ",
        "AU65830ZG",
        "ZI95555EO",
        "LP59098BV",
        "GX43708FY",
        "NQ88747HX",
        "OA02527CB",
        "TF77003GS",
        "QP73499WR",
        "WU63470KT",
        "DG67514ZX",
        "TN89613NY",
        "QW97037XX",
        "YW82254SR",
        "SF51770KW",
        "CK74112TB",
        "JK36104WM",
        "AI26523NV",
        "TK71115CZ",
        "XS27894IK",
        "OR47377VU",
        "KT54810ZD",
        "HW18356RE",
        "BO93091QJ",
        "ZO68356VB",
        "GP19567XN"
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
    output_csv = "consumo_logistica_lzw.csv"
    num_repetitions = 1000
    
    with open(output_csv, "w", newline='') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(["Num_Messages", "Avg_CPU_Percent", "Avg_Memory_MB", "Max_Memory_MB"])
        
        for num_msg in range(1, 41):
            try:
                data = concatenate_messages(num_msg)
                output_file = f"lzw_compressed_{num_msg}.bin"
                
                # Escreve arquivo temporário
                write_temp_file(data, temp_input_file)
                

                # Comando de compressão
                compress_cmd = ["./compressao", temp_input_file, output_file]
                
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
