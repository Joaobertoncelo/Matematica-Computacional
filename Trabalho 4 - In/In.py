#Cálculo e^x e ln(x) baseados em uma tabela de consulta com entradas nice-numbers, numeros que, envolvidos numa multiplicação, resultam em um bit-shift e uma adição
#y = ln(x); x>0 tem como forma invariante
#y = ln(x/x) = ln(1) = 0 para 1/x = 1/(kx) em y = ln(x/x)
#y = ln(x/kx) = ln((x/x)*(1/k))
#y = ln(x/x) + ln(1/k) = 0 + ln(1/k) = -ln(k)

import math

def ln(x):
    if x == 1:
        return 0
    elif x < 1:
        k = 1/x
        return -math.log(k)
    else:
        return ln(1/x)

def e(x):
    return 2.71828182845904523536028747135266249775724709369995**x

#uma tabela de consulta com entradas nice-numbers
def niceNumbers():
    return [1.0, 1.125, 1.25, 1.375, 1.5, 1.625, 1.75, 1.875]

#Cálculo e^x e ln(x)
def calc(x):
    if x == 0:
        return 1
    elif x >= 0:
        return e(x)
    else:
        return ln(x)
    
def main():
    print("Bem-vindo ao programa de cálculo de e^x e ln(x)!")
    x = input("Por favor, informe um número: ")
    try:
        x = float(x)
        print(f"e^{x} = {calc(x)}")
        print(f"ln({x}) = {calc(-x)}")
    except ValueError:
        print("O valor informado é inválido. Por favor, informe um número.")

if __name__ == "__main__":
    main()
