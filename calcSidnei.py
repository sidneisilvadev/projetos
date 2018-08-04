class Calculadora(object):

    def __init__(self, n1, n2):
        self.n1 = n1
        self.n2 = n2
    
    def __add__(self, n1, n2):
        total = (n1 + n2)
        return total

    def __sub__(self, n1, n2):
        total = n1 - n2
        return total

    def __mult__(self, n1, n2):
        total = n1 * n2
        return total

    def __truediv__(self, n1, n2):
        total = n1 / n2
        return total

while True:
    n1 = float(input('Primeiro valor: '))
    operador = input('Operador [+ - * /]: ')
    n2 = float(input('Segundo valor: '))


    calc = Calculadora(n1, n2)

    if operador == '+':
        print('%.2f %s %.2f = %.2f' %(n1, operador, n2, calc.__add__(n1, n2)))
    elif operador == '-':
        print('%.2f %s %.2f = %.2f' %(n1, operador, n2, calc.__sub__(n1, n2)))
    elif operador == '*':
        print('%.2f %s %.2f = %.2f' %(n1, operador, n2, calc.__mult__(n1, n2)))
    else:
        print('%.2f %s %.2f = %.2f' %(n1, operador, n2, calc.__truediv__(n1, n2)))

    sair = input('\n...para sair digite "q" :')
    if sair == 'q':
        break

    print('*' * 30, '\n')
