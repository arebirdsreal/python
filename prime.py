def is_prime(num):
    if num == 0 or num == 1:
        return False
    elif num >= 2:
        for i in range(2, (num//2)+1):
            if num % i == 0:
                return False
        return True
print(is_prime(73))
print(is_prime(75))