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
    output_csv = "consumo_gps_cmix.csv"
    num_repetitions = 100
    max_messages = 64

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

