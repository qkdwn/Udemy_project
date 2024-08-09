def prime_checker(number):
    is_primt = True
    for i in range(2, number):
        if number % i == 0:
            is_prime = False

n = int(input())
prime_checker(number=n)