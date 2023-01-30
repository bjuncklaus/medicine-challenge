class Person():
    def __init__(self, height=.0, weight=.0, age=0, name=None, disease=None) -> None:
        self.height = height
        self.weight = weight
        self.age = age
        self.name = name
        self.disease = disease
    
    def __str__(self) -> str:
        return f'Height: {self.height}, Weight: {self.weight}, Age: {self.age}'

    def eat(self, food, kcal):
        print(f'Person: {self.name} ate {food} and added {kcal} to their weight.')
        self._add_weight(kcal)

    def _add_weight(self, amount_to_add):
        self.weight += self.weight*amount_to_add

    def get_weight(self):
        return self.weight

if __name__ == '__main__':
    isaque = Person(1.67, 51, 25, 'Isaque')
    print('person1:', isaque)
    isaque.eat('Pizza slice', 0.5)
    # print(isaque.get_weight())

    bruno = Person(1.82, 70.0, 33, 'Bruno')
    print('person2:', bruno)
    bruno.eat('Pizza slice', 0.5)
    # print(bruno.get_weight())
