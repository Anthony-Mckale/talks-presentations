import sys

from fib import fib

if __name__ == "__main__":
    count = sys.argv[1]
    print(f"outputing fib to {count}")
    fib(int(count))
