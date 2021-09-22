num = 987

sum = 0
while num > 9:
    n = num
    while n != 0:
        sum = sum + (n % 10)
        n //= 10
        # print(sum)
    num = sum
    sum = 0
    print(num)
print('last sum', num)
