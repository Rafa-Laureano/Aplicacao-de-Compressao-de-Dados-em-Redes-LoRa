#include "Compress.h"
#include <cstring>
#include <cstdlib>
#include <cstdio>

int COMPRIME_LZW(lista* dic_list, char* mensagem, int tamanho_mensagem, unsigned char* mensagem_comprimida, int* tamanho_comprimido) {
    char* mensagem_aux = (char*)calloc(256, sizeof(char));
    if (mensagem_aux == nullptr) {
        printf("FALHA NA ALOCAÇÃO COMPRIME_LZW\n");
        return 1;
    }
    memset(mensagem_aux, 0, sizeof(char) * 256);
    strncpy(mensagem_aux, mensagem, 1);
    *tamanho_comprimido = 0;
    
    for (int i = 1; i < tamanho_mensagem; i++) {
        char c = mensagem[i];
        strncat(mensagem_aux, &c, 1);
        
        int index;
        if (busca_dicionario(dic_list, mensagem_aux, &index) != 0) {
            insere_elemento_lista_ordenado(dic_list, mensagem_aux, strlen(mensagem_aux));
            mensagem_comprimida[*tamanho_comprimido] = index;
            (*tamanho_comprimido)++;
            memset(mensagem_aux, 0, sizeof(char) * 256);
            strncpy(mensagem_aux, &mensagem[i], 1);
        }
    }
    free(mensagem_aux);
    return 0;
}
