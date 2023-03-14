import math
import numpy as np
import matplotlib.pyplot as plt

def taylor_seno(x):    
    #para X ao quadrado
    y = x*x
    p = x(1+y*(-(1/6)+y*((1/120) + y*(-(1/5040)+ y*((1/362880)+ y*(-(1/39916800)))))))
    return p

def pade_seno(x):
    # Método Pade
    p = ((-1331)*(x**7) + 126210*(x**5) + (-3643920)*(x**3) + 24948000*x)/(3990*(x**4) + 514080*(x**2) + 24948000) 
    return p

def plotagem(corretos, aproximacoes_taylor, aproximacoes_pade):
    plt.plot(aproximacoes_pade, 'k--', label="pade")
    plt.plot(aproximacoes_taylor, 'go', label="taylor")
    plt.plot(corretos)
    plt.show()

def main():
    valores_corretos = []
    aproximacoes_taylor = []
    aproximacoes_pade = []

    for x in np.arange(0, 20.1, 0.1):
        # Calcula o seno exato usando a função sin() do módulo numpy
        valores_corretos.append(np.sin(x))
        #print(valores_corretos)

        # Calcula uma aproximação do seno usando a função aprox_seno() definida acima
        aproximacoes_taylor.append(taylor_seno(x))
        print(aproximacoes_taylor)
        aproximacoes_pade.append(pade_seno(x))
        print(aproximacoes_pade)
        #print(f'{np.sin(x)} {taylor_seno(x, n)} {pade_seno(x)}')

    plotagem(valores_corretos, aproximacoes_taylor, aproximacoes_pade)

    # Imprime os resultados
    #print(f"O seno de {x} é {seno_exato:.11f}")
    #print(f"A aproximação taylor com {n} termos é {seno_taylor_aprox:.11f}")
    #print(f"A aproximação pade com {n} termos é {seno_pade_aprox:.11f}")
    #print(f"A diferença taylor é {abs(seno_exato - seno_taylor_aprox):.11f}")
    #print(f"A diferença pade é {abs(seno_exato - seno_pade_aprox):.11f}")
main()
