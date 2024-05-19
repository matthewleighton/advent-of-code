#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int get_file_size(FILE * fp) {
	int file_size;

	fseek(fp, 0, SEEK_END);
	file_size = ftell(fp);
	fseek(fp, 0, SEEK_SET);

	return file_size;
}

int move_santa(FILE* fp, int* px, int* py) {
	char c = fgetc(fp);

	if (feof(fp)) {
		return 0;
	}

	switch(c) {
		case '^':
			(*py)++;
			break;
		case 'v':
			(*py)--;
			break;
		case '>':
			(*px)++;
			break;
		case '<':
			(*px)--;
			break;
	}
	
	return 1;
}

void switch_santa(int* santa_number, int task_number) {
	if (task_number == 1) {
		return;
	}
	if (*santa_number == 0) {
		(*santa_number)++;
	} else {
		(*santa_number)--;
	}
}

int main(void) {
	FILE*  fp;
	int x[2] = {0, 0};
	int y[2] = {0, 0};
	int total_visited = 1;
	int file_size;
	char** visited;
	char coord[10];
	int in_visited = 0;
	int santa_number = 0;
	int task_number;

	printf("Select a task number (1 or 2): ");
	scanf("%d", &task_number);
	if (task_number != 1 && task_number != 2) {
		printf("Invalid task number. Exiting.\n");
		return 1;
	}
	
	fp = fopen("data.txt", "r");
	if (fp == NULL) {
		perror("Error opening file");
		return 1;
	}
	file_size = get_file_size(fp);

	// Request memory for an array containing file_size number of items, each with a size of char*
	visited = (char**)malloc(file_size * sizeof(char*));
	if (visited == NULL) {
		fprintf(stderr, "Memory allocation failed");
		return 1;
	}
	visited[0] = "0 0";

	while(1) {
		if (!move_santa(fp, &x[santa_number], &y[santa_number])) {
			break;
		}
		sprintf(coord, "%d %d", x[santa_number], y[santa_number]);

		in_visited = 0;
		for (int j = 0; j < file_size; j++) {
			if (visited[j] == NULL) {
				break;
			}
			if(strcmp(visited[j], coord) == 0) {
				in_visited = 1;
				break;
			}
 		}

		if (!in_visited) {
			visited[total_visited] = (char*)malloc(10 * sizeof(char));
			sprintf(visited[total_visited], "%d %d", x[santa_number], y[santa_number]);
			total_visited++;
		}

		switch_santa(&santa_number, task_number);
	}

	printf("Total visited: %d\n", total_visited);
}