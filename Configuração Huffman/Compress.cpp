#include "Compress.h"

void compress_dado(char *string_descom, unsigned int *tamanho_dado_compactado, unsigned short *bits, unsigned short *aux_cod, unsigned short *mensagem_code, node *arvore) {

	int soma = 0;
	int i = 0;
	char b[10] = {0};
	while(string_descom[i]){
		int tamanho = 0;

		pega_binario(arvore,b,tamanho,string_descom[i],&soma);
		
		//printf("tamanho: %d - string_descom[%d]: %c - b: %s\n", tamanho, i, string_descom[i], b);
          
		i++;
		for(char *c = b; *c; c++){
            if(*c == '1'){
				*aux_cod = *aux_cod | (1 << *bits % 16); // MSB
            }

            *bits = *bits - 1; // VOU DECREMENTANDO E QUANDO CHEGA A NEGATIVO VAI PRA 65535
            
            if(*bits == 65535){
                *bits = 15;
				//printf("----> *aux_cod: %x\n", *aux_cod);
                mensagem_code[TAB_OFFSET + *tamanho_dado_compactado] = *aux_cod;
				//printf("----> mensagem_code[%d]: %x\n", *tamanho_dado_compactado, mensagem_code[TAB_OFFSET + *tamanho_dado_compactado]);
                *tamanho_dado_compactado = *tamanho_dado_compactado + 1; // conta um short a cada incremento.
                *aux_cod = 0;
            }
		}
    }
	
	//printf("*bits: %d\n",*bits);
	
    if(*bits != 15){
        mensagem_code[TAB_OFFSET-1] = 15 - *bits; // SALVA A QUANTIDADE DE BITS A CONSIDERAR NO ULTIMO
		//printf("----> *aux_cod: %x\n", *aux_cod);
        mensagem_code[TAB_OFFSET + *tamanho_dado_compactado] = *aux_cod;
		//printf("----> mensagem_code[%d]: %x\n", *tamanho_dado_compactado, mensagem_code[TAB_OFFSET + *tamanho_dado_compactado]);
        (*tamanho_dado_compactado)++;
	} else {
		mensagem_code[TAB_OFFSET-1] = 0;  // SE NAO SOBRE NENHUM BYTE INCOMPLETO COLOCA AQUI
    }
}

int descompacta(char **mensagem_decode, unsigned short *mensagem_comprimida, int tamanho_arq, int qtd_msn, int *char_counter){
    
	unsigned short tabela_compac[TAB_OFFSET] = {0}; // TABELA

    for(int i = 0; i < TAB_OFFSET-1; i++){ // SALVANDO TABELA
		tabela_compac[i] = mensagem_comprimida[i];
    }
        
	////////////// CONSTROI LISTA
    lista ordena_comp;
    ordena_comp.head = NULL;
    ordena_comp.calda = NULL;
	
#ifdef GPS
	int ALFA = 10;				
#else
	#ifdef LOG
		int ALFA = 36;
	#else
		int ALFA = 62;
	#endif
#endif

    for(int i = 0; i < TAB_OFFSET-1; i++){
		// insere na lista apenas se for um elemento válido, ou seja, haja bytes
		if(tabela_compac[i]){
			if(i < 10){
				insere_elemento_lista_ordenado(&ordena_comp,cria_no(tabela_compac[i],48+i,NULL,NULL,NULL));
#ifndef GPS				
			} else if(i >= 10 && i <= 35){
				insere_elemento_lista_ordenado(&ordena_comp,cria_no(tabela_compac[i],65+i-10,NULL,NULL,NULL));
#ifndef LOG
			} else if(i >= 36 && i <= 61){
				insere_elemento_lista_ordenado(&ordena_comp,cria_no(tabela_compac[i],97+i-36,NULL,NULL,NULL));
#endif
#endif
			} else if(i==ALFA){
				insere_elemento_lista_ordenado(&ordena_comp,cria_no(tabela_compac[i],10,NULL,NULL,NULL));
#ifndef LOG				
			} else if(i==ALFA+1){
				insere_elemento_lista_ordenado(&ordena_comp,cria_no(tabela_compac[i],45,NULL,NULL,NULL));	
#endif

#ifdef GPS
			} else if(i==ALFA+2){   
				insere_elemento_lista_ordenado(&ordena_comp,cria_no(tabela_compac[i],46,NULL,NULL,NULL));
			} else if(i==ALFA+3){   
				insere_elemento_lista_ordenado(&ordena_comp,cria_no(tabela_compac[i],44,NULL,NULL,NULL));
#endif
			} else {
				//printf("Caractere não inserido na lista!!!: %d, %d\n", t[i], i);
			}
		}
    }

    // LISTA ORDENADA DA TABELA
    no *aux = ordena_comp.head;
    constroi_arvore(&ordena_comp);

    unsigned int tamanho_bits_comp = tamanho_arq*8; // Tamanho em bits do arquivo.

    if(mensagem_comprimida[TAB_OFFSET-1] != 0) {// POSICAO QUE CONTEM O TAMANHO DE BITS USADOS NO ULTIMO BYTE
        tamanho_bits_comp = tamanho_bits_comp - (16-mensagem_comprimida[TAB_OFFSET-1]);
		//printf("AQUIIII!!!\n");
		//tamanho_bits_comp = tamanho_bits_comp - 3;
	}
       
    int count_ = 0;
    unsigned short bit_atual = 15;
    unsigned short aux_char = 0, aux_2 = 0;
    int pos = 2*TAB_OFFSET*8; // contador de bits.
    char *mensagem_descom = (char*) calloc(35*qtd_msn, sizeof(char));
	
    if(mensagem_descom == NULL) {
		return 2;
    }
	
    while(pos < tamanho_bits_comp){
		
        node *atual = ordena_comp.head->dado; // RAIZ DA ARVORE
		
        while(atual->left || atual->right){
			
            if(pos%16 == 0){
                aux_char = mensagem_comprimida[pos/16]; // ATUALIZA TODA VEZ QUE COMPLETA 2 BYTES
				//printf("aux_char: %x\n", aux_char);
            }
              
            aux_2 = aux_char & (1 << bit_atual); // AND DO BIT ATUAL
              
            bit_atual--;
            if(bit_atual == 65535)
				bit_atual = 15; // COMECA O NOVO BYTE

            if(aux_2){
                atual = atual->right;
            } else {
				atual = atual->left;
            }
            pos++;
        }
    
        mensagem_descom[count_] = atual->caracter;
		
		//printf("mensagem_descom[count_]: %c\n", mensagem_descom[count_]);
		
        count_++;
    }

    mensagem_descom[count_] = '\0';
	
	*char_counter = count_;

    FreeHuffmanTree(ordena_comp.head->dado); // APAGA ARVORE OS NOS DA ARVORE
    free(ordena_comp.head); // APAGA ESSE ELEMENTO
    
    *mensagem_decode = mensagem_descom;
        
    return 1;
}
