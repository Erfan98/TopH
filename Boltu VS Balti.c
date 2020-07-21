#include<stdio.h>
int main()
{
    long long int n,m,i,s=0;
    while(scanf("%lld %lld",&n,&m)!=EOF){
    
    /*scanf("%lld %lld",&n,&m);*/
    if(n>m){
        n=n+m;
        m=n-m;
        n=n-m;
    }
    for(i=n;i<=m;i++){
        s=s+i;

    }
    printf("Sum of %lld to %lld is -> %lld;\n",n,m,s);
    s=0;
    }
}   