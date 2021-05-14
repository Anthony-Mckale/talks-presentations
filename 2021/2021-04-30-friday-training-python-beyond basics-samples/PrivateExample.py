class PrivateClass():
    def __init__(self):
        self.__mr_private_var = "world"
        self.mr_public_var = "hello"

    def get_private_var(self) -> str:
        return self.__mr_private_var


private_class = PrivateClass()

print(private_class.mr_public_var)
print(private_class.get_private_var())
print(private_class.__mr_private_var)
