
# -*- coding: utf-8 -*-
import subprocess
import os
import time
import numpy as np

# Função para retornar as mensagens baseadas em um índice
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
    concatenated = ""
    for i in range(up_to_idx):
        concatenated += get_message(i) + "\n"
    return concatenated

def write_temp_file(data, filename):
    with open(filename, "w") as f:
        f.write(data)

def compress(input_filename, output_filename):
    subprocess.run(['./bsc-m03', 'e', input_filename, output_filename], capture_output=True, text=True)

# Configurações
temp_input_file = "temp_input.txt"
max_messages = 40  # número máximo de mensagens (grupos de 1 a 63)
num_of_rep = 100   # repetições por grupo

for num_of_msg in range(1, max_messages + 1):
    # Gera o nome do arquivo automaticamente
    output_time_file = f"tempos_bsc_logistica{num_of_msg}.txt"
    output_compressed_file = f"compressed_{num_of_msg}.bin"

    # Concatena as mensagens
    data_to_compress = concatenate_messages(num_of_msg)
    write_temp_file(data_to_compress, temp_input_file)

    # Medir tempos
    tempos = np.zeros(num_of_rep)
    for k in range(num_of_rep):
        start_time = time.time()
        compress(temp_input_file, output_compressed_file)
        end_time = time.time()
        tempos[k] = end_time - start_time

    # Escreve os tempos no arquivo específico
    with open(output_time_file, "w") as tempo_file:
        for t in tempos:
            tempo_file.write(f"Tempo para {num_of_msg} mensagens: {t:.15f} segundos\n")
        tempo_file.write(f"\nTempo médio para {num_of_msg} mensagens: {np.mean(tempos):.15f} segundos\n")

    print(f"Grupo {num_of_msg}: compressão concluída e tempos salvos em {output_time_file}")

print("\nCompressão de todos os grupos concluída com sucesso.")
