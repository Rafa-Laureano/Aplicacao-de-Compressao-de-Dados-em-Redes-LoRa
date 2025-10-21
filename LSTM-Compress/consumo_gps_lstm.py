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

        "-24.732765,-53.763553",
        "-24.732765,-53.763553",
        "-24.732765,-53.763553",
        "-24.73274,-53.763553",
        "-24.73274,-53.763553",
        "-24.73274,-53.763553",
        "-24.73274,-53.763553",
        "-24.732734,-53.763557",
        "-24.732734,-53.763565",
        "-24.732736,-53.763557",
        "-24.732736,-53.763557",
        "-24.732736,-53.763557",
        "-24.732736,-53.763557",
        "-24.732437,-53.763534",
        "-24.732437,-53.763534",
        "-24.732006,-53.763664",
        "-24.732006,-53.763664",
        "-24.731723,-53.769142",
        "-24.731723,-53.769142",
        "-24.731723,-53.769142",
        "-24.731723,-53.769142",
        "-24.731723,-53.769142",
        "-24.730815,-53.767192",
        "-24.730815,-53.767192",
        "-24.730815,-53.767192",
        "-24.730815,-53.767192",
        "-24.730815,-53.767192",
        "-24.730167,-53.764495",
        "-24.730167,-53.764495",
        "-24.731939,-53.762893",
        "-24.731939,-53.762893",
        "-24.731939,-53.762893",
        "-24.731939,-53.762893",
        "-24.731939,-53.762893",
        "-24.731939,-53.762893",
        "-24.731939,-53.762893",
        "-24.731939,-53.762893",
        "-24.734163,-53.76242",
        "-24.734163,-53.76242",
        "-24.734163,-53.76242",
        "-24.734163,-53.76242",
        "-24.734163,-53.76242",
        "-24.734163,-53.76242",
        "-24.734163,-53.76242",
        "-24.733573,-53.761615",
        "-24.733573,-53.761615",
        "-24.733573,-53.761615",
        "-24.733573,-53.761615",
        "-24.733573,-53.761615",
        "-24.733573,-53.761615",
        "-24.7322,-53.760742",
        "-24.7322,-53.760742",
        "-24.7322,-53.760742",
        "-24.7322,-53.760742",
        "-24.7322,-53.760742",
        "-24.7322,-53.760742",
        "-24.732019,-53.761318",
        "-24.732019,-53.761318",
        "-24.733858,-53.760204",
        "-24.733858,-53.760204",
        "-24.733858,-53.760204",
        "-24.733858,-53.760204",
        "-24.733858,-53.760204",
        "-24.733858,-53.760204",
        "-24.733858,-53.760204",
        "-24.733858,-53.760204",
        "-24.731815,-53.761615",
        "-24.731815,-53.761615",
        "-24.731815,-53.761615",
        "-24.731815,-53.761615",
        "-24.731815,-53.761615",
        "-24.731815,-53.761615",
        "-24.731815,-53.761615",
        "-24.729873,-53.762302",
        "-24.729873,-53.762302",
        "-24.729873,-53.762302",
        "-24.729873,-53.762302",
        "-24.729873,-53.762302",
        "-24.730913,-53.762622",
        "-24.730913,-53.762622",
        "-24.730913,-53.762622",
        "-24.730913,-53.762622",
        "-24.730873,-53.76268",
        "-24.730873,-53.76268",
        "-24.730873,-53.76268",
        "-24.730644,-53.761566",
        "-24.730644,-53.761566",
        "-24.730644,-53.761566",
        "-24.730644,-53.761566",
        "-24.729955,-53.760654",
        "-24.729955,-53.760654",
        "-24.729955,-53.760654",
        "-24.729955,-53.760654",
        "-24.729955,-53.760654",
        "-24.730924,-53.7602",
        "-24.730924,-53.7602",
        "-24.730924,-53.7602",
        "-24.730924,-53.7602",
        "-24.730989,-53.760208",
        "-24.731742,-53.760704",
        "-24.731742,-53.760704",
        "-24.731742,-53.760704",
        "-24.731742,-53.760704",
        "-24.731742,-53.760704",
        "-24.732072,-53.760139",
        "-24.732072,-53.760139",
        "-24.732072,-53.760139",
        "-24.732072,-53.760139",
        "-24.732053,-53.761161",
        "-24.732044,-53.763412",
        "-24.732044,-53.763412",
        "-24.732044,-53.763412",
        "-24.731996,-53.765712",
        "-24.731996,-53.765712",
        "-24.731996,-53.765712",
        "-24.731996,-53.765712",
        "-24.731996,-53.765712",
        "-24.731916,-53.76794",
        "-24.731916,-53.76794",
        "-24.731916,-53.76794",
        "-24.731916,-53.76794",
        "-24.731916,-53.76794",
        "-24.731916,-53.76794",
        "-24.731916,-53.76794",
        "-24.731916,-53.76794",
        "-24.729858,-53.768421",
        "-24.729858,-53.768421",
        "-24.729858,-53.768421",
        "-24.73043,-53.768554",
        "-24.731576,-53.769409",
        "-24.731576,-53.769409",
        "-24.731576,-53.769409",
        "-24.731576,-53.769409",
        "-24.731576,-53.769409",
        "-24.730669,-53.770118",
        "-24.730669,-53.770118",
        "-24.729839,-53.770759",
        "-24.729715,-53.769916",
        "-24.729715,-53.769916",
        "-24.729715,-53.769916",
        "-24.729745,-53.764354",
        "-24.729745,-53.764354",
        "-24.729745,-53.764354",
        "-24.729745,-53.764354",
        "-24.729745,-53.764354",
        "-24.729745,-53.764354"
    ]
    return messages[idx]

