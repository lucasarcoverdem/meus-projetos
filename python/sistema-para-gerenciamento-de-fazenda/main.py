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

    name = input('\nInsira o nome do bovino: ').strip().lower().capitalize()

    while True:
        gender = normalize(input('Insira o gênero do bovino (boi, vaca): ').strip())

        if gender in ['boi', 'vaca']:
            break
        else:
            print('\nEntrada inválida. Por favor, digite "boi" ou "vaca".')    

    breed = input('Insira a raça do bovino: ').strip().lower().capitalize()

    while True:
        try:
            age = float(input('Insira a idade do bovino (anos, ex: 0.5 para 5 meses): ').strip())
            if age < 0:
                print("\nA idade não pode ser negativa. Tente novamente.")
            else:
                break
        except ValueError:
            print('\nEntrada inválida. Digite um número válido (ex: 0.5 para 5 meses).')

    while True:    
        try:
            weight_kg = float(input('Insira o peso do bovino (kg): ').strip())
            if weight_kg <= 0:
                print("\nO peso deve ser maior que zero.")
            else:
                break
        except ValueError:
            print('\nEntrada inválida. Digite um número válido (ex: 500.5).')

    while True:
        try:
            market_value = float(input('Insira o valor de mercado do bovino (R$): ').strip())
            if market_value < 0:
                print("\nO valor de mercado não pode ser negativo.")
            else:
                break
        except ValueError:
            print('\nEntrada inválida. Digite um número válido (ex: 3500.75).')

    new_bovine = Bovine(name, gender, breed, age, weight_kg, market_value)
    cattle.append(new_bovine)

    print(f'\n{name} adicionado com sucesso!')


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
        return 
    else:
        print("\nOpção inválida. Tente novamente.")


def login():
    user = input('Digite seu nome de usuário: ').strip().lower().capitalize()
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
