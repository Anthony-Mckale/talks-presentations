class SetterGetterClass():
    def __init__(self):
        self.dump = {}

    def __setattr__(self, key, value):
        print(f"something tried to set var '{key}' to {value}")

    def __getattribute__(self, key):
        print(self, key)
        return f"something called var '{key}'"


getter = SetterGetterClass()

print(getter.ghost)

getter.world = 3
