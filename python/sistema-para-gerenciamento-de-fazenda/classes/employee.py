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

    def to_dict(self):
        return {
            "name": self.name,
            "role": self.role,
            "salary": self.salary,
            "age": self.age,
            "gender": self.gender
        }

    @classmethod
    def from_dict(cls, data):
        return cls(**data)
