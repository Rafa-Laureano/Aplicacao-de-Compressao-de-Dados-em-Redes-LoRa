#include <iostream>
#include <fstream>
#include <string>
#include <vector>
#include <cstring>

#include "Arvore_bin.h"
#include "Compress.h"
#include "Lista.h"
#include "tabela_mani.h"

void compressFile(const std::string& inputFilePath, const std::string& outputFilePath) {
    // Inicializa as estruturas necessárias
    lista lista_ordenada;
    inicializa_lista(&lista_ordenada);
	
    // Lê o arquivo de entrada
    std::ifstream inputFile(inputFilePath, std::ios::binary);
    if(!inputFile) {
        std::cerr << "Erro ao abrir o arquivo de entrada: " << inputFilePath << std::endl;
        return;
    }

    // Lê o conteúdo do arquivo
    std::string content((std::istreambuf_iterator<char>(inputFile)), std::istreambuf_iterator<char>());
    inputFile.close();

    // Cria a tabela de frequência dos caracteres
	unsigned short tabela_probabilidade[TAB_OFFSET] = {0};
    if(tabela(const_cast<char*>(content.c_str()), tabela_probabilidade) != 0) {
        std::cerr << "Erro: Estouro na tabela de probabilidade." << std::endl;
        return;
    }

    // Constroi a lista ordenada e a árvore de Huffman
    constroi_lista(tabela_probabilidade, &lista_ordenada);
    constroi_arvore(&lista_ordenada);

    // Inicializa as variáveis necessárias para a compressão
    unsigned int tamanho_dado_compactado = 0;
    unsigned short bits = 15;
    unsigned short aux_cod = 0;
    std::vector<unsigned short> mensagem_code(TAB_OFFSET + int(content.size()/2) + 1, 0);

    // Executa a compressão
    compress_dado(const_cast<char*>(content.c_str()), &tamanho_dado_compactado, &bits, &aux_cod, mensagem_code.data(), lista_ordenada.head->dado);

    // CARREGA TABELA
    for(int m = 0; m < TAB_OFFSET-1; m++){
        mensagem_code.data()[m] = tabela_probabilidade[m];
    }
	
	/*for(int i = 0; i < (TAB_OFFSET + tamanho_dado_compactado); i++) {
		printf("### mensagem_code.data()[%d]: %x\n", i, mensagem_code.data()[i]);
	}*/

    // Salva a mensagem comprimida no arquivo de saída
    std::ofstream outputFile(outputFilePath, std::ios::binary);
    if(!outputFile) {
        std::cerr << "Erro ao abrir o arquivo de saída: " << outputFilePath << std::endl;
        return;
    }

    outputFile.write(reinterpret_cast<const char*>(mensagem_code.data()), (TAB_OFFSET + tamanho_dado_compactado)*sizeof(unsigned short));
    outputFile.close();

    std::cout << "Arquivo comprimido com sucesso: " << outputFilePath << std::endl;
}

void deCompressFile(const std::string& inputFilePath, const std::string& outputFilePath) {
    // Inicializa as estruturas necessárias
    lista lista_ordenada;
    inicializa_lista(&lista_ordenada);
	
    // Lê o arquivo de entrada
    std::ifstream inputFile(inputFilePath, std::ios::binary);
    if (!inputFile) {
        std::cerr << "Erro ao abrir o arquivo de entrada: " << inputFilePath << std::endl;
        return;
    }

    // Lê o conteúdo do arquivo
    std::string content((std::istreambuf_iterator<char>(inputFile)), std::istreambuf_iterator<char>());
    inputFile.close();
	
	//printf("content.size(): %ld\n", content.size());
	
	unsigned short buffer[content.size()/2]; 
	
	// Copie os dados para um buffer de tipo apropriado
	std::memcpy(buffer, content.c_str(), content.size());
	
	
	/*for(int i = 0; i < content.size()/2; i++) {
		printf("*** buffer[%d]: %x\n",i,buffer[i]);
	}
	printf("--------------------------------\n");*/

    // Inicializa as variáveis necessárias para a descompressão
	char* rawPtr = NULL;

    // Executa a descompressão.
	int char_counter = 0;
	descompacta(&rawPtr, buffer, content.size(), 300, &char_counter);

    // Salva a mensagem comprimida no arquivo de saída
    std::ofstream outputFile(outputFilePath, std::ios::binary);
    if(!outputFile) {
        std::cerr << "Erro ao abrir o arquivo de saída: " << outputFilePath << std::endl;
        return;
    }

    outputFile.write(reinterpret_cast<const char*>(rawPtr), char_counter);
    outputFile.close();
	
	free(rawPtr);

    std::cout << "Arquivo descomprimido com sucesso: " << outputFilePath << std::endl;
}

int main(int argc, char* argv[]) {

    if (argc != 4) {
		std::cerr << "Uso: " << "-c/-d" << argv[0] << " <arquivo_entrada> <arquivo_saida>" << std::endl;
        return 1;
    }
	
    std::string inputFilePath = argv[2];
    std::string outputFilePath = argv[3];	
	
	if(strcmp("-c", argv[1]) == 0) {
		compressFile(inputFilePath, outputFilePath);
	}
	
	if(strcmp("-d", argv[1]) == 0) {
		deCompressFile(inputFilePath, outputFilePath);
	}

    return 0;
}
