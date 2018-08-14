
n1 = float(input('Digite o primeiro número: '))
n2 = float(input('Digite o segundo número: '))
oper = ''


while oper != 'q':
    oper = str(input("Escolha uma operação: + - * /\nDigite 'q' para sair:"))

    if oper == '+':   # Soma.
        print('A soma entre {:.2f} e {:.2f} resultou em {:.2f}'.format(n1, n2, (n1+n2)))
        break

    elif oper == '-':   # Subtração.
        print('A subtração entre {:.2f} e {:.2f} resultou em {:.2f}'.format(n1, n2, (n1-n2)))
        break

    elif oper == '*':   # Multiplicação.
        print('A multiplicação entre {:.2f} e {:.2f} resultou em {:.2f}'.format(n1, n2, (n1*n2)))
        break

    elif oper == '/':   # Divisão.
        print('O resultado da divisão entre {:.2f} e {:.2f} resultou em {:.2f}'.format(n1, n2, (n1/n2)))
        break

    elif oper.lower() == 'q':   # Sair.
        print('Ok, cancelado')
        break

    else:   # A opção digitada não foi definida.
        print('Operação inválida')


print('Fim do processo!')
