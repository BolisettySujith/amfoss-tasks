#include <stdio.h>
#include <cs50.h>
#include <math.h>
int main(int cent)
int main(void)
{
    // input process
    float input;
    do
    {
        printf("Change owed:");
        input = get_float("");
    }
    while(input < 0);

    // out put process
    printf("%d\n", change( (int)round(input*100) )  );
}
// return - minimum number of changes
int change (int cent)
{
    // 25 // (whatever's remaing) 10 //(wer) 5 // (wer) 1
    return cent/25 +(cent%25)/10 + ((cent%25)%10)/5 + ((cent%25)%10)%5 ;
}