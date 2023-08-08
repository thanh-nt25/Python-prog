#include <stdio.h>
#include <string.h>
#include <ctype.h>

int is_cyclone_word(char* word){
    int len = strlen(word);
    printf("%d\n", len);
    int left = 0;
    int right = len-1;

    while (left < right)
    {   
        if (word[left] > word[right]){
            return 0;
        }
        left += 1;
        right -=1;
    }

    left=1; right = len-1;
    while (left < right)
    {
        if (word[left] < word[right]){
            return 0;
        }
        left += 1;
        right -=1;
    }


    return 1;
}

// 0, n, 1, n-1, 2, n-2 
/* a=1, b = n (index)
left=w[a], right = w[b]
a=1, b=n
left<right (1,n) a+=1, b-=1
left<right (2,n-1)

a=2, b=n
left>right (2,n) a+=1, b-=1
left>right (3,n-1) 
*/

int main(void){
    char word[] = "settled"; //"adjourned"
    int check = is_cyclone_word(word);
    if (check == 1){
        printf("True\n");
    }
    else 
        printf("False\n");

    // printf("%d\n", word[left]);    
    return 0;
}
