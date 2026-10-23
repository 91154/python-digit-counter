x = int (input("x : "))

i = 0
while x > 0:
    x //= 10
    i += 1
print(i)
