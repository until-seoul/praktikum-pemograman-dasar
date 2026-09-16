#include <stdio.h>
#include <math.h>

int main() {
    int alas = 5, tinggi = 12, luas = 30, keliling = 30;

    int miring = sqrt(pow(alas, 2) + pow(tinggi, 2));
    printf("Diketahui :\n");
    printf("Alas = %d\n", alas);
    printf("Tinggi = %d\n", tinggi);
    printf("\n");

    printf("Jawab : \n");
    printf("Sisi A = %dcm\n", tinggi);
    printf("Sisi B = %dcm\n", miring);
    printf("Sisi C = %dcm\n", alas);
    printf("Keliling = %dcm\n", keliling);
    printf("Luas = %dcm\n", luas);
}