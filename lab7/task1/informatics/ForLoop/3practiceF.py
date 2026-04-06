x = input()
rev = ""

for c in x[::-1]:
    rev += c


print(int(rev))