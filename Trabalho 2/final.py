import numpy as np
import matplotlib.pyplot as plt

# Definindo a função seno
def f(x):
    return np.sin(x)

# Aproximação de Padé com 11 elementos
p = np.poly1d([1575/6912, 0, -245/1152, 0, 49/512, 0, -1/16, 0, 1/720, 0, -1/40320])

# Aproximação de Taylor com 11 termos
def taylor(x):
    return x - x**3/6 + x**5/120 - x**7/5040 + x**9/362880 - x**11/39916800

# Intervalo de x para plotar o gráfico
x = np.linspace(-(np.pi), (np.pi), 10000)

# Cálculo dos valores de y
y = f(x) * 1e12
y_pade = p(x) * 1e12
y_taylor = taylor(x) * 1e12

# Plotando o gráfico
plt.plot(x, y, label="Seno")
plt.plot(x, y_pade, label="Aproximação de Padé")
plt.plot(x, y_taylor, label="Aproximação de Taylor")
plt.legend()
plt.ylabel("-1e12")
plt.show()
