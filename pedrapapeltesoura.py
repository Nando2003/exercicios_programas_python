# import random
from random import choice

player_win = 0
machine_win = 0


def opcao_player():
    esc_jogador = input("Escolha pedra, papel ou tesoura: ")
    esc_jogador = esc_jogador.lower()
    if esc_jogador == 'pedra':
        return esc_jogador
    elif esc_jogador == 'papel':
        return esc_jogador
    elif esc_jogador == 'tesoura':
        return esc_jogador
    else:
        print("Opção Invalida. Tente novamente.")
        opcao_player()


def opcao_machine():
    esc_maquina = choice(['pedra', 'papel', 'tesoura'])
    return esc_maquina


while True:

    print("-"*30)
    esc_jogador = opcao_player()
    esc_maquina = opcao_machine()
    print("-"*30)

    if (esc_jogador == 'pedra') and (esc_maquina == 'papel') \
        or (esc_jogador == 'papel') and (esc_maquina == 'tesoura') \
            or (esc_jogador == 'tesoura') and (esc_maquina == 'pedra'):
        print(
            f"VITORIA DA MAQUINA! A Maquina escolheu {esc_maquina} \
                e o Jogador escolheu {esc_jogador}")
        machine_win = machine_win + 1
    elif esc_maquina == esc_jogador:
        print(
            f"EMPATE! A Maquina escolheu {esc_maquina} e o Jogador \
                escolheu {esc_jogador}")
    else:
        print(
            f"VITORIA DO JOGADOR! A Maquina escolheu {esc_maquina} \
                e o Jogador escolheu {esc_jogador}")
        player_win = player_win + 1

    print("-"*30)
    print("Numero de vítorias do jogador: ", player_win)
    print("Numero de vítorias da maquina: ", machine_win)
    print("-"*30)

    esc_jogador = input("Voce deseja jogar novamente? ")
    if esc_jogador in ('SIM', 'Sim', 'sim', 'S', 's'):
        pass
    elif esc_jogador in ('NAO', 'Nao', 'nao', 'N', 'n'):
        break
    else:
        break
