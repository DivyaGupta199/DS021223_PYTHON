def isprime(number):
    if number == 1:
        return False
    
    elif number == 2:
        return True

    elif number > 2:
        for i in range(2, number):
            if number % i == 0:
                return False
            
        return True
    
    else:
        print("Please provide a natural number")

def is_num_positve(num):
    if num < 0:
        print("The number is Negative")
    elif num == 0:
        print("The is Zero")
    else:
        print("The number is positive")

def sorting(*numbers):
    lst = list(numbers)
    lst.sort(reverse = True)
    print(lst)

def table(number = 7):
    for i in range(1,11):
        print(f"{number}*{i} = {number*i}")


if __name__ == "__main__":
    result = isprime(11)
    print(result)

