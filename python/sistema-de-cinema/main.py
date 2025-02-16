films = ['Ainda Estou Aqui', 'Emilia Perez', 'A Substância', 'Wicked', 'O Auto da Compadecida 2']
prices = [25.00, 30.00, 20.00, 35.00, 15.00]

def filmsOptions(films):
    """Exibe os filmes disponíveis."""
    print('\nFilmes em cartaz: \n')
    for i, film in enumerate(films, start=1):
        print(f'{i} - {film}')

def filmsOptionsPrices(films, prices):
    """Exibe os filmes disponíveis com seus preços."""
    print('\nFilmes em cartaz: \n')
    for i, (film, price) in enumerate(zip(films, prices), start=1):
        print(f'{i} - {film}: R${price:.2f}')

def filmsOnDisplay(films, prices):
    """Exibe a lista de filmes em cartaz e opções de navegação."""
    filmsOptions(films)

    while True:
        menu = input(
            '\n- - -\n'
            '1 - Voltar\n'
            '2 - Comprar ingressos\n\n'
            'Escolha uma opção: '
        ).lower()

        if menu in ['1', 'voltar']:
            break
        elif menu in ['2', 'comprar ingressos']:
            tickets(films, prices)
        else:
            print('\nOpção inválida! Tente novamente...\n')

def chairsSelecting():
    """Solicita a seleção de uma cadeira entre 1 e 36."""
    while True:
        chairSelect = input(
            '\n- - -\n\n'
            '[1 - 12: Frente\n'
            '13 - 30: Meio\n'
            '31 - 36: Final]\n\n'
            'Escolha sua cadeira (1-36): '
        )
        if chairSelect.isdigit() and 1 <= int(chairSelect) <= 36:
            return int(chairSelect)
        else:
            print("Número de cadeira inválido! Por favor, escolha entre 1 e 36.")

def tickets(films, prices):
    """Realiza a compra de ingressos para o filme escolhido."""
    filmsOptionsPrices(films, prices)

    while True:
        filmBuyed = input(
            '\nQual filme deseja comprar? (1, 2...): '
        )

        if filmBuyed.isdigit() and 1 <= int(filmBuyed) <= len(films):
            chairSelect = chairsSelecting()
            print(f'\nIngresso comprado para o filme "{films[int(filmBuyed) - 1]}" na cadeira {chairSelect}.')
            break
        else:
            print('\nOpção inválida! Tente novamente...\n')

def main(films, prices):
    """Menu principal do Cinema Moviemax."""
    while True:
        print(
            '- - - M O V I E M A X - - -\n\n'
            'Bem-vindo ao Cinema Moviemax!\n'
        )

        menu = input(
            '1 - Filmes em cartaz\n'
            '2 - Comprar ingressos\n'
            '3 - Sair\n\n'
            'Escolha uma opção: '
        ).lower()

        if menu in ['1', 'filmes em cartaz']:
            filmsOnDisplay(films, prices)
        elif menu in ['2', 'comprar ingressos']:
            tickets(films, prices)
        elif menu in ['3', 'sair']:
            print('\nObrigado por usar o Cinema Moviemax. Até logo!\n')
            break
        else:
            print('\nOpção inválida! Tente novamente...\n')

if __name__ == "__main__":
    main(films, prices)
