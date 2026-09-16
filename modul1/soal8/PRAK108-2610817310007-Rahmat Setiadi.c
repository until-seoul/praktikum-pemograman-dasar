
#include <stdio.h>
#include <math.h>

int main()
{
    float jarak_tempuh = 14;
    int putaran = 5;
    float keliling_taman = jarak_tempuh / putaran;
    float jari_jari_taman = keliling_taman / (2 * M_PI);

    printf("Diketahui :\n");
    printf("Pak Dengklek mengelilingi taman sebanyak %d putaran\n", putaran);
    printf("Jarak tempuh Pak Dengklek adalah %.2f kilometer\n", jarak_tempuh);
    printf("Jawaban :\n");
    printf("Jari-jari taman yang dikelilingi Pak Dengklek adalah %.2f kilometer\n", jari_jari_taman);

    return 0;
}
