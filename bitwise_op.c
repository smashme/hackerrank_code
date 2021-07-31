#include <stdio.h>
#include <string.h>
#include <math.h>
#include <stdlib.h>
//Complete the following function.


void calculate_the_maximum(int n, int k) {
  //Write your code here.
  unsigned int temp1=0, temp2=0, temp3=0;
  unsigned int max_a_d=0,max_o_r=0, max_x_o=0;
  unsigned int a,b,ad,o_r,x_o;
  for (a=1;a<=k;a++){
      for (b=a+1;b<=n;b++){
          ad=(a&b);
          o_r=(a|b);
          x_o=(a^b);
          temp1=ad;
          temp2=o_r;
          temp3=x_o;
          /*printf(" or= %d",temp2);*/
          if (temp1>max_a_d && temp1<k){
              max_a_d=temp1;
          }
          if (temp2>=max_o_r && temp2<k){
              max_o_r=temp2;
              
          }
          if ( temp3>max_x_o && temp3<k){
              max_x_o=temp3;
          }
       }
  }
  printf("%d\n", max_a_d);
  printf("%d\n", max_o_r);
  printf("%d\n", max_x_o);

}

int main() {
    int n, k;
  
    scanf("%d %d", &n, &k);
    calculate_the_maximum(n, k);
 
    return 0;
}

