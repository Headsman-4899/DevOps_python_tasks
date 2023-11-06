a, b = map(int, input().split())
result = []

for i in range(a, b+1):
    if i % 2 == 0:
        result.append(i)

print(result)
