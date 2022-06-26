def print_val(n):
    if n == 1: return print(1)
    print_val(n-1)
    print(n)

print_val(10)