# programa para login e snha
print('\nLogin e Senha')
try:
    n = 0
    for n in range(0,3):
        login = str(input('\nEntre com o seu login: '))
        senha = str(input('\nEntre com a sua senha (Digite -1 caso queira abortar a operação): '))
        if login == 'aluno' and senha == 'uninove':
            print('\nLogin efetuado com sucesso!!')
            break
        elif senha == '-1':
            print('\nOperação abortada!!')
            break
        else:
            print('\nLogin e/ou senha inválidos!!')
            n = n + 1
            if n == 3:
                print('\nQuantidade de tentativas excedidas! Operação abortada!')

    input('\nPressione ENTER para sair...')

except ValueError:
    print('digite um número')
