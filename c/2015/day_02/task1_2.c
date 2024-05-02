#include <stdio.h>
#include <string.h>
#include <stdlib.h>

#define MAX_LINE_LENGTH 10

int get_lengths(char line[9], int lengths[3]) {
	const char delim = 'x';
	char *token = strtok(line, &delim);
	int i = 0;
	while (token != NULL) {
		lengths[i] = atoi(token);
		token = strtok(NULL, &delim);
		i++;
	}
	return 0;
}

int compare(const void *a, const void *b) {
	return ( *(int*)a - *(int*)b );
}

int get_sides(int lengths[3], int sides[3]) {
	sides[0] = lengths[0] * lengths[1];
	sides[1] = lengths[0] * lengths[2];
	sides[2] = lengths[1] * lengths[2];

	qsort(sides, 3, sizeof(int), compare);

	return 0;
}

int get_loops(int lengths[3], int loops[3]) {
	loops[0] = 2 * (lengths[0] + lengths[1]);
	loops[1] = 2 * (lengths[0] + lengths[2]);
	loops[2] = 2 * (lengths[1] + lengths[2]);

	qsort(loops, 3, sizeof(int), compare);
	return 0;
}

int main(void) {
	FILE * fp;
	char line[MAX_LINE_LENGTH];
	int lengths[3];
	int sides[3];
	int loops[3];
	int task_1_total = 0;
	int task_2_total = 0;

	fp = fopen("data.txt", "r");
	if (fp == NULL) {
		perror("Error opening file");
		return 1;
	}

	while (fgets(line, sizeof(line), fp) != NULL) {
		get_lengths(line, lengths);
		get_sides(lengths, sides);
		task_1_total += 2 * (sides[0] + sides[1] + sides[2]) + sides[0];

		get_loops(lengths, loops);
		task_2_total += loops[0] + (lengths[0] * lengths[1] * lengths[2]);
	}
	fclose(fp);

	printf("Task 1: %d\n", task_1_total);
	printf("Task 2: %d\n", task_2_total);
	return 0;
}

