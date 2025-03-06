""" Calculadora com while """

while True:
    # Coletando os números do usuário
    numero_1 = input('Digite um número: ')
    numero_2 = input('Digite outro número: ')
    operador = input('Digite o operador (+-/*): ')

    numeros_validos = False
    num_1_float = 0
    num_2_float = 0

    try:
        num_1_float = float(numero_1)  # transformamos os números inputados em float
        num_2_float = float(numero_2)
        numeros_validos = True
    except ValueError:
        numeros_validos = False

    # Validando se os números do usuário são válidos, impedindo que letras ou símbolos sejam digitados ao invés de números reais
    if not numeros_validos:
        print('Um ou ambos os números digitados são inválidos.')
        continue

    operadores_permitidos = '+-/*'

    # Validação dos operadores permitidos na operação, nada será aceito além dos sinais de operação válidos.
    if operador not in operadores_permitidos:
        print('Operador inválido.')
        continue

    # Impedindo que o usuário digite mais de um operador
    if len(operador) > 1:
        print('Digite apenas um operador.')
        continue

    # Printando o resultado das operações
    print('O resultado da operação é: ')

    if operador == '+':
        print(f'O {num_1_float} + {num_2_float} = {num_1_float + num_2_float}')
    
    elif operador == '-':
        print(f'O {num_1_float} - {num_2_float} = {num_1_float - num_2_float}')

    elif operador == '*':
        print(f'O {num_1_float} * {num_2_float} = {num_1_float * num_2_float}')

    elif operador == '/':
        print(f'O {num_1_float} / {num_2_float} = {num_1_float / num_2_float}')

    #                 !!!SE ESSE ELSE FOR TRUE, É SINAL DE QUE DEIXAMOS PASSAR ALGUM ERRO DE VALIDAÇÃO DENTRO DO CÓDIGO!!!
    else:
        print('Algum erro conseguiu passar nas validações. Revise seu código.')

    # Se o usuário quiser interromper o programa, basta digitar s, S, Sair, SAIR, sair, sim, Sim, SIM
    sair = input('Deseja sair da calculadora? [s]im: ').lower().startswith('s')

    if sair:
        break