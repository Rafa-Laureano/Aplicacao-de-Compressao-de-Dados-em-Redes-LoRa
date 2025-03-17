
//#define GPS 1
//#define LOG 1

#ifdef GPS
	#define TAB_OFFSET 15
#else
	#ifdef LOG
		#define TAB_OFFSET 38
	#else
		#define TAB_OFFSET 65
	#endif
#endif

extern int free_heap;

/*
 * Função que cria a tabela de probabilidade
 * char *v : mensagem a ser comprimida
 * unsigned short *t : vetor que armazenará as probabilidade do símbolos
 * return : 
 * 0 : Não houve estouro
 * 1 : Houve estouro
 */
int tabela(char *v, unsigned short *t);
void print_tab(unsigned short *v);
