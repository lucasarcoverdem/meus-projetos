# Sistema para Gerenciamento de Fazenda

import json
import unicodedata

from classes.bovines import Bovine
from classes.milkproduction import MilkProduction
from classes.employee import Employee


cattle = []
team = []

def normalize(text):
    text = text.strip().lower().replace(" ", "")
    text = unicodedata.normalize("NFKD", text).encode("ASCII", "ignore").decode("utf-8")
    return text


def register_bovine():
    print('\n- Registrar bovino')
    


def cattle_function():
    print('\n- Gado')
    menu = input(
        '\n1 - Registrar bovino'
        '\n2 - Remover bovino'
        '\n3 - Ver gado registrado'
        '\n4 - Voltar'
        '\n(1, 2...): '
    ).strip().lower()

    menu = normalize(menu)

    if menu == '1':
        register_bovine()
    elif menu == '2':
        pass
    elif menu == '3':
        pass
    elif menu == '4':
        main()
    else:
        print("\nOpção inválida. Tente novamente.")


def login():
    user = input('Digite seu nome de usuário: ').lower().capitalize()
    password = input('Digite sua senha: ')

    print('Entrando. . .')
    return user


def main():
    user = login()

    print('\n- - - F A Z E N D A B A N A N E I R A - - -')
    print(f'\nSeja bem-vindo, {user}!')

    while True:
        menu = input(
            '\n1 - Gerenciar gado'
            '\n2 - Gerenciar produção'
            '\n3 - Gerenciar equipe'
            '\n4 - Sair'
            '\n(1, 2...): '
        ).strip().lower().replace(" ", "")

        menu = normalize(menu)

        if menu in ['1', 'gerenciargado']:
            cattle_function()
        elif menu in ['2', 'gerenciarproducao']:
            pass
        elif menu in ['3', 'gerenciarequipe']:
            pass
        elif menu == '4':
            print('\nEncerrando. . .')
            break
        else:
            print('\nOpção inválida. Por favor, tente novamente!')


if __name__ == "__main__":
    main()
