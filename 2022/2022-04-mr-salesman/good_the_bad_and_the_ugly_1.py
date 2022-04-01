import time

size = 1000000 * 1
tic = time.perf_counter()

numbers = []
for i in range(1, size):
    numbers.append(i)

sum = 0
for number in numbers:
    sum += number

toc = time.perf_counter()
print(f"1 to {size} = {sum}")
print(f"""{(toc - tic):.05f} seconds""")
# 1 to 1000000 = 499999500000
# 0.18943 seconds