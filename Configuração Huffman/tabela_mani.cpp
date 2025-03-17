#include "tabela_mani.h"
#include "stdio.h"
#include "stdlib.h"
#include "string.h"

#define MAX_CNT 65535

int tabela(char *v, unsigned short *t){
	/* # VALOR - 48 DO ASCII
	0-0
	1-1
	2-2
	3-3
	4-4
	5-5
	6-6
	7-7
	8-8
	9-9
	10- - 45 = -3
	11 -< 60 = 12
	12 -> 62 = 14
	13 -& 38 = -10
	14 -. 46 = -1

	*/
	char *token;
	token = strtok(v, "#");
	v = token;

	int size = strlen(v);
	int aux = 0;
	
#ifdef GPS
	int ALFA = 0;
#else
	#ifdef LOG
		int ALFA = 26;
	#else
		int ALFA = 52;
	#endif
#endif
	
	for(int i = 0; i < size; i++){
		
		// 48 a 57
		if((v[i] >= 48 && v[i] <= 57)){
			//printf("CARACTERES DE 0 A 9.....\n");
			aux = v[i] - 48; //ASCII PARA BINARIO NORMAL
			t[aux] += 1;
			//printf("caracteres de 0 a 9: %d - %d\n", aux, t[aux]);
			if(t[aux]>MAX_CNT){
				printf("\n TAMANHO MAX %c %d %d\n", v[i], aux, t[aux]);
				return 1;
			}
			continue;
		}

#ifndef GPS
		// 65 a 90
		if(v[i] >= 65 && v[i] <= 90){
			//printf("CARACTERES DE A A Z.....\n");
			aux = v[i] - 65 + 10; //ASCII PARA BINARIO NORMAL
			
			//printf("A a Z - aux: %d - v: %c\n", aux, v[i]);
			
			t[aux] += 1;
			if(t[aux]>MAX_CNT){
				printf("\n TAMANHO MAX %d %d\n", aux, t[aux]);
				return 1;
			}
			continue;
		}

#ifndef LOG
		// 97 a 122
		if(v[i] >= 97 && v[i] <= 122){ // 10 + 26
			//printf("CARACTERES DE a A z.....\n");
			aux = v[i] - 97 + 10 + 26; //ASCII PARA BINARIO NORMAL
			
			//printf("a a z - aux: %d - v: %c\n", aux, v[i]);
			
			t[aux] += 1;
			if(t[aux]>MAX_CNT){
				printf("\n TAMANHO MAX %d %d\n", aux, t[aux]);
				return 1;
			}
			continue;
		}
#endif
#endif

		aux = v[i] - 48; //ASCII PARA BINARIO NORMAL		
		if(aux == -38) { // 65 (ASCII 10: Line Feed - \n)
			t[10 + ALFA]+=1;		
			if(t[10 + ALFA]>MAX_CNT){
				printf("\n TAMANHO MAX %d \n",t[10 + ALFA]);
				return 1;
			}
			continue;
		}		
		
#ifndef LOG
		if(aux == -3) { // 63 (ASCII 45: -)
			t[10 + ALFA + 1]+=1;
			if(t[10 + ALFA + 1]>MAX_CNT){
				printf("\n TAMANHO MAX %d \n",t[10 + ALFA + 1]);
				return 1;
			}
			continue;
		}
#endif
		
#ifdef GPS
		if(aux == -2){ // 62 (ASCII 46: .)
			t[10 + ALFA + 2]+=1;
			if(t[10 + ALFA + 2]>MAX_CNT){
				printf("\n TAMANHO MAX %d \n",t[10 + ALFA + 2]);
				return 1;
			}
			continue;
		}

		if(aux == -4) { // 64 (ASCII 44: ,)
			t[10 + ALFA + 3]+=1;
			if(t[10 + ALFA + 3]>MAX_CNT){
				printf("\n TAMANHO MAX %d \n",t[10 + ALFA + 3]);
				return 1;
			}
			continue;
		}
#endif

		printf("\n CARACTER NÃO RECONHECIDO: %d\n", v[i]);
		printf("ELE NÃO SERÁ ARMAZENADO NA TABELA!!!.....\n");
	}

	return 0;
}

void print_tab(unsigned short *v){

	for(int i=0;i<10;i++)
		printf("\n %d %d \n",i,v[i]);
	printf("\n %c %d \n",'-',v[10]);
	printf("\n < %d \n",v[11]);
	printf("\n > %d \n",v[12]);
	printf("\n & %d \n",v[13]);
	printf("\n . %d \n",v[14]);
}
