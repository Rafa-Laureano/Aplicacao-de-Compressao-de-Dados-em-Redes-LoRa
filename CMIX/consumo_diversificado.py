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

def monitor_resources(process, cpu_readings, mem_readings, sampling_interval=0.1):
    """Monitora continuamente o consumo de CPU e memória (incluindo subprocessos)"""
    try:
        proc = psutil.Process(process.pid)

        # Pré-aquecimento para todas threads e subprocessos
        children = proc.children(recursive=True)
        all_procs = [proc] + children
        for p in all_procs:
            try:
                p.cpu_percent(interval=None)
            except:
                pass

        while process.poll() is None:
            time.sleep(sampling_interval)

            try:
                children = proc.children(recursive=True)
                all_procs = [proc] + children

                total_cpu = 0.0
                total_mem = 0.0

                for p in all_procs:
                    try:
                        total_cpu += p.cpu_percent(interval=None)
                        total_mem += p.memory_info().rss
                    except (psutil.NoSuchProcess, psutil.AccessDenied):
                        continue

                if total_cpu > 0:
                    cpu_readings.append(total_cpu)  # porcentagem
                if total_mem > 0:
                    mem_readings.append(total_mem / (1024 * 1024))  # MB

            except Exception as e:
                print("Erro ao monitorar:", e)
                break
    except Exception as e:
        print("Erro ao criar processo psutil:", e)

def run_compression(process_command, num_repetitions):
    """Executa a compressão múltiplas vezes com monitoramento preciso"""
    cpu_readings = deque()
    mem_readings = deque()

    for _ in range(num_repetitions):
        process = subprocess.Popen(process_command, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
        monitor_resources(process, cpu_readings, mem_readings, sampling_interval=0.1)

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
    output_csv = "consumo_diversificado_cmix.csv"
    num_repetitions = 100
    max_messages = 169

    with open(output_csv, "w", newline='') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(["Num_Mensagens", "CPU_Media(%)", "RAM_Media(MB)", "RAM_Max(MB)", "Tempo_Total(s)"])

        for num_msg in range(1, max_messages + 1):
            try:
                data = concatenate_messages(num_msg)
                output_file = f"cmix_{num_msg}.bin"
                write_temp_file(data, temp_input_file)

                compress_cmd = ["./cmix", "-c", temp_input_file, output_file]

                start_time = time.time()
                avg_cpu, avg_mem, max_mem = run_compression(compress_cmd, num_repetitions)
                elapsed_time = time.time() - start_time

                writer.writerow([
                    num_msg,
                    round(avg_cpu, 2),
                    round(avg_mem, 2),
                    round(max_mem, 2),
                    round(elapsed_time, 2)
                ])
                csvfile.flush()

                print(f"{num_msg} msgs ({num_repetitions}x): CPU {avg_cpu:.2f}%, MEM {avg_mem:.2f}MB (max {max_mem:.2f}MB), Tempo {elapsed_time:.2f}s")

                os.remove(temp_input_file)
                if os.path.exists(output_file):
                    os.remove(output_file)

            except Exception as e:
                print(f"[ERRO] {num_msg} mensagens: {e}")
                continue

    print(f"✅ Resultados salvos em: {output_csv}")

if __name__ == "__main__":
    main()

