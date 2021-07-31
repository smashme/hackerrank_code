#include <stdio.h>
#include <string.h>
#include <math.h>
#include <stdlib.h>

int main() 
{

    int k,n,p,q,g,y,i,a;
    scanf("%d", &k);
  	// Complete the code to print the pattern.
    int num=2;
 
    //inserted code
     for (int row_1=1; row_1<=(k*2-1); row_1++){
        printf("%d ",k);
    }
    printf("\n");
    
    for (int i=1; i<k; i++){  //rows count
        for (int j=k; j>=(k-i); j--){  //numbers count
            printf("%d ",j);
   
            num=j;
        }
        for (p=(num*2-1); p>=2; p--){ //prints next number in sequence num*2-1 times
            printf("%d ",num);
        }
        for (y=num+1;y<=k; y++){  //counting numbers to the end of row
            printf("%d ",y);
        }
        
        
        printf("\n");
    }
    
  //end inserted code

 //works 222 to all 7's increasing
    num++;
    for (int i=1; i<k; i++){  //rows count
        for (int j=k; j>=num; j--){  //numbers count down
            printf("%d ",j);
          //  num++;
        }   
//    printf("\n");
//    printf("num=%d",num);
    //for (p=num; p<=(num*2-1); p++){  //number in middle
    for (p=(num*2-1); p>=2; p--){  //number in middle
            printf("%d ",num);
         //   num++;
        
        }
     //   printf("\n");
     
     for (q=num+1; q<=k; q++){   //number count up
          printf("%d ",q);
     }
     num++;
     printf("\n");

    }
   // printf("Hello world");
     
    return 0;
}

