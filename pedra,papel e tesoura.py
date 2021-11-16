from random import randint;
print('''
    [ 1 ] - > pedra
    [ 2 ] - > papel
    [ 3 ] - > tesoura
    ''')
maquina = ['ignore', 'pedra', 'papel', 'tesoura']
jogador = randint(1, 3); # 1 pedra, 2 papel, 3 tesoura;
ppt = int(input('opção: '))
if ppt == 1 or ppt == 2 or ppt == 3:
    if ppt == jogador:
        print('empate! nós dois escolhemos',maquina[ppt])
    elif ppt == 1 and jogador == 3: #escolhi pedra e o jogador tesoura(ganhei)
        print('você ganhou, eu escolhi',maquina[jogador],'e você',maquina[ppt])
    elif ppt == 3 and jogador == 2: #escolhi tesoura e o jogador papel(ganhei)
        print('você ganhou, eu escolhi',maquina[jogador],'e você',maquina[ppt])
    elif ppt == 2 and jogador == 1: #escolhi papel e o jogador pedra(ganhei)
        print('você ganhou, eu escolhi',maquina[jogador],'e você',maquina[ppt])
    else: #se eu não ganhei nem empatei, obviamente eu perdi.
        print('você perdeu, eu escolhi',maquina[jogador],'e você',maquina[ppt])
else:
    print('escolha apenas opções entre 1, 2 e 3!')