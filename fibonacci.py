fibonacci = int(input("How many Fibonacci numbers? "))
a = 0
b = 1
for i in range(fibonacci):
    print(a)
    first = a
    a = b
    b = first + a

