#include<stdio.h>
#include<stdlib.h>

#define CARDS 52
#define BACK -1
//추가적인 전역변수 선언 금지
static char card_suit[4][3] = {"♠", "◆", "♥", "♣"};
static char card_num[13][3] = {"A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K"};

int deck[CARDS];
int money;

void print_card(int card);


int main(void)
{
	print_card(BACK);
	print_card(0);


	return 0;
}


/*
제공, 카드 한 장 출력
매개변수 card는 int형 변수로 0~51의 범위를 가지며 트럼프 카드 총 52장을 나타낸다
카드 모양의 순서는  ♠, ◆, ♥, ♣이고 각각의 모양에서 A, 2, 3, ……, 10, J, Q, K 이다
ex) 0 ->  ♠A,  1 -> ♠2,  51 -> ♣K
*/
void print_card(int card){
	if (card == BACK)
		printf("▒▒");
	else
		printf("%s%2s\t", card_suit[card/13], card_num[card%13]);
}


