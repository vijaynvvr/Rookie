#include <stdio.h>

int main ()
{
    int a=5,b=6,c=7,d;
    printf("Working of logical && :\n");
    d=(a>b)&&(b>c);
    printf("(%d>%d)&&(%d>%d)=%d\n", a, b, b, c, d );
    d=(a>b)&&(b<c);
    printf("(%d>%d)&&(%d<%d)=%d\n", a, b, b, c, d );
    d=(a<b)&&(b<c);
    printf("(%d<%d)&&(%d<%d)=%d\n", a, b, b, c, d );
    d=(a<b)&&(b>c);
    printf("(%d<%d)&&(%d>%d)=%d\n\n", a, b, b, c, d );
    
    printf("Working of logical || :\n");
    d=(a>b)||(b>c);
    printf("(%d>%d)||(%d>%d)=%d\n", a, b, b, c, d );
    d=(a>b)||(b<c);
    printf("(%d>%d)||(%d<%d)=%d\n", a, b, b, c, d );
    d=(a<b)||(b<c);
    printf("(%d<%d)||(%d<%d)=%d\n", a, b, b, c, d );
    d=(a<b)||(b>c);
    printf("(%d<%d)||(%d>%d)=%d\n\n", a, b, b, c, d );
    
    printf("Working of logical ! :\n");
    d=!(a>b);
    printf("!(%d>%d)=%d\n", a, b, d);
    d=!(a<b);
    printf("!(%d<%d)=%d\n", a, b, d);
    return 0;
}