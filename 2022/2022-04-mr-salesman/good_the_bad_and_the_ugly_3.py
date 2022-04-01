import time

size = 1000000 * 1000 * 1000
tic = time.perf_counter()

sum = (1 + size) * size * .5

toc = time.perf_counter()
print(f"1 to {size} = {sum}")
print(f"""{(toc - tic):.05f} seconds""")
# 1 to 1000000 = 500000500000.0
# 0.00000 seconds