def is_fibonacci_number(num):
    a, b = 0, 1
    while a < num:
        a, b = b, a + b

    return a == num

if is_fibonacci_number(21):
    print("является числом Фибоначчи")
else:
    print("не является числом Фибоначчи")
