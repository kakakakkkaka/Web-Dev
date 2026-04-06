x = input()
decimal = 0
l = len(x)

for i in range(l):
    digit = int(x[i])
    decimal += digit * (2 ** (l - 1 - i))
print(decimal)