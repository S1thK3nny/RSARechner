def is_prime(n):
    if n <= 1:
        return False
    elif n <= 3:
        return True
    elif n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True



def must_be_prime(value): 
    number = int(value) 
    if is_prime(number):
        return number
    else: 
        raise TypeError("Die Zahl muss eine Primzahl sein!")