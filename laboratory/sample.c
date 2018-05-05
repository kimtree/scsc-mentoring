#include <stdio.h>
#include <stdlib.h>
#include <time.h>

int main(void) {
    int num;

    srand(time(NULL));
    num = (rand() % 50) + 1;

    printf("<Generation of a random number between 1 and 50 \n");
    printf("Random number: %d\n", num);

    return 0;
}