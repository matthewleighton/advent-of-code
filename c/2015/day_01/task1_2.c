#include <stdio.h>

int main(void) {
	FILE * fp;
	char c;
	int floor = 0;
	int entered_basement = 0;
	int i = 0;

	fp = fopen("data.txt", "r");
	while(1) {
		c = fgetc(fp);
		if (feof(fp)) {
			break;
		}

		if (c == '(') {
			floor++;
		} else if (c == ')') {
			floor--;
		}
		i++;

		if (floor < 0 && !entered_basement) {
			entered_basement = i;
		}
	}
	fclose(fp);

	printf("End on floor %d\n", floor);
	printf("Entered basement on move %d\n", entered_basement);

}