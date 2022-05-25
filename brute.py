alphabet = "АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ"

text = "ЁНЦЩЬСБРБЪЦЯ"
sequence = [alphabet.find(i) for i in text]

with open("res.txt", "w") as file:
    for a in alphabet:
        print(a)
        for b in alphabet:
            for c in alphabet:
                for d in alphabet:
                    key = a + b + c + d
                    gamma = key * 3
                    gamma = [alphabet.find(i) for i in gamma]
                    res = [(sequence[i] - gamma[i]) % 33 for i in range(len(sequence))]
                    # print("".join([alphabet[i] for i in res]))
                    res = key + " | " + "".join([alphabet[i] for i in res]) + "\n"
                    file.write(res)
