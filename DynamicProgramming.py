# Online Python compiler (interpreter) to run Python online.
# Write Python 3 code in this online editor and run it.
print("Dynamic Programming")
print("1! x 2! x 3! x .. x n!")

sumsum = 1
num = int(input())
for xx in range(1, num + 1):
    sum = 1
    for x in range(1, xx + 1):
        sum *= x
    print(x, " != ", sum)
    sumsum *= sum
print(sumsum, " = ", sumsum)