def concatenate_messages(up_to_idx):
    return "\n".join(get_message(i) for i in range(up_to_idx))

def write_temp_file(data, filename):
    with open(filename, "w") as f:
        f.write(data)

def monitor_resources(stop_event, cpu_readings, mem_readings, sampling_interval=0.001):
    """Monitora continuamente o consumo de CPU e memória"""
    process = psutil.Process()
    while not stop_event.is_set():
        cpu_readings.append(psutil.cpu_percent(interval=None))
        mem_readings.append(process.memory_info().rss / (1024 * 1024))  # MB
        time.sleep(sampling_interval)

def run_compression(process_command, num_repetitions):
    """Executa a compressão múltiplas vezes com monitoramento preciso"""
    total_cpu = 0
    total_mem = 0
    max_mem = 0
    
    for _ in range(num_repetitions):
        try:
            # Inicia o monitoramento
            stop_event = threading.Event()
            cpu_readings = deque()
            mem_readings = deque()
            
            monitor_thread = threading.Thread(
                target=monitor_resources,
                args=(stop_event, cpu_readings, mem_readings)
            )
            monitor_thread.start()
            
            # Inicia o tracemalloc para medição precisa de memória
            tracemalloc.start()
            
            # Executa o processo
            start_time = time.time()
            process = subprocess.Popen(process_command,
                                     stdout=subprocess.PIPE,
                                     stderr=subprocess.PIPE)
            process.wait()
            elapsed_time = time.time() - start_time
            
            # Para o monitoramento
            stop_event.set()
            monitor_thread.join()
            
            # Obtém estatísticas de memória
            current_mem, peak_mem = tracemalloc.get_traced_memory()
            tracemalloc.stop()
            
            # Calcula estatísticas
            if cpu_readings:
                avg_cpu = sum(cpu_readings) / len(cpu_readings)
            else:
                avg_cpu = 0
                
            if mem_readings:
                avg_mem = sum(mem_readings) / len(mem_readings)
                max_mem_reading = max(mem_readings)
            else:
                avg_mem = 0
                max_mem_reading = 0
                
            # Converte memória para MB
            peak_mem_mb = peak_mem / (1024 * 1024)
            current_mem_mb = current_mem / (1024 * 1024)
            max_mem_reading = max(max_mem_reading, peak_mem_mb)
            
            total_cpu += avg_cpu
            total_mem += avg_mem
            if max_mem_reading > max_mem:
                max_mem = max_mem_reading
                
        except Exception as e:
            print(f"Erro durante execução: {str(e)}")
            if 'tracemalloc' in locals():
                tracemalloc.stop()
            if 'stop_event' in locals() and not stop_event.is_set():
                stop_event.set()
            continue
    
    # Calcula médias
    avg_cpu = total_cpu / num_repetitions if num_repetitions > 0 else 0
    avg_mem = total_mem / num_repetitions if num_repetitions > 0 else 0
    
    return avg_cpu, avg_mem, max_mem

def main():
    temp_input_file = "temp_input.txt"
    output_csv = "consumo_gps_lstm.csv"
    num_repetitions = 10
    
    with open(output_csv, "w", newline='') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(["Num_Messages", "Avg_CPU_Percent", "Avg_Memory_MB", "Max_Memory_MB"])
        
        for num_msg in range(1, 64):
            try:
                data = concatenate_messages(num_msg)
                output_file = f"lstm_compressed_{num_msg}.bin"
                
                # Escreve arquivo temporário
                write_temp_file(data, temp_input_file)
                
                # Comando de compressão
                compress_cmd = ["./lstm-compress", "-c", temp_input_file, output_file]
                
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
