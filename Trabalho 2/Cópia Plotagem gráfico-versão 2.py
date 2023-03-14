import numpy as np
import matplotlib.pyplot as plt

# Definindo a função seno
def f(x):
    return np.sin(x)

# Aproximação de Padé com (7,4) elementos
def pade(x):
    p = ((-1331)*(x**7) + 126210*(x**5) + (-3643920)*(x**3) + 24948000*x)/(3990*(x**4) + 514080*(x**2) + 24948000) 
    return p

# Aproximação de Taylor com 11 termos
def taylor(x):
    #para X ao quadrado
    y = x*x
    p = x*(1+y*((-1/6)+y*((1/120) + y*((-1/5040)+ y*((1/362880)+ y*((-1/39916800)))))))
    return p

# Intervalo de x para plotar o gráfico
x = np.linspace(-(np.pi)/4, (np.pi)/4, 100)

# Cálculo dos valores de y
y = f(x)
y_pade = pade(x)
y_taylor = taylor(x)

# Plotando o gráfico
plt.plot(x, y, label="Seno")
plt.plot(x, y_pade, label="Aproximação de Padé")
plt.plot(x, y_taylor, label="Aproximação de Taylor")
plt.legend()
plt.show()