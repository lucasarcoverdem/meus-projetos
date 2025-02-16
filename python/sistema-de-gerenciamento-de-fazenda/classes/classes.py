class Bovine:
    def __init__(self, name, gender, breed, age, weight, value):
        self.name = name
        self.gender = gender
        self.breed = breed
        self.age = age
        self.weight = weight
        self.value = value

    def describe(self):
        print(f'Nome: {self.name}')
        print(f'Gênero: {self.gender}')
        print(f'Raça: {self.breed}')
        print(f'Idade: {self.age} anos')
        print(f'Peso: {self.weight} kg')
        print(f'Valor: R$ {self.value:.2f}')

    def __str__(self):
        return (f'Bovino: {self.name}, {self.gender}, {self.breed}, '
                f'{self.age} anos, {self.weight} kg, R$ {self.value:.2f}')

    def to_dict(self):
        return vars(self)

    @classmethod
    def from_dict(cls, data):
        return cls(**data)

    def update_value(self, new_value):
        """Atualiza o valor do bovino."""
        self.value = new_value
        print(f'Novo valor atualizado para {self.name}: R$ {self.value:.2f}')


class MilkProduction:
    def __init__(self, date, amount):
        self.date = date
        self.amount = amount

    def describe(self):
        print(f'Data da produção: {self.date}')
        print(f'Quantidade: {self.amount} litros')

    def __str__(self):
        return f'Produção de leite em {self.date}: {self.amount} litros'

    def to_dict(self):
        return vars(self)

    @classmethod
    def from_dict(cls, data):
        return cls(**data)

    def update_amount(self, new_amount):
        """Atualiza a quantidade de leite produzida."""
        self.amount = new_amount
        print(f'Nova quantidade de leite produzida em {self.date}: {self.amount} litros')


class Employee:
    def __init__(self, name, role, wage, age, gender):
        self.name = name
        self.role = role
        self.wage = wage
        self.age = age
        self.gender = gender

    def describe(self):
        print(f'Nome: {self.name}')
        print(f'Função: {self.role}')
        print(f'Salário: R$ {self.wage:.2f}')
        print(f'Idade: {self.age} anos')
        print(f'Gênero: {self.gender}')

    def __str__(self):
        return (f'Funcionário: {self.name}, {self.role}, '
                f'R$ {self.wage:.2f}, {self.age} anos, {self.gender}')

    def to_dict(self):
        return vars(self)

    @classmethod
    def from_dict(cls, data):
        return cls(**data)

    def update_wage(self, new_wage):
        """Atualiza o salário do funcionário."""
        self.wage = new_wage
        print(f'Novo salário de {self.name}: R$ {self.wage:.2f}')

