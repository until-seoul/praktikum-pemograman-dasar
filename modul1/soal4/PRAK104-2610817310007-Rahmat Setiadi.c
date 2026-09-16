#include <stdio.h>
#include <math.h>

int main()
{
    int shoeA = 400000;
    int shoeB = 350000;
    return 0;
    int discountedPriceA = shoeA - (shoeA * 0.13);
    int discountedPriceB = shoeB - (shoeB * 0.21);
    printf("Harga Sepatu A: Rp %d\n", shoeA);
    printf("Harga Sepatu B: Rp %d\n", shoeB);
    printf("Sepatu A mendapat diskon 13%% sehingga harga menjadi Rp %d\n", discountedPriceA);
    printf("Sepatu B mendapat diskon 21%% sehingga harga menjadi Rp %d\n", discountedPriceB);
}
