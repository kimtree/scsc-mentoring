#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
#include <time.h>

#define NUMBER_SIZE 3

int generateRandomNumber() {
	int randomNumber;

	// 랜덤 숫자 생성을 위한 씨드 설정
	srand(time(NULL));
	// 100 ~ 999 = 0 ~ 899 + 100
	randomNumber = rand() % 900 + 100;

	return randomNumber;
}

int getNumberFromUser() {
	int number;

	printf("Guess number (000 ~ 999): ");
	scanf("%d", &number);

	return number;
}

bool checkNumber(int inputNumber, int randomNumber) {
	int strikeCount, ballCount;
	int copiedRandomNumber = randomNumber;

	// 3자리 숫자임을 가정해서 숫자를 배열에 자릿수 별로 담아둠
	int inputNumberArray[NUMBER_SIZE];
	int randomNumberArray[NUMBER_SIZE];
	int i ;
	for (i = 0; i < NUMBER_SIZE; i++) {
		inputNumberArray[i] = inputNumber % 10;
		inputNumber = inputNumber / 10;

		randomNumberArray[i] = randomNumber % 10;
		randomNumber = randomNumber / 10;
	}

	for (i = 0; i < NUMBER_SIZE; i++) {
		// 자릿수와 숫자가 일치하면 스트라이크 1 증가
		if (inputNumberArray[i] == randomNumberArray[i]) {
			strikeCount += 1;
		} else {
			// 자릿수와 숫자가 일치하지 않으면 해당 숫자가 randomNumber 안에 있는지 체크함
			for (int j=0; j < 3; j++) {
				if (j != i && inputNumberArray[i] == randomNumberArray[j]) {
					ballCount += 1;
				}
			}
		}
	}

	if (strikeCount == 3) {
		// 3자리 숫자를 다 맞춘 경우
		printf("Correct, answer is %d\n", copiedRandomNumber);
	} else if (strikeCount > 0 || ballCount > 0) {
		// 일치하는 숫자가 1개라도 있는 경우
		printf("%d strike, %d ball\n", strikeCount, ballCount);
	} else {
		// 입력된 숫자가 랜덤 숫자에 하나도 포함되어있지 않은 경우
		printf("Out!\n");
	}

	return (strikeCount == 3);
}

int main(void) {
	char playYn;
	bool result;
	int inputNumber;
	int randomNumber = generateRandomNumber();

	printf("==================\n");
	printf("S T A R T\n");

	while(1) {
		inputNumber = getNumberFromUser();
		result = checkNumber(inputNumber, randomNumber);

		// 3 Strike인 경우 성공
		if (result) {
			printf("Play again? (y or n): ");
			scanf("%s", &playYn);

			if (playYn == 'n') {
				break;
			}

			// 새 랜덤 숫자를 생성
			randomNumber = generateRandomNumber();
		}
	}

    return 0;
}