#write your code here
target = 100
for number in range(1, target + 1):
    if number % 3 == 0 and number % 5 == 0: # and 생각하기!! << 생각도 몬함
        print("FizzBuzz")
    elif number % 3 == 0:
        print("Fizz")
    elif number % 5 == 0:
        print("Buzz")
    else:
        print(number)