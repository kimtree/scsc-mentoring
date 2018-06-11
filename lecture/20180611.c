#include <stdio.h>

void change_array(int *arr) {
	for (int i=0; i < 4; i++) {
		arr[i] = arr[i] * 2;
	}
}

void change_int_by_value(int a) {
	printf("change_int_by_value pointer: %10p", &a);
	a = a * 2;
}

void change_int_by_reference(int *a) {
	printf("change_int_by_reference pointer: %10p", a);
	*a = *a * 2;
}

int main(void) {
	// 배열
	int array[4] = {1, 2, 3, 4};
	// 포인터 변수
	int *ptr;
	int index;

	int a = 2;

	printf("int a: %d\n", a);
	printf("original %10p\n", &a);
	change_int_by_reference(&a);
	printf("\nint a: %d\n", a);

	// int = 4bytes sizeof (int)

	// array == &dates[0]
	ptr = array;

	// &array[0] = 0x00
	// &array[1] = 0x04
	// &array[2] = 0x08
	// &array[3] = 0x0c

	// ptr = 0x00

	// *(ptr + index) = ptr + (index * sizeof (int))
	// if index == 2

	// * => value
	// *(ptr + 2) = *(ptr + (2 * sizeof (int)))
	// *(ptr + 2) = *(0x00 + ( 2 * 4 )) = *(0x08) ==> 3 ==> array[2]

	// no * => address
	// ptr + 2 = 0x00 + (2 * sizeof (int)) = 0x00 + (2 * 4) == 0x08

	for (index = 0; index < 4; index++) {
		printf("pointers + %d: %4d %4d %10p %10p\n", index,
			*(ptr + index), array[index],
			ptr + index, &array[index]
		);
	}

	change_array(array);
	printf("\n\n After call change_array func\n\n");

	for (index = 0; index < 4; index++) {
		printf("pointers + %d: %4d %4d %10p %10p\n", index,
			*(ptr + index), array[index],
			ptr + index, &array[index]
		);
	}

	printf("\n\nsizeof array: %4lu \n", sizeof (array));
	printf("sizeof int: %4lu \n", sizeof (int));
	printf("sizeof array element (e.g. array[0]): %4lu \n", sizeof (array) / sizeof (int));

	return 0;
}
