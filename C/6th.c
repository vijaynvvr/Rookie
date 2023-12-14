#include <stdio.h>

int main() 
{
    printf("char = %d\n", sizeof(char));
    printf("unsigned char = %d\n", sizeof(unsigned char));
    printf("int = %d\n", sizeof(int));
    printf("short int = %d\n", sizeof(short int));
    printf("long int = %d\n", sizeof(long int));
    printf("unsigned int = %d\n", sizeof(unsigned int));
    printf("float = %d\n", sizeof(float));
    printf("double = %d\n", sizeof(double));
    printf("long double = %d", sizeof(long double));
    
    return 0;
}