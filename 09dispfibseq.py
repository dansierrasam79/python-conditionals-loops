# fibonnaci sequence
num = 0
num2 = 1
fib_num = 0
print(num)
print(num2)
while fib_num < 50:
    fib_num = num + num2
    print(fib_num)
    num, num2 = num2, fib_num