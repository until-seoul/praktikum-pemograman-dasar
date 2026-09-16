#include <stdio.h>
#include <math.h>

int main()
{
    int shoe_a_price = 400000;
    int shoe_b_price = 350000;
    float shoe_a_discount = 13.0 / 100.0;
    float shoe_b_discount = 21.0 / 100.0;

    int discounted_price_a = shoe_a_price - (shoe_a_price * shoe_a_discount);
    int discounted_price_b = shoe_b_price - (shoe_b_price * shoe_b_discount);
    printf("Harga sepatu A adalah %d\n", shoe_a_price);
    printf("Harga sepatu B adalah %d\n", shoe_b_price);
    printf("Sepatu A mendapat diskon 13%% sehingga harganya menjadi %d\n", discounted_price_a);
    printf("Sepatu B mendapat diskon 21%% sehingga harganya menjadi %d\n", discounted_price_b);
    return 0;
}
