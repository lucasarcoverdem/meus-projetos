class Bovine:
    def __init__(self, name, gender, breed, age, weight_kg, market_value):
        self.name = name
        self.gender = gender
        self.breed = breed
        self.age = age
        self.weight_kg = weight_kg
        self.market_value = market_value

    def describe(self):
        return '\n'.join([
            f'Nome: {self.name}',
            f'Gênero: {self.gender}',
            f'Raça: {self.breed}',
            f'Idade: {self.age}',
            f'Peso: {self.weight_kg}',
            f'Valor: {self.market_value}'
        ])
