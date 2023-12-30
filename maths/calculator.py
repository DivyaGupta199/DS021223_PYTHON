def addition(*number):
    add = sum(number)
    return add

def substraction(n1,n2):
    sub = n1 - n2
    return sub

def multiplication(*numbers):
    product = 1
    for i in numbers:
        product *= i

    return product

def division(n1,n2):
    d = n1/n2
    return d

