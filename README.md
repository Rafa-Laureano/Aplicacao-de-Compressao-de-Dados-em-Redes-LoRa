# Aplicacao-de-Compressao-de-Dados-em-Redes-LoRa
O presente estudo explora a eficácia de algoritmos de compressão sem perdas, que utilizam técnicas clássicas e auxiliadas por aprendizado de máquina. Estes algoritmos são aplicados a três tipos de dados distintos: dados do sistema de coordenadas globais (GPS) (dados numéricos); dados de sensores IoT (texto); e dados de logística (alfanuméricos).

Para o algoritmo Huffman desenvolvido nesse estudo, utilize a linha de comando:

g++ -o "nome_de_preferencia" Arvore_bin.cpp Compress.cpp Lista.cpp main.cpp tabela_mani.cpp (para arquivos que possuem letras maiusculas, minusculas e números)

g++ -o "nome_de_preferencia" Arvore_bin.cpp Compress.cpp Lista.cpp main.cpp tabela_mani.cpp -DGPS (para arquivos que possuem apenas números e caracteres especiais)

g++ -o "nome_de_preferencia" Arvore_bin.cpp Compress.cpp Lista.cpp main.cpp tabela_mani.cpp -DLOG (para arquivos alfanuméricos)
