import time

size = 1000000 * 1
tic = time.perf_counter()

sum = 0
# for number in range(1, size):
#    sum += number

i = 0
while i <= size:
    sum += i
    i += 1
    # if i % 10000 == 0:
    #     print(f"1 to {i} = {sum}")
    # print(f"1 to {i} = {sum}")

toc = time.perf_counter()
print(f"1 to {size} = {sum}")
print(f"""{(toc - tic):.05f} seconds""")
# 1 to 1000000 = 499999500000
# 0.07962 seconds