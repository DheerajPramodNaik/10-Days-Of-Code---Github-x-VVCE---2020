#include<stdio.h>
int main()
{
    int n, d, a[1000000], i, diff = 0;
    scanf("%d%d", &n, &d);

    for(i = 0; i < n; i++)
    {
        scanf("%d", &a[i]);
    }

    for(i = d; i < n; i++)
    {
        printf("%d ", a[i]);
    }

    diff = n - d;

    for(i = 0; i < (n - diff); i++)
    {
        printf("%d ", a[i]);
    }
}