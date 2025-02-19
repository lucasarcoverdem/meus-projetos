class MilkProduction:
    def __init__(self, production_date, amount):
        self.production_date = production_date
        self.amount = amount

    def describe(self):
        return '\n'.join([
            f'Data: {self.production_date}',
            f'Quantidade: {self.amount}'
        ])
    
    def to_dict(self):
        return {
            "production_date": self.production_date,
            "amount": self.amount
        }

    @classmethod
    def from_dict(cls, data):
        return cls(**data)
