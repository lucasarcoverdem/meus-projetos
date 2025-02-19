import unicodedata

from classes.bovine import Bovine
from classes.milkproduction import MilkProduction
from classes.employee import Employee

cattle = []
milk_production = []
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
            print('\nEntrada inválida. Por favor, digite "boi" ou "vaca".\n')

    breed = input('Insira a raça do bovino: ').strip().lower().capitalize()

    while True:
        try:
            age = float(input('Insira a idade do bovino (anos, ex: 0.5 para 5 meses): ').strip())
            if age < 0:
                print("\nA idade não pode ser negativa. Tente novamente.\n")
            else:
                break
        except ValueError:
            print('\nEntrada inválida. Digite um número válido (ex: 0.5 para 5 meses).\n')

    while True:
        try:
            weight_kg = float(input('Insira o peso do bovino (kg): ').strip())
            if weight_kg <= 0:
                print("\nO peso deve ser maior que zero.\n")
            else:
                break
        except ValueError:
            print('\nEntrada inválida. Digite um número válido (ex: 500.5).\n')

    while True:
        try:
            market_value = float(input('Insira o valor de mercado do bovino (R$): ').strip())
            if market_value < 0:
                print("\nO valor de mercado não pode ser negativo.\n")
            else:
                break
        except ValueError:
            print('\nEntrada inválida. Digite um número válido (ex: 3500.75).\n')

    new_bovine = Bovine(name, gender, breed, age, weight_kg, market_value)
    cattle.append(new_bovine)
    print(f'\n{name} adicionado com sucesso!')


def remove_bovine():
    print('\n- Remover bovino')
    while True:
        if not cattle:
            print('\nNão há bovinos para remover!')
            break

        removed_bovine = input('\nInsira o nome do bovino a ser removido: ').strip().lower().capitalize()

        for bovine in cattle:
            if bovine.name == removed_bovine:
                cattle.remove(bovine)
                print(f'\n{removed_bovine} removido com sucesso!')
                return

        print('\nBovino não encontrado! Tente novamente.')


def view_cattle():
    print('\n- Ver gado')
    if not cattle:
        print('\nNão há gado registrado!')
        return

    print('\nLista de Bovinos:')
    print('-' * 30)
    for i, bovine in enumerate(cattle, start=1):
        print(f'{i} - {bovine.describe()}')
        print('-' * 30)


def cattle_function():
    print('\n- Gado')
    menu = input('\n1 - Registrar bovino\n2 - Remover bovino\n3 - Ver gado registrado\n4 - Voltar\n(1, 2...): ').strip().lower().replace(" ", "")
    menu = normalize(menu)

    if menu in ['1', 'registrarbovino']:
        register_bovine()
    elif menu in ['2', 'removerbovino']:
        remove_bovine()
    elif menu in ['3', 'vergadoregistrado']:
        view_cattle()
    elif menu == '4':
        return
    else:
        print("\nOpção inválida. Tente novamente.")


def register_milk_production():
    print('\n- Registrar produção')
    production_date = input('Insira a data da produção (dd/mm/yyyy): ').strip()

    while True:
        try:
            amount = float(input('Insira a quantidade produzida (litros): ').strip())
            if amount < 0:
                print('\nA quantidade não pode ser negativa. Tente novamente.')
            else:
                break
        except ValueError:
            print('\nEntrada inválida. Digite um número válido.')

    new_production = MilkProduction(production_date, amount)
    milk_production.append(new_production)
    print('\nProdução registrada com sucesso!')


def view_milk_production():
    print('\n- Ver produções')
    if not milk_production:
        print('\nNão há produções registradas!')
        return

    print('\nRegistro:')
    print('-' * 30)
    for i, production in enumerate(milk_production, start=1):
        print(f'{i} - {production.describe()}')
        print('-' * 30)


def milk_function():
    print('\n- Leite')
    menu = input('\n1 - Registrar produção\n2 - Ver produção\n3 - Voltar\n(1, 2...): ').strip().lower().replace(" ", "")
    menu = normalize(menu)

    if menu in ['1', 'registrarproducao']:
        register_milk_production()
    elif menu in ['2', 'verproducao']:
        view_milk_production()
    elif menu in ['3', 'voltar']:
        return
    else:
        print('\nOpção inválida. Tente novamente!')


def view_current_team():
    print('\n- Ver equipe atual')
    if not team:
        print('\nNão há funcionários registrados!')
        return
    
    print('\nEquipe:')
    print('-' * 30)


def register_employee():
    print('\n- Registrar funcionário')

    name = input('\nInsira o nome do funcionário: ').strip().lower().capitalize()
    role = input('Insira a função do funcionário ("Aprendiz" p/ jovem aprendiz): ').strip().lower().capitalize()

    while True:
        try:
            salary = float(input('Insira o salário do funcionário (R$ p/ semana): ').strip())
            if salary * 4 < 1518:
                print('\nSalário abaixo do imposto pelas Leis Trabalhistas!\n')
            else:
                break
        except ValueError:
            print('\nValor inválido. Digite um número.\n')

    while True:
        try:
            age = int(input('Insira a idade do funcionário: ').strip())
            if age < 18 and role != 'Aprendiz':
                print('\nIdade inválida para a função!\n')
            else:
                break
        except ValueError:
            print('\nValor inválido. Digite um número.\n')

    while True:
        gender = input('Insira o gênero do funcionário (fem / masc): ').strip().lower()
        if gender not in ['fem', 'masc']:
            print('\nDigite "fem" ou "masc"!\n')
        else:
            break

    new_employee = Employee(name, role, salary, age, gender)
    team.append(new_employee)
    
    print(f'{new_employee.name} registrado com sucesso!')


def remove_employee():
    print('\n- Demitir funcionário')
    while True:
        if not team:
            print('\nNão há funcionários para demitir!')
            break

        removed_employee = input('\nInsira o nome do funcionário a ser demitido: ').strip().lower().capitalize()

        for employee in team:
            if employee.name == removed_employee:
                team.remove(employee)
                print(f'\n{removed_employee} removido com sucesso!')
                return

        print('\nFuncionário não encontrado! Tente novamente.')


def team_function():
    print('\n- Equipe')
    menu = input('\n1 - Ver equipe atual\n2 - Registrar funcionário\n3 - Demitir funcionário\n4 - Voltar\n(1, 2...): ').strip().lower().replace(" ", "")
    menu = normalize(menu)

    if menu in ['1', 'verequipeatual']:
        view_current_team()
    elif menu in ['2', 'registrarfuncionario']:
        register_employee()
    elif menu in ['3', 'demitirfuncionario']:
        remove_employee()
    elif menu in ['4', 'voltar']:
        return


def login():
    user = input('Digite seu nome de usuário: ').strip().lower().capitalize()
    password = input('Digite sua senha: ')
    print('Entrando. . .')
    return user


def main():
    user = login()
    print('\n- - - F A Z E N D A B A N A N I R A - - -')
    print(f'\nSeja bem-vindo, {user}!')

    while True:
        menu = input('\n1 - Gerenciar gado\n2 - Gerenciar produção\n3 - Gerenciar equipe\n4 - Sair\n(1, 2...): ').strip().lower().replace(" ", "")
        menu = normalize(menu)

        if menu in ['1', 'gerenciargado']:
            cattle_function()
        elif menu in ['2', 'gerenciarproducao']:
            milk_function()
        elif menu in ['3', 'gerenciarequipe']:
            team_function()
        elif menu == '4':
            print('\nEncerrando. . .')
            break
        else:
            print('\nOpção inválida. Por favor, tente novamente!')


if __name__ == "__main__":
    main()
