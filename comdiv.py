def num():
    a = int(input("Enter first number"))
    b = int(input("Enter second number"))

    n = min(a, b)
    for i in range(1, n):
        if a%i == 0 & b%i == 0:
            print(i)


num()
