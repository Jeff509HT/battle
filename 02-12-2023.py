a = "12-34-34A3-23"
total = 0
num = 0

for x in a:
    if x.isdigit():
        num = num * 10 + int(x)
    elif x == '-':
        total += num
        num = 0

total += num
print(total)
