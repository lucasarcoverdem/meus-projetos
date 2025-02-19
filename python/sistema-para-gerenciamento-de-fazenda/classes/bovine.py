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

    def to_dict(self):
        return {
            "name": self.name,
            "gender": self.gender,
            "breed": self.breed,
            "age": self.age,
            "weight_kg": self.weight_kg,
            "market_value": self.market_value
        }

    @classmethod
    def from_dict(cls, data):
        return cls(**data)
