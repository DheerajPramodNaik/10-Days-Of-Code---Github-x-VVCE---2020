#include <stdio.h>
#include <string.h>
#include <math.h>
#include <stdlib.h>

int front = 0;
int rear = -1;
int queue[100000];

int main() {   

    int n, t, key, i, j;
    scanf("%d", &n);
    i = 0;
    while(i<n)
    {
        scanf("%d", &t);
        switch(t)
        {
            case 1: scanf("%d", &key);
                    if(front > rear)
                    {
                        front = 0;
                        rear = 0;
                    }
                    queue[rear++] = key;
                    break;
            case 2: front++;
                    break;
            case 3: printf("%d\n", queue[front]);
                    break;    
        }
        i++;
    }
    return 0;
}