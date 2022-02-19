x = int(input('>'))

list = []
sum = 0
product = 1

while x != 0:
    list.append(x)
    if x % 2 == 0:
        sum += x
    x = int(input('>'))

for x in list:
    if x % 2 == 0:
        product *= x

print(sum, product)