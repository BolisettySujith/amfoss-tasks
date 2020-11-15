#include <stdio.h>
#include <cs50.h>

int main(void)
{
    int n;
    do
    {
        printf("Height: ");
        n = get_int("");
    }
    while(n < 0 || n > 23);

    //whilw the pattren
    for(int i = 0; i < n; i++)
    {
        for(int j = 0; j <=n; j++)
        {
            if (i + j < (n - 1)) // if i + j less than n-1 it will print spaces
                printf(" ");
            else
                printf("#"); // if i +j >= n-1 it will print #
        }

        // a single line is over now move on to next line
        printf("\n");
    }

}
