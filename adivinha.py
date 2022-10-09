print('''
-----JOGO DE ADIVINHAÇÃO-----
ESCOLHA QUALQUER NÚMERO INTEIRO ATÉ 100 PARA JOGAR!
-----BOA SORTE!-----
''')
numero_secreto = 42
total_de_tentativas = 3
rodada = 1

while(rodada <= total_de_tentativas > 0):

    print('Tentativa {} de {}'.format(rodada, total_de_tentativas))
    chute_str = input('Digite o seu número: ')
    print('Você digitou:', chute_str)
    chute = int(chute_str)

    acertou = chute == numero_secreto
    maior = chute > numero_secreto
    menor = chute < numero_secreto


    if acertou:
        print('Você acertou!')
    else:
        if(maior):
            print('Você errou! O seu número foi maior que o número secreto')
        if(menor):
            print('Você errou! O seu numéro foi menor que o número secreto')

    rodada += 1



print('Fim do jogo')
