#include <stdio.h>

int main() {
    // Write C code here
    int num,contador,factorial = 1;
    
    printf("introduzca un numero para calcular el factorial: \n");
    scanf("%i",&num);
    
    for(contador = num;contador>1;contador--){
    
        factorial = factorial*contador;
    }
     printf("el factorial de %i es = %i\n",num,factorial);
}