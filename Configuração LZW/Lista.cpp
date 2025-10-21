#include "Lista.h"
#include <cstdlib> // Para alocação de memória

void inicializa_dic(lista* dic_list) {
    dic_list->head = nullptr;
    dic_list->size = 0;
}

int insere_elemento_lista_ordenado(lista* dic_list, char* str, int len) {
    no* novo_no = (no*)malloc(sizeof(no));
    if (novo_no == nullptr) {
        return 1; // Falha na alocação
    }
    strncpy(novo_no->dado, str, len);
    novo_no->dado[len] = '\0';
    novo_no->prox = dic_list->head;
    dic_list->head = novo_no;
    dic_list->size++;
    return 0; // Sucesso
}

int remove_termo(lista* dic_list) {
    // Implementação da função de remoção
    return 0;
}

int busca_dicionario(lista* dic_list, char* string, int* index) {
    no* atual = dic_list->head;
    *index = 0;
    while (atual != nullptr) {
        if (strcmp(atual->dado, string) == 0) {
            return 0; // Encontrado
        }
        atual = atual->prox;
        (*index)++;
    }
    return 1; // Não encontrado
}
