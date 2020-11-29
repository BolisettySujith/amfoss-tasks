# include <stdio.h>
int main (void)
{
    int n,i,j;
    printf("how many rows u want :");
    scanf("%d\n",&n);
    for(i=1;i<=n;i++)
    {
        for(j=1;j<= 2*n-1;j++)
        {
            if(j>=n-(i-1) && j <=n+(i-1))
            {
                printf("D");
            }
            else
                printf("*");
                
        }
        printf("\n");
        
    }
    for(i=n-1;i<=n;--i)
    {
        for(j=1;j<= 2*n-1;j++)
        {
            if(j>=n-(i-1) && j<=n+(i-1))
            {
                printf("D");
            }
            else
                printf("*");
                
        }
        if(i <= 1)
        {
            break;
        }
        printf("\n");
    }    
          
    return 0 ;
    
}