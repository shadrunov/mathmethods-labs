from enum import Enum
from typing import Tuple


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
            return "(1, 3, 5, 7, 9, 11, 15, 17, 19, 21, 23, 25)"
        return "(1, 2, 4, 5, 7, 8, 10, 13, 14, 16, 17, 19, 20, 23, 25, 26, 28, 29, 31, 32)"


class Mode(Enum):
    Decrypt = "d"
    Encrypt = "e"


LANG = Lang(1)
MODE = Mode("d")


def user_input():
    global LANG
    global MODE

    t = int(input("affine cipher\n" "select language:\n" "1 - EN\n" "2 - RU\n" "Enter 1 or 2: "))
    assert t in (1, 2)
    LANG = Lang(t)

    t = input("Encrypt or decrypt? Enter:\n" "d - decrypt\n" "e - encrypt: ")
    assert t in ("d", "e")
    MODE = Mode(t)

    sequence = input("Enter a sequence: ").strip().upper()
    assert set(sequence).issubset(set(LANG.alphabet))

    key = (
        input(
            "Enter the key -- two numbers separated by space.\n"
            f"The first one should be selected from the list below and the second is less than {len(LANG.alphabet)}.\n"
            f"{LANG.multiplicative_group} \n"
            "enter two numbers, e. g. 17 20: \n"
        )
        .strip()
        .upper()
    )
    assert " " in key, "wrong"
    key = list(map(int, key.split(" ")))
    assert len(key) == 2
    assert str(key[0]) in LANG.multiplicative_group
    assert key[1] < len(LANG.alphabet)

    return (sequence, key)


def decrypt(sequence: str, key: Tuple[int, int], LANG: Lang = LANG) -> str:
    alpha, beta = key
    m = len(LANG.alphabet)
    alpha_inv = pow(alpha, -1, m)
    # for i in sequence:
    #     print(
    #         LANG.alphabet.find(i),
    #         alpha_inv * (LANG.alphabet.find(i) - beta),
    #         (alpha_inv * (LANG.alphabet.find(i) - beta)) % m,
    #         LANG.alphabet[(alpha_inv * (LANG.alphabet.find(i) - beta)) % m],
    #     )

    # print(
    #     "Elements of ciphertext: (",
    #     ", ".join(map(str, [(alpha_inv * (LANG.alphabet.find(i) - beta)) % m for i in sequence])),
    #     ").",
    # )
    return ''.join([ LANG.alphabet[(alpha_inv * (LANG.alphabet.find(i) - beta)) % m] for i in sequence ])


def encrypt(sequence: str, key: Tuple[int, int]) -> str:
    alpha, beta = key
    m = len(LANG.alphabet)
    # for i in sequence:
    #     print(
    #         LANG.alphabet.find(i),
    #         alpha * LANG.alphabet.find(i) + beta,
    #         (alpha * LANG.alphabet.find(i) + beta) % m,
    #         LANG.alphabet[(alpha * LANG.alphabet.find(i) + beta) % m],
    #     )
    # print(
    #     "Elements of ciphertext: (",
    #     ", ".join(map(str, [(alpha * LANG.alphabet.find(i) + beta) % m for i in sequence])),
    #     ").",
    # )
    return ''.join([ LANG.alphabet[(alpha * LANG.alphabet.find(i) + beta) % m] for i in sequence ])


if __name__ == "__main__":
    sequence, key = user_input()
    if MODE.value == "d":
        print(decrypt(sequence, key))
    else:
        print(encrypt(sequence, key))

# wearediscovered
# ZEBRASCDFGHIJKLMNOPQTUVWXY
# VAZOARFPBLUAOAR

# 11 10
# SCKPCRUAGIHCPCR

# срочно
# ЧЯЮЭЫЬЁЩШЦЙХФУБДТЗВРПМЛКАИОЪЖЕСГН
# ВЗДАБД

# 17 20
# ЬЛКЯЪК