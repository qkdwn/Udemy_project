target = int(input())

even_sum = 0
for number in range(2, target + 1, 2): #특정 숫자까지의 범위를 만들려면 해당 숫자에 1을 더한 값을 넣어야 한다.
    even_sum += number
print(even_sum)

alternative_sum = 0
for number in range(1, target + 1):
    if number % 2 == 0:
        alternative_sum += number
print(alternative_sum)