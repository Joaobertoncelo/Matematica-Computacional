#Cálculo e^x e ln(x) baseados em uma tabela de consulta com entradas nice-numbers, numeros que, envolvidos numa multiplicação, resultam em um bit-shift e uma adição
#y = ln(x); x>0 tem como forma invariante
#y = ln(x/x) = ln(1) = 0 para 1/x = 1/(kx) em y = ln(x/x)
#y = ln(x/kx) = ln((x/x)*(1/k))
#y = ln(x/x) + ln(1/k) = 0 + ln(1/k) = -ln(k)

from typing import List, Dict
import math
import struct

def ln_x(number: float) -> float:
    """
    Retorna o logaritmo natural (ln) de um número usando interpolação a partir de uma tabela predefinida.
    """
    # Obtendo a tabela de números Nice
    nice_table = niceNumbers()

    # Definindo uma variável para percorrer a tabela Nice
    index = 0

    # Obtendo a linha atual da tabela Nice
    current_row = nice_table[index]

    # Enquanto o número for maior que o limite inferior da próxima linha da tabela Nice,
    # avança para a próxima linha
    while index < len(nice_table) - 1 and nice_table[index + 1]['n'] > number:
        index += 1
        current_row = nice_table[index]

    # Dividindo o número pela constante da linha atual da tabela Nice
    x = number / current_row['n']

    # Obtendo o ln da linha atual da tabela Nice
    y = current_row['ln']

    # Interpolando o ln do número a partir das próximas linhas da tabela Nice
    while index < len(nice_table) - 1:
        # Multiplicando x pela potência da constante da linha atual da tabela Nice
        power = current_row['exp']
        mult = x ** power

        # Enquanto o número for maior ou igual ao limite inferior da próxima linha da tabela Nice,
        # avança para a próxima linha
        while index < len(nice_table) - 1 and mult >= 1:
            index += 1
            current_row = nice_table[index]
            power = current_row['exp']
            mult = x ** power

        # Se ainda há linhas para interpolar o ln, atualiza o valor de x e y
        if index < len(nice_table) - 1:
            x = mult
            y -= current_row['ln']

    # Retorna o ln do número subtraído do erro de arredondamento
    return y - abs(1 - x)


#uma tabela de consulta com entradas nice-numbers
def niceNumbers() -> list[dict]:
    return [
    {'n': 3.0, 'ln': 1.0986122886681098, 'exp': 1},
    {'n': 5.0, 'ln': 1.6094379124341003, 'exp': 2},
    {'n': 9.0, 'ln': 2.1972245773362196, 'exp': 3},
    {'n': 17.0, 'ln': 2.833213344056216, 'exp': 4},
    {'n': 33.0, 'ln': 3.4965075614664802, 'exp': 5},
    {'n': 65.0, 'ln': 4.174387269895637, 'exp': 6},
    {'n': 129.0, 'ln': 4.8573324964312685, 'exp': 7},
    {'n': 257.0, 'ln': 5.543741150080023, 'exp': 8},
    {'n': 513.0, 'ln': 6.233406007803151, 'exp': 9},
    {'n': 1025.0, 'ln': 6.926205448990583, 'exp': 10},
    {'n': 2049.0, 'ln': 7.621945174070975, 'exp': 11},
    {'n': 4097.0, 'ln': 8.320363047772128, 'exp': 12},
    {'n': 8193.0, 'ln': 9.021279351957755, 'exp': 13},
    {'n': 16385.0, 'ln': 9.72452689305461, 'exp': 14},
    {'n': 32769.0, 'ln': 10.429948609920046, 'exp': 15},
    {'n': 65537.0, 'ln': 11.137399121336791, 'exp': 16},
    {'n': 131073.0, 'ln': 11.846740579210332, 'exp': 17},
    {'n': 262145.0, 'ln': 12.557841045021825, 'exp': 18},
    {'n': 524289.0, 'ln': 13.270573115025252, 'exp': 19},
    {'n': 1048577.0, 'ln': 13.984814572476575, 'exp': 20},
    {'n': 2097153.0, 'ln': 14.700448005475653, 'exp': 21},
    {'n': 4194305.0, 'ln': 15.417360959112062, 'exp': 22},
    {'n': 8388609.0, 'ln': 16.135444016864466, 'exp': 23},
    {'n': 16777217.0, 'ln': 16.85459291287815, 'exp': 24},
    {'n': 33554433.0, 'ln': 17.57470786432736, 'exp': 25},
    {'n': 67108865.0, 'ln': 18.295691437997673, 'exp': 26},
]

def libc_ln(x: float) -> float:
    return math.log(x)

def calc(a, e):
    val = struct.pack('f', a)
    k = struct.unpack('i', val)[0]

    expoente = (k >> 23) & 0xFF

    aux = a

    expoente += e

    k = (k & ~(0xFF << 23)) | (expoente << 23)

    val = struct.pack('i', k)
    f = struct.unpack('f', val)[0]

    f += aux

    return f
    
def main():
    numbers = [1, 3, 5, 7, 10, 20, 50, 100, 200, 500, 1000, 5000, 10000]
    for number in numbers:
        # Obtém o resultado da nossa função
        result = ln_x(number)
        
        # Compara com o resultado da biblioteca matemática do Python
        expected = math.log(number)
        error = abs(expected - result)
        
        # Exibe o resultado
        print(f"ln({number}) = {result:.6f} (erro: {error:.6f})")


if __name__ == "__main__":
    main()
