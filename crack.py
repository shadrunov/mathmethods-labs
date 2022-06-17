# c = int(input('type c number: '))
# e = int(input('type public key exponent e: '))
# n = int(input('type modulus n: '))

c, e, n = 519884, 5, 601229

j = 1
m = 0
t = pow(c, e, n)
print(f"{j} | {t} | {c}")

while t != c:
    print(f"{j} | {t} | {c}")
    j += 1
    m = t
    t = pow(t, e, n)


print(f"{j} | {t} | {c}")
print("plain number: ", m)
