import random
print('\n- - - Gerador de bilhetes da Mega Sena: - - - \n')
for num in range(1,11):
    jogo = random.sample(range(1,61),6)
    print('Jogo:', num, jogo)
print('\nBOA SORTE NA SUA Aposta!!!\n')
input('\n APERTE ENTER PARA SAIR\n')