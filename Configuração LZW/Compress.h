#ifndef COMPRESS_H
#define COMPRESS_H

#include "Lista.h"

int COMPRIME_LZW(lista* dic_list, char* mensagem, int tamanho_mensagem, unsigned char* mensagem_comprimida, int* tamanho_comprimido);

#endif // COMPRESS_H
