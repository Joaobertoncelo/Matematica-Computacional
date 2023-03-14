import numpy as np
import matplotlib.pyplot as plt

# Definindo a função seno
def f(x):
    return np.sin(x)

# Aproximação de Padé de ordem (7,4) elementos
p = np.poly1d([-121/2268000, 0, 601/118800, 0, -241/1650, 0, 1, 0])
q = np.poly1d([19/118800, 0, 17/825, 0, 1])
def pade(x):
    return p(x)/q(x)

# Aproximação de Taylor com 6 termos
a = -1/6
b = 1/120
c = -1/5040
d = 1/362880
e = -1/39916800
def taylor(x):
    y = x * x
    return x * (1 + y * (a + y * (b + y * (c + y * (d + y * e)))))

# Intervalo de x para plotar o gráfico
x = np.linspace(-(np.pi), (np.pi), 10000)

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
