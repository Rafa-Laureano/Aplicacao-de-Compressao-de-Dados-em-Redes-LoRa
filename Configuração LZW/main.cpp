#include <iostream>
#include <fstream>
#include <vector>
#include "Compress.h"
#include "Lista.h"

std::vector<char> lerArquivo(const std::string& nomeArquivo) {
    std::ifstream file(nomeArquivo, std::ios::binary);
    return std::vector<char>((std::istreambuf_iterator<char>(file)), std::istreambuf_iterator<char>());
}

void escreverArquivo(const std::string& nomeArquivo, const std::vector<unsigned char>& dados) {
    std::ofstream file(nomeArquivo, std::ios::binary);
    file.write(reinterpret_cast<const char*>(dados.data()), dados.size());
}

int main(int argc, char** argv) {
    if (argc < 3) {
        std::cerr << "Uso: " << argv[0] << " <arquivo_entrada> <arquivo_saida>" << std::endl;
        return 1;
    }

    std::string arquivoEntrada = argv[1];
    std::string arquivoSaida = argv[2];

    std::vector<char> mensagem = lerArquivo(arquivoEntrada);
    int tamanhoMensagem = mensagem.size();

    lista dic_list;
    inicializa_dic(&dic_list);

    std::vector<unsigned char> mensagemComprimida(tamanhoMensagem * 2);
    int tamanhoComprimido = 0;

    int result = COMPRIME_LZW(&dic_list, mensagem.data(), tamanhoMensagem, mensagemComprimida.data(), &tamanhoComprimido);
    if (result != 0) {
        std::cerr << "Erro na compressão" << std::endl;
        return 1;
    }

    mensagemComprimida.resize(tamanhoComprimido);
    escreverArquivo(arquivoSaida, mensagemComprimida);

    std::cout << "Compressão concluída com sucesso!" << std::endl;
    std::cout << "Tamanho original: " << tamanhoMensagem << " bytes" << std::endl;
    std::cout << "Tamanho comprimido: " << tamanhoComprimido << " bytes" << std::endl;
    double taxaCompressao = 100.0 * (1.0 - (double)tamanhoComprimido / tamanhoMensagem);
    std::cout << "Taxa de compressão: " << taxaCompressao << "%" << std::endl;

    return 0;
}
