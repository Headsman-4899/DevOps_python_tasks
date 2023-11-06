def calc_eposit(n, k, b):
    for _ in range(n):
        b += (k / 100) * b

    return b

n, k, b = map(int, input().split())
print(calc_eposit(n, k, b))
