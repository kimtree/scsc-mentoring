#include <stdio.h>

int main(void) {
	int i, j;
	int number;

	printf("Please input the last number\n");
	scanf("%d", &number);

	printf("-------- start --------\n");

	for (i = 1; i <= number; i++) {
		int clapCount = 0;
		// i 값을 calcNum에 복사
		int calcNum = i;

		while (calcNum > 0) {
			// 1의 자릿수
			int extra = calcNum % 10;

			// 3, 6, 9가 포함된 경우
			if (extra == 3 || extra == 6 || extra == 9) {
				// 박수 카운트 증가
				clapCount++;
			}

			calcNum = calcNum / 10;
		}

		// 박수 칠 카운트가 있는 경우
		if (clapCount > 0) {
			for (j = 0; j < clapCount; j++) {
				printf("clap ");
			}
			printf("\n");
		} else {
			printf("%d \n", i);
		}
	}

	return 0;
}