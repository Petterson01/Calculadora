from funções import * #"importando as funções do arquivo funcções"
while True: #"criando um loop infinito"
    print('Qual operação deseja realizar: ') #menu
    print("""
        1 - adição
        2 - subtração 
        3 - multiplicação 
        4 - divisão  
        5 - sair
    """)
    operação = int(input("")) #entrada da resposta para o match case

    match operação: #estrutura inicial match case   /  match variavel     case 1 ... case 2 ... case 3 ...

        case 1: 
            num1 = int(input('numero 1: ')) 
            num2 = int(input('numero 2: ')) 
            print(f'Resultado: {somar(num1,num2)}') 
        case 2:
            num1 = int(input('numero 1: ')) 
            num2 = int(input('numero 2: ')) 
            print(f'Resultado: {subtração(num1,num2)}') 
        case 3:
            num1 = int(input('numero 1: '))
            num2 = int(input('numero 2: ')) 
            print(f'Resultado: {multiplicacao(num1,num2)}') 
        case 4:
            num1 = int(input('numero 1: '))
            num2 = int(input('numero 2: ')) 
            print(f'Resultado: {divisao(num1,num2)}') 
        case _:
            break # encerramento do programa
