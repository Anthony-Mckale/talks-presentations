class ExampleClass:
    static_var = "static_var"

    def __init__(self):
        # do something
        self.instance_var = "some_var"

    def do_some_thing(self, value: str):
        # ...
        print(self.__dict__)
        return self.instance_var + value

    @staticmethod
    def do_some_static_thing(value: str):
        # ...
        return value


print(ExampleClass.static_var)
# echo static_var
print(ExampleClass.do_some_static_thing("static_func asgasdjhasd"))
# echo static_func

example = ExampleClass()
example.instance_var = '322323'
print(example.instance_var)
# echo some_var
print(example.do_some_thing("_func"))
# echo some_var_func
