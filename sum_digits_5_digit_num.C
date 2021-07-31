#include <stdio.h>
#include <string.h>
#include <math.h>
#include <stdlib.h>

int main() {
	
    int n=0,j=0;
    int num=0;
    int sum=0;
    scanf("%d", &n);
    //Complete the code to calculate the sum of the five digits on n.
    while (n>=0){
        num=n/10;
       /* printf("%d\n",n);*/
        sum=sum+(n%10);
        n=num;
        if (num==0){
            break;
        }
    }
    printf("%d",sum);
    
    return 0;
}


