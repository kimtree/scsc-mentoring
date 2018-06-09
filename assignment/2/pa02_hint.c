#include <stdio.h>
#include <stdlib.h>
// TODO: 랜덤 생성용 헤더 추가
#include <unistd.h>
#include <time.h>

#define CARDS 52
#define BACK -1
//추가적인 전역변수 선언 금지
static char card_suit[4][4] = {"♠", "◆", "♥", "♣"};
// TODO: UTF-8이라서 그런지 특수문자 3byte + NULL 이라서 4바이트로 해줘야함 [4][3] -> [4][4]
static char card_num[13][3] = {"A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K"};

int deck[CARDS];
int money;

void print_card(int card);

// TODO: int card_count값에 따라서 숫자로 된 카드 포인트 가져오는 함수
int get_card_point(bool is_player, int card_count) {
	int card_point = 0;
	int start = is_player ? 1 : 0;

	for (int i = start; i < (2 * card_count); i += 2) {
		int card = deck[i] % 13;
		if (card == 0) {
			card_point += 11;
		} else if (card > 0 && card < 10) {
			card_point += card + 1;
		} else {
			card_point += 10;
		}
	}

	return card_point;
}

void show_cards(int dealer_card_count, int player_card_count, bool show_dealers_card) {
	printf("\nDealer : \n");
	for (int i = 0; i < (2 * dealer_card_count); i += 2) {
		// 첫 턴에는 딜러의 첫 카드를 보여주지 않음
		if (!show_dealers_card && i == 0) {
			print_card(BACK);
		} else {
			print_card(deck[i]);
		}
	}

	printf("\nCount: %d", get_card_point(false, dealer_card_count));

	printf("\nPlayer : \n");
	for (int i = 1; i < (2 * player_card_count); i += 2) {
		print_card(deck[i]);
	}

	printf("\nCount: %d", get_card_point(true, player_card_count));

}

bool is_bust(bool is_player, int card_count) {
	if (get_card_point(is_player, card_count) > 21) {
		printf("\n\n ====== (%s) BUST ====== \n\n", is_player ? "PLAYER" : "DEALER");
		return true;
	}

	return false;
}

void whos_win(int dealer_card_count, int player_card_count, int bet_cash, bool is_double_down) {
	int dealer_card_point = get_card_point(false, dealer_card_count);
	int player_card_point = get_card_point(true, player_card_count);

	if (dealer_card_count == 2 && dealer_card_point == 21) {
		printf("\n\n ====== BLACK JACK (DEALER WIN) ======\n\n");
	} else if (player_card_count == 2 && player_card_point == 21) {
		printf("\n\n ====== BLACK JACK (PLAYER WIN) ======\n\n");
		money = money - bet_cash + (bet_cash * 2) + (int) (bet_cash * 0.5);
	} else if (dealer_card_point > player_card_point) {
		printf("\n\n ====== DEALER WIN ======\n\n");
		printf("Player Lose : %d\n", bet_cash);
		money = money - bet_cash;
	} else if (player_card_point > dealer_card_point) {
		printf("\n\n ====== PLAYER WIN ======\n\n");

		// 승리 보상(베팅 * 2)
		if (is_double_down) {
			bet_cash *= 2;
		}
		printf("Player Earn : %d\n", (bet_cash * 2));
		money = money - bet_cash + (bet_cash * 2);
	} else {
		printf("\n\n ====== D R A W ======\n\n");
	}

	printf("\nPlayer Money : %d\n", money);
}

void swap(int *a, int *b) {
	int temp = *a;
	*a = *b;
	*b = temp;
}

int main(void)
{
	int i, j;
	// TODO: 52장의 무작위 카드 덱 만들기
	srand(time(NULL));
	for (i = 0; i < CARDS; i++) {
		deck[i] = i;
	}
	for (i = 0; i < CARDS; i++) {
		j = (rand() % CARDS);
		swap(&deck[i], &deck[j]);
	}

	// TODO: 소지한 캐시 초기화 및 출력
	money = 200;
	printf("Cash : %d\n", money);

	// TODO: 배팅 금액 입력 및 출력
	int bet_cash = 0;
	while (true) {
		printf("How much do you bet?\n");
		scanf("%d", &bet_cash);

		if (bet_cash > money) {
			printf(" ====== NOT ENOUGH MONEY ====== \n\n");
		} else if (bet_cash == 0) {
			printf(" ====== YOU HAVE TO BET ====== \n\n");
		} else {
			break;
		}
	}

	printf("Bet : %d\n", bet_cash);

	// TODO: 더블다운용 플래그
	bool is_double_down = false;

	// TODO: 딜러 - 패 2장 자동으로 받기
	int dealer_card_count = 2;

	// TODO: 플레이어 - 패 2장 자동으로 받기
	int player_card_count = 2;

	// TODO: 카드 출력
	show_cards(dealer_card_count, player_card_count, false);

	// TODO: 블랙잭 확인
	if (get_card_point(false, dealer_card_count) == 21 || get_card_point(true, player_card_count) == 21) {
		whos_win(dealer_card_count, player_card_count, bet_cash, is_double_down);
		return 0;
	}

	char choose;

	while (true) {
		// TODO: 고르기
		printf("\n\nChoose One [h: hit, s: Stay, d: Double down]\n");
		scanf(" %c", &choose);

		if (choose == 'h') {
			// TODO: 유저 카드 한 장 더 받기
			player_card_count++;

			// TODO: 카드 출력
			show_cards(dealer_card_count, player_card_count, true);

			// TODO: 유저의 BUST 조건
			if (is_bust(true, player_card_count)) {
				break;
			}

			if (is_double_down) {
				// TODO: 게임 종료 조건
				printf("\n\n ====== DOUBLE DOWN ACTIVATED ======\n\n");

				whos_win(dealer_card_count, player_card_count, bet_cash, is_double_down);
				break;
			}
		} else if (choose == 's') {
			printf("\nDealer's Turn\n");
			// TODO: 딜러의 카드 포인트가 16 이하이면 hit / 그 이상은 stay
			while (get_card_point(false, dealer_card_count) <= 16) {
				dealer_card_count++;
			}

			// TODO: 카드 출력
			show_cards(dealer_card_count, player_card_count, true);

			// TODO: 딜러의 BUST 조건
			if (is_bust(false, dealer_card_count)) {
				// 승리 보상(베팅 * 2)
				printf("Player Earn : %d\n", (bet_cash * 2));
				break;
			}

			// TODO: 승패 비교
			whos_win(dealer_card_count, player_card_count, bet_cash, is_double_down);
			break;
		} else if (choose == 'd') {
			if (player_card_count != 2 || money < bet_cash || is_double_down) {
				printf("\n\n ====== NOT AVAILABLE ====== \n\n");
			}
			is_double_down = true;

		} else if (choose == 'q') {
			break;
		}
	}

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
		// TODO: 그림대로 나오려면 숨겨진 아이콘 뒤에 \t가 추가 되어야 함
		printf("▒▒\t");
	else
		printf("%s%2s\t", card_suit[card/13], card_num[card%13]);
}


