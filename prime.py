def IsPrime(value):
    if value <= 1:
        return False
    for i in range(2, value):
        if value % i == 0:
            return False
    return True