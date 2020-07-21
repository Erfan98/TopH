#include<stdio.h>
#include<math.h>
int main()
{
    long long int n,m,r1,r2,i;
    int t;
    scanf("%d",&t);
    for(i=1;i<=t;i++){
    scanf("%lld %lld",&n,&m);
    r1=pow(n,m);
    r2=pow(m,n);
    if (r1>r2){
        printf("%lld \n",n);
    }
    else{
        printf("%lld \n",m);
    }
    }
}