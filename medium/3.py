def is_prime(number):
    if number <= 1:
        return False 

    for i in range(2, int(number**0.5) + 1):
        if number % i == 0:
            return False

    return True


num = int(input())
result = is_prime(num)
if result:
    print(f"{num} является простым числом")
else:
    print(f"{num} не является простым числом")
