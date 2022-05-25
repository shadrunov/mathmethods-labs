# Самоключ Виженера по открытому тексту

from enum import Enum


class Lang(Enum):
    EN = 1
    RU = 2

    @property
    def alphabet(self):
        if self.value == 1:
            return "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        return "АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ"

    @property
    def multiplicative_group(self):
        if self.value == 1:
            return [1, 3, 5, 7, 9, 11, 15, 17, 19, 21, 23, 25]
        return [1,2,4,5,7,8,10,13,14,16,17,19,20,23,25,26,28,29,31,32]

    @property
    def modulo(self):
        if self.value == 1:
            return 26
        return 33


class Mode(Enum):
    Decrypt = "d"
    Encrypt = "e"


class Cryptosystem:
    def __init__(self) -> None:
        self.input_params()

    lang: Lang
    mode: Mode
    key: str

    def input_params(self):

        t = int(
            input(
                "Vigenere cipher\n\n"
                "select language:\n"
                "1 - EN\n"
                "2 - RU\n"
                "Enter 1 or 2: "
            )
        )
        assert t in (1, 2)
        self.lang = Lang(t)

        t = input("Encrypt or decrypt? Enter:\n" "d - decrypt\n" "e - encrypt: ")
        assert t in ("d", "e")
        self.mode = Mode(t)

        key = (
            input("Enter key. This is one symbol of the same alphabet\n")
            .strip()
            .upper()
        )
        assert set(key).issubset(set(self.lang.alphabet))
        self.key = key

    def input_text(self) -> str:
        sequence = input("Enter a sequence: ").strip().upper()
        assert set(sequence).issubset(set(self.lang.alphabet))
        return sequence

    def decrypt(self, text: str) -> str:
        sequence = [self.lang.alphabet.find(i) for i in text]
        res = []
        res.append((sequence[0] - self.lang.alphabet.find(self.key)) % self.lang.modulo)
        for i in range(1, len(sequence)):
            res.append((sequence[i] - res[i-1]) % self.lang.modulo)
            # print(res)

        return "".join([self.lang.alphabet[int(i)] for i in res])

    def encrypt(self, text: str) -> str:

        gamma = self.key + text[:-1]
        # print(gamma)
        gamma = [self.lang.alphabet.find(i) for i in gamma]
        # print(gamma)
        sequence = [self.lang.alphabet.find(i) for i in text]
        # print(sequence)

        res = [(gamma[i] + sequence[i]) % self.lang.modulo for i in range(len(sequence))]
        # print(res)
        return "".join([self.lang.alphabet[i] for i in res])

    def __call__(self, test: str) -> str:
        if self.mode.value == "e":
            return self.encrypt(text)
        return self.decrypt(text)


if __name__ == "__main__":
    cs = Cryptosystem()
    text = cs.input_text()
    result = cs(text)
    print(result)
