#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <stdbool.h>

#define STRING_LENGTH 18

int contains_repeat_pair(char string[STRING_LENGTH]) {
  for (int i = 0; i < strlen(string) - 2; i++) {
    for (int j = i + 2; j < strlen(string); j++) {
      if (string[i] == string[j] && string[i+1] == string[j+1]) {
        return true;
      }
    }
  }
  return false;
}

int contains_separated_repeat_character(char string[STRING_LENGTH]) {
  for (int i = 0; i < strlen(string) - 2; i++) {
    if (string[i] == string[i+2]) {
      return true;
    }
  }
  return false;
}

int is_string_nice(char string[STRING_LENGTH]) {
  if (!contains_repeat_pair(string)) {
    return false;
  }
  if (!contains_separated_repeat_character(string)) {
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
