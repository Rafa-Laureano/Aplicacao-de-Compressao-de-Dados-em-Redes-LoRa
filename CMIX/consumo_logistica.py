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
    output_csv = "consumo_logistica_cmix.csv"
    num_repetitions = 100
    max_messages = 40

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

