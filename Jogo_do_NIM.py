# Jogo do NIM

def computador_escolhe_jogada(n, m):
    retirar = 1
    while True:
        if (n - retirar) % (m + 1) == 0:
            break
        else:
            retirar += 1
            if retirar > m:
                retirar = m
                break
    return retirar


def usuario_escolhe_jogada(n,m):
    while True:
        retirar = int(input('Quantas peças você quer remover? '))
        if retirar > m or retirar > n or retirar <= 0:
            print('Oops! Jogada inválida! Tente de novo.')
            continue
        else:
            break
    return retirar


def partida():
    n = int(input('Quantas peças? '))
    m = int(input('Limite de peças por jogada? '))
    vencedor = 0

    if n % (m + 1) != 0:
        print('Computador começa!')
        while n > 0:
            print(f'O computador retirou {computador_escolhe_jogada(n, m)} peças')
            n = n - (computador_escolhe_jogada(n, m))
            if n <= 0:
                print('O computador ganhou!')
                vencedor = 1
                break
            else:
                print(f'Há {n} peças restantes')
            retirar = usuario_escolhe_jogada(n, m)
            print(f'Você retirou {retirar} peças')
            n = n - retirar
            if n <= 0:
                print('Você ganhou!')
                vencedor = 2
                break
            else:
                print(f'Há {n} peças restantes')
        return vencedor
    else:
        print('Você começa!')
        while n > 0:
            retirar = usuario_escolhe_jogada(n, m)
            print(f'Você retirou {retirar} peças')
            n = n - retirar
            if n <= 0:
                print('Você ganhou!')
                vencedor = 2
                break
            else:
                print(f'Há {n} peças restantes')

            print(f'O computador retirou {computador_escolhe_jogada(n, m)} peças')
            n = n - (computador_escolhe_jogada(n, m))
            if n <= 0:
                print('O computador ganhou!')
                vencedor = 1
                break
            else:
                print(f'Há {n} peças restantes')
    return vencedor


def campeonato():
    rodada = 1
    vitoria_jogador = 0
    vitoria_computador = 0
    while rodada <= 3:
        print(f'***** Rodada {rodada} *****')
        resultado = partida()
        if resultado == 1:
            vitoria_computador += 1
        else:
            vitoria_jogador += 1
        rodada += 1
    print(f'Placar: Você {vitoria_jogador} X {vitoria_computador} Computador')


ínicio_jogo = input('Bem-vindo ao jogo do NIM! Escolha:\n'
          '\n'
          '1 - para jogar uma partida isolada\n'
          '2 - para jogar um campeonato ')
if ínicio_jogo == '1':
    print('Você escolheu uma partida isolada!')
    partida()

elif ínicio_jogo == '2':
    print('Você escolheu campeonato!')
    campeonato()
