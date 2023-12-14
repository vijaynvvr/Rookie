#include <math.h>
#include <stdio.h>

int main()
{
    double a,b,c,D,r1,r2,R,I;
    printf("Enter coefficients a,b and c:");
    scanf("%lf %lf %lf", &a, &b, &c);

    D = b*b-4*a*c;

    if (D>0) {
        r1 = (-b + sqrt(D))/(2*a);
        r2 = (-b - sqrt(D))/(2*a);
        printf("root1 = %lf and root2 = %lf", r1, r2);
    }

    else if (D==0) {
        r1 = r2 = -b/(2*a);
        printf("root1 = root2 = %lf", r1);
    }

    else {
        R = -b/(2*a);
        I = sqrt(-D)/(2*a);
        printf("root1 = %lf+(i)%lf and root2 = %lf-(i)%lf", R, I, R, I);
    }
    return 0;
}
