from aff_rec import decrypt, Lang

LANG = Lang(1)

n_freq = {
    "E": 12.02,
    "T": 9.10,
    "A": 8.12,
    "O": 7.68,
    "I": 7.31,
    "N": 6.95,
    "S": 6.28,
    "R": 6.02,
    "H": 5.92,
    "D": 4.32,
    "L": 3.98,
    "U": 2.88,
    "C": 2.71,
    "M": 2.61,
    "F": 2.30,
    "Y": 2.11,
    "W": 2.09,
    "G": 2.03,
    "P": 1.82,
    "B": 1.49,
    "V": 1.11,
    "K": 0.69,
    "X": 0.17,
    "Q": 0.11,
    "J": 0.10,
    "Z": 0.07,
}

f_freq = {}

res = []

counter = 0

y = input()
m = len(LANG.alphabet)
print()

for a in [1, 3, 5, 7, 9, 11, 15, 17, 19, 21, 23, 25]:
    for b in range(26):
        for c in [1, 3, 5, 7, 9, 11, 15, 17, 19, 21, 23, 25]:
            for d in range(26):
                x = decrypt(y, (a, b), (c, d), LANG)
                for letter in n_freq.keys():
                    f_freq[letter] = x.count(letter) / len(x)
                chi = sum([n_freq[key] * f_freq[key] for key in n_freq.keys()])
                res.append((chi, x))
                counter += 1
                if counter % 1000 == 0: 
                    print(counter / 97344 * 100, "%")

res.sort(key=lambda t: t[0], reverse=True)
for i in res[:5]:
    print(i[0], " | ", i[1][:70], "...")
