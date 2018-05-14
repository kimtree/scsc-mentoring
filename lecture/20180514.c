#include <stdio.h>
#include <unistd.h>

int main(void) {
	int i;
	/*
	for ([[ 1 ]]; [[ 2 > 5 ]]; [[ 4 > 7 ]]) {
		[[ 3 > 6 ]]
		printf("Num: %d \n", i);
	}
	*/
	for (i = 5; i < 10; i++) {
		printf("Num: %d \n", i);
	}

	int score = 88;
	char grade;
	if (score > 95) {
		grade = 'A';
	} else if (score > 80) {
		grade = 'B';
	} else if (score > 70) {
		grade = 'C';
	} else {
		grade = 'F';
	}

	/* Bit */
	unsigned int c = 4; // 100
	unsigned int d = 1; // 001
	printf(" %d \n", c | d);
	printf(" %d \n", c & d);

	/*
	if a > 10 and b > 20:
		pass
	*/
	int a = 15;
	int b = 30;
	if (a > 10 && b > 20) {
		printf("a > 10 && b > 20\n");
	}
	if (a > 10 || b > 20) {
		printf("a > 10 && b > 20\n");
	}

	/* Print format */
	/* decimal, float */
	printf("%d %.2f %4d\n", 10, 1.23456, 122);

	/* Character */
	char alpha = 'a';
	/* String size + 1(null \0) */
	char alphaString[6] = "alpha";

	int f = 10;
	printf("%d\n", ++f); // 11
	printf("%d\n", f++); // 11 -> 12

	// f = 10
	// printf -> format string -> ++f -> f = f + 1 -> get f(f = 11) -> print
	// f = 11
	// printf -> format string -> get f -> print (f = 11) -> f = f + 1
	// f = 12

    return 0;
}