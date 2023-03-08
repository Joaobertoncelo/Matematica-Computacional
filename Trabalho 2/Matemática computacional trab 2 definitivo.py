import math
import numpy as np

def taylor_seno(x, n):
    """
    Calcula uma aproximação do seno de x usando os n primeiros termos da série de Taylor.
    """
    seno = 0
    sinal = 1

    for k in range(1, n + 1, 2):
        termo = sinal * x**k / math.factorial(k)
        seno += termo
        sinal *= -1

    return seno

def pade_seno(x):
    p = x - (1/math.factorial(3)) - (1/math.factorial(7))
    return p


def main():
    # Lê o valor de x e n a partir do usuário
    x = float(input("Digite o valor de x: "))
    n = 11

    # Calcula o seno exato usando a função sin() do módulo math
    seno_exato = math.sin(x)

    # Calcula uma aproximação do seno usando a função aprox_seno() definida acima
    seno_taylor_aprox = taylor_seno(x, n)
    seno_pade_aprox = pade_seno(x)

    # Imprime os resultados
    print(f"O seno de {x} é {seno_exato:.9f}")
    print(f"A aproximação taylor com {n} termos é {seno_taylor_aprox:.9f}")
    print(f"A aproximação pade com {n} termos é {seno_pade_aprox:.9f}")
    print(f"A diferença é {abs(seno_exato - seno_taylor_aprox):.9f}")

if __name__ == '__main__':
    main()
