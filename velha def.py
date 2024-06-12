print('Jogo da Velha')
c1, c2, c3, c4, c5, c6, c7, c8, c9 = 1, 2, 3, 4, 5, 6, 7, 8, 9

print(f'  {c1} | {c2} | {c3} \n'f' ---+---+---\n'f'  {c4} | {c5} | {c6} \n'f' ---+---+---\n'f'  {c7} | {c8} | {c9} ')

while True:
    jogador1 = input('\nVocê quer ser X ou O? ').upper()
    if jogador1 != 'X' and jogador1 != 'O':
        print('Opção inválida!\n')
        continue
    break
    
if jogador1 == 'X':
    jogador2 = 'O'
elif jogador1 == 'O':
    jogador2 = 'X'

verificador = False
for n in range(10):
    if n == 9:
        print('\nDeu Velha!')
        break
    elif n % 2 == 0:
        jogador, nj = jogador1, 1
    elif n % 2 != 0:
        jogador, nj = jogador2, 2
    
    while True:
        try:
            jogada = int(input(f'\nJogador {nj} - Digite o número da casa que deseja jogar: '))
        except:
            print('Jogada inválida')
            continue

        if jogada == 1 and type(c1) == int:
            c1 = jogador
        elif jogada == 2 and type(c2) == int:
            c2 = jogador
        elif jogada == 3 and type(c3) == int:
            c3 = jogador
        elif jogada == 4 and type(c4) == int:
            c4 = jogador
        elif jogada == 5 and type(c5) == int:
            c5 = jogador
        elif jogada == 6 and type(c6) == int:
            c6 = jogador
        elif jogada == 7 and type(c7) == int:
            c7 = jogador
        elif jogada == 8 and type(c8) == int:
            c8 = jogador
        elif jogada == 9 and type(c9) == int:
            c9 = jogador
        else:
            print('Jogada inválida\n')
            continue
        break

    print(f'\n  {c1} | {c2} | {c3} \n'f' ---+---+---\n'f'  {c4} | {c5} | {c6} \n'f' ---+---+---\n'f'  {c7} | {c8} | {c9} ')

    if (c1 == c2 == c3) or (c4 == c5 == c6) or (c7 == c8 == c9) or (c1 == c4 == c7) or (c2 == c5 == c8) or (c3 == c6 == c9) or (c1 == c5 == c9) or (c3 == c5 == c7):
            print(f'\nJogador {nj} Venceu!')
            verificador = True
    
    if verificador == True:
        break
    
        