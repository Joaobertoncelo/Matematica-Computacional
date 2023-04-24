#include <stdio.h>
#include <math.h>
#include <stdint.h>

float newton_raphson(float num, float x0){
    return 0.5 * (x0 + (num/x0));
}

float inv_newton_raphson(float num, float x0){
    return x0 * (1.5f - 0.5f * num * x0 * x0);
}

float inv_sqrt(float num){
    const float num2 = 0.5f * num;

    union{
        float x;
        uint32_t k;
    } u = {num};

    u.k = 0x5f3759df - (u.k >> 1);
    u.x = u.x * (1.5f - num2 * u.x * u.x);

    return u.x;
}

float aprox_sqrt(float num){
    union{
        float f;
        uint32_t k;
    } val = {num};

    val.k -= 1 << 23;
    val.k >>= 1;
    val.k += 1 << 29;

    return val.f;   
}

int main(){
    float num = 59.1f;
    
    printf(
        "1/sqrt: %f\n1/newton_raphson: %f\ninv_newthon_raphson: %f\ntarolli: %f\n",
         1/sqrt(num),
         1/newton_raphson(num ,aprox_sqrt(num)),
         inv_newton_raphson(num, aprox_sqrt(1/num)),
         inv_sqrt(num)
    );

    return 0;
}