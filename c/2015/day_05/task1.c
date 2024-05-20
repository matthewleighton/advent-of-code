#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <stdbool.h>

#define STRING_LENGTH 18


int contains_three_vowels(char string[STRING_LENGTH]) {
	char vowels[5] = "aeiou";
	int vowel_count = 0;
	for (int i = 0; i < strlen(string); i++) {
		if (strchr(vowels, string[i]) !=  NULL) {
			vowel_count++;
		}
		if (vowel_count >= 3) {
			return true;
		}
	}
	return false;
}

int contains_repeat_letter(char string[STRING_LENGTH]) {
	for (int i = 1; i < strlen(string); i++) {
		if (string[i] == string[i-1]) {
			return true;
		}
	}
	return false;
}

int contains_forbidden_string(char string[STRING_LENGTH]) {
	char forbidden_strings[4][3] = {"ab", "cd", "pq", "xy"};
	for(int i = 0; i < 4; i++) {
		if (strstr(string, forbidden_strings[i]) != NULL) {
			return true;
		} 
	}
	return false;
}

int is_string_nice(char string[STRING_LENGTH]) {
	if (!contains_three_vowels(string)) {
		return false;
	}
	if (!contains_repeat_letter(string)) {
		return false;
	}
	if (contains_forbidden_string(string)) {
		return false;
	}
	return true;
}

int main(void) {
	FILE* fp;
	int nice_count = 0;
	char string[STRING_LENGTH];

	fp = fopen("data.txt", "r");

	while (fgets(string, sizeof(string), fp) != NULL) {
		if (is_string_nice(string)) {
			nice_count++;
		}
	}

	printf("There are %d nice strings.\n", nice_count);
}