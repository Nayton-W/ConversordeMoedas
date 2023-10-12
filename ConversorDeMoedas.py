while (True):
    print('==== Coversor de moedas R$ / U$ ====')
    print('*'*7)
    op = float(input(
        'Escolha:\n   (1) pra converter dolar a real\n   (2) pra converter real a dolar \n'))
    print('*'*2)
    print('='*48)

    match op:
        case 1:
            dol = float(input('Quanto dinheiro você tem na carteira ? '))
            print('='*48)
            r = dol * 4.94
            print('Com U$ {} você pode comprar R$ {:.6}'.format(dol, r))

        case 2:
            real = float(input('Quanto dinheiro você tem na carteira ? '))
            print('='*48)
            dolar = real / 4.94
            print('Com R$ {} você pode comprar U$ {:.6}'.format(real, dolar))

        case _:

            print("ERROR")

    print('='*48)

    decisao = input("Deseja continuar (s) / (n) ?:\n")
    if (decisao != 's' and decisao != 'sim'):
        break
    print('='*48)
