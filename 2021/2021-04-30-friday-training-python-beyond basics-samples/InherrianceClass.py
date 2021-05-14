class LifeClass():
    def __init__(self, name: str):
        # do something
        self.name = name

    def can_breath(self) -> str:
        return f"{self.name} maybe can"


class AnimalClass(LifeClass):
    def can_breath(self) -> str:
        return f"yes {self.name} can, i'm breathing oxygen"

    def walk(self) -> str:
        return "i'm walking on the road"


life = LifeClass('blob')
print(life.can_breath())
animal = AnimalClass('cat')
print(animal.can_breath())
print(animal.walk())
