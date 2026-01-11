// Last updated: 1/11/2026, 12:37:15 PM
bool isPalindrome(char* s) {
    #include <stdio.h>
    #include <string.h>
    #include <ctype.h>

    int left = 0;
    int right = strlen(s) - 1;

    while (left < right) {
        while (left < right && !isalnum(s[left])) {
            left++;
        }
        while (left < right && !isalnum(s[right])) {
            right--;
        }
        if (tolower(s[left]) != tolower(s[right])) {
            return false;
        }
        left++;
        right--;
    }

    return true;
}