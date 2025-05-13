#include <stdio.h>
#include <stdlib.h>
#include <string.h>

void create_file() {
    FILE *file = fopen("salida.txt", "w");

    fprintf(file, "Sistemas Operativos.");
    fclose(file);
}

int main() {
    // ----- malloc
    int *p = malloc(sizeof(int));
    *p = 5;
    printf("%d\n", *p);
    free(p);
    
    // ----- char inmutable  
    char *str = "Hola";
    // str[0] = 'h';
    printf("%s\n", str);

    // ----- TEST con char  
    char str2 = 'H';
    printf("char en comillas simples: %c\n", str2);

    char str3[] = "Hola";
    strcpy(str3, "holis");
    strcat(str3, ", ");
    strcat(str3, "que mas");
    
    printf("String con modificaciones: %s\n", str3);  // Imprime: Hola Mundo

    // ----------------
    create_file();
}

