import numpy as np
import matplotlib.pyplot as plt

# Definindo a função seno
def seno_exato(x):
    return np.sin(x)

# Aproximação de Padé de ordem (7,4) elementos
# Define os coeficientes dos polinômios p(x) e q(x)
p_coef = [-121/2268000, 0, 601/118800, 0, -241/1650, 0, 1, 0]
q_coef = [19/118800, 0, 17/825, 0, 1]

# Define as funções para avaliar os polinômios p(x) e q(x) em um dado valor de x
def eval_poly(p_coef, x):
    result = 0
    for i in range(len(p_coef)):
        result += p_coef[i] * x ** i
    return result

def eval_p(p_coef, x):
    return eval_poly(p_coef, x)

def eval_q(q_coef, x):
    return eval_poly(q_coef, x)

# Define a função pade(x)
def pade(x):
    return eval_p(p_coef, x) / eval_q(q_coef, x)


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
x = np.linspace(-(np.pi/4), (np.pi/4), 10000)

def erro_pade(x):
    return abs(seno_exato(x) - pade(x))

def erro_taylor(x):
    return abs(seno_exato(x) - taylor(x))

# Cálculo dos valores de y
#y = f(x)
#y_pade = pade(x)
#y_taylor = taylor(x)
y_erro_p = erro_pade(x)
y_erro_t = erro_taylor(x)

# Plotando o gráfico
#plt.plot(x, y, label="Seno")
#plt.plot(x, y_pade, label="Aproximação de Padé")
#plt.plot(x, y_taylor, label="Aproximação de Taylor")
plt.plot(x, y_erro_p, label="Erro de Padé")
plt.plot(x, y_erro_t, label="Erro de Taylor")
plt.legend()
plt.show()

#Imprime os resultados
print(f"O seno de {x} é {seno_exato:.11f}")
print(f"A aproximação taylor com {n} termos é {taylor:.11f}")
print(f"A aproximação pade com {n} termos é {pade:.11f}")
print(f"A diferença taylor é {abs(seno_exato - taylor):.11f}")
print(f"A diferença pade é {abs(seno_exato - pade):.11f}")
