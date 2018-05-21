#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
#include <time.h>

int main(void) {
	int num;
	int condition = 15;

	if (condition > 10) {
		num = 3;
	} else {
		num = 6;
	}

	printf("condition= %d / num= %d \n", condition, num);

	condition = 5;

	// 3항 연산자
	num = (condition > 10) ? 3 : 6;

	printf("condition= %d / num= %d \n", condition, num);

	// ch >= 'a' && ch <= 'z'
	char character = 'c';

	// a - 97 / A - 65 (32 차이)
	if (character >= 'a' && character <= 'z') {
		printf("lower case alphabet! \n");
		printf("%c %d\n", character - 32, character - 32);
	} else {
		printf("%c %d\n", character + 32, character + 32);
	}

	// switch ~ case
	char grade = 'A';
	int score;

	if (grade == 'A' || grade = 'a') {
		score = 95;
	} else if (grade == 'B' || grade = 'b') {
		score = 85;
	} else if (grade == 'C' || grade = 'c') {
		score = 75;
	} else {
		score = 0;
	}

	printf("Grade: %c / Score: %d\n", grade, score);

	grade = 'a';
	switch (grade) {
		case 'a':
		case 'A':
			score = 95;
			break;
		case 'b':
		case 'B':
			score = 85;
			break;
		case 'c':
		case 'C':
			score = 75;
			break;
		default:
			printf("Default called\n");
			score = 0;
	}

	printf("Grade: %c / Score: %d\n", grade, score);

    return 0;
}