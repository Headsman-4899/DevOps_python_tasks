def find_perfect_numbers(start, end):
    perfect_numbers = []

    for num in range(start, end + 1):
        divisors_sum = 0

        for divisor in range(1, num):
            if num % divisor == 0:
                divisors_sum += divisor

        if divisors_sum == num:
            perfect_numbers.append(num)

    return perfect_numbers

result = find_perfect_numbers(0, 1000)
print("Совершенные числа в диапазоне от 0 до 1000: ", result)
