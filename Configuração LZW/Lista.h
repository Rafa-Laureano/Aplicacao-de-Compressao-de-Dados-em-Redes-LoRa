#ifndef LISTA_H
#define LISTA_H

#include <cstring> // Para funções de manipulação de strings

typedef struct no {
    char dado[256]; // Definição de um dado no nó
    no* prox;
} no;

typedef struct lista {
    no* head;
    int size;
} lista;

// Declarações das funções para manipulação da lista
void inicializa_dic(lista* dic_list);
int insere_elemento_lista_ordenado(lista* dic_list, char* str, int len);
int remove_termo(lista* dic_list);
int busca_dicionario(lista* dic_list, char* string, int* index);

#endif // LISTA_H
