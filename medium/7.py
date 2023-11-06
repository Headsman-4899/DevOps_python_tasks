def is_perfect_number(num):
    divisors_sum = 0

    for divisor in range(1, num):
        if num % divisor == 0:
            divisors_sum += divisor

    return divisors_sum == num


number = int(input())

if is_perfect_number(number):
    print("число совершенное")
else:
    print("число не совершенное")
