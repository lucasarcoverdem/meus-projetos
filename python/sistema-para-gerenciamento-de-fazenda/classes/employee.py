class Employee:
    def __init__(self, name, role, age, gender):
        self.name = name
        self.role = role
        self.age = age
        self.gender = gender

    def describe(self):
        return '\n'.join([
            f'Nome: {self.name}',
            f'Função: {self.role}',
            f'Idade: {self.age}',
            f'Gênero: {self.gender}'
        ])
