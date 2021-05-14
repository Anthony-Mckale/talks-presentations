class EzeMathExpection(Exception):
    def __init__(self, value: str, expected_value: str):
        # do something
        self.value = value
        self.expected_value = expected_value
        self.message = f"Eze math problem got {value} but expected {expected_value}"


try:
    raise EzeMathExpection(1, 2)
except EzeMathExpection as err:
    print(err.message)
