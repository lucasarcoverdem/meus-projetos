class Employee:
    def __init__(self, name, role, salary, age, gender):
        self.name = name
        self.role = role
        self.salary = salary
        self.age = age
        self.gender = gender

    def describe(self):
        return '\n'.join([
            f'Nome: {self.name}',
            f'Função: {self.role}',
            f'Salário: {self.salary}',
            f'Idade: {self.age}',
            f'Gênero: {self.gender}'
        ])
        
