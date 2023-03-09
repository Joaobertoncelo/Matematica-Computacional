import math
import numpy as np
import matplotlib.pyplot as plt

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
    # Alocando os valores do cálculo a constantes para diminuir o trabalho do computador
    a = -1/6
    b = 1/120
    c = -1/5040
    d = 1/362880
    e = -1/39916800
    y = x*x
    # Método Pade
    p = x * (1 + y * (a + y * (b + y * (c + y * ( d + y * e)))))
    return p

def plotagem(corretos, aproximacoes_taylor, aproximacoes_pade):
    plt.plot(aproximacoes_pade, 'k--', label="pade")
    plt.plot(aproximacoes_taylor, 'go', label="taylor")
    plt.plot(corretos)
    plt.show()

def main():
    n = 11
    valores_corretos = []
    aproximacoes_taylor = []
    aproximacoes_pade = []

    for x in np.arange(0, 20.1, 0.1):
        # Calcula o seno exato usando a função sin() do módulo numpy
        valores_corretos.append(np.sin(x))
        #print(valores_corretos)

        # Calcula uma aproximação do seno usando a função aprox_seno() definida acima
        aproximacoes_taylor.append(taylor_seno(x, n))
        print(aproximacoes_taylor)
        aproximacoes_pade.append(pade_seno(x))
        #print(aproximacoes_pade)
        #print(f'{np.sin(x)} {taylor_seno(x, n)} {pade_seno(x)}')

    plotagem(valores_corretos, aproximacoes_taylor, aproximacoes_pade)

    # Imprime os resultados
    #print(f"O seno de {x} é {seno_exato:.11f}")
    #print(f"A aproximação taylor com {n} termos é {seno_taylor_aprox:.11f}")
    #print(f"A aproximação pade com {n} termos é {seno_pade_aprox:.11f}")
    #print(f"A diferença taylor é {abs(seno_exato - seno_taylor_aprox):.11f}")
    #print(f"A diferença pade é {abs(seno_exato - seno_pade_aprox):.11f}")

if __name__ == '__main__':
    main()
