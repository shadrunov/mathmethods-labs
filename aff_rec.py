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


def inv_el(el: int) -> int:
    m = len(LANG.alphabet)
    return pow(el, -1, m)


def user_input():
    global LANG
    global MODE

    t = int(input("аффинный рекуррентный шифр\n" "select language:\n" "1 - EN\n" "2 - RU\n" "Enter 1 or 2: "))
    assert t in (1, 2)
    LANG = Lang(t)

    t = input("Encrypt or decrypt? Enter:\n" "d - decrypt\n" "e - encrypt: ")
    assert t in ("d", "e")
    MODE = Mode(t)

    sequence = input("Enter a sequence: ").strip().upper()
    assert set(sequence).issubset(set(LANG.alphabet))
    assert len(sequence) > 1

    key_1 = (
        input(
            "Enter the first key -- two numbers separated by space.\n"
            f"The first one should be selected from the list below and the second is less than {len(LANG.alphabet)}.\n"
            f"{LANG.multiplicative_group} \n"
            "enter two numbers, e. g. 17 20: \n"
        )
        .strip()
        .upper()
    )
    assert " " in key_1, "wrong"
    key_1 = list(map(int, key_1.split(" ")))
    assert len(key_1) == 2
    assert str(key_1[0]) in LANG.multiplicative_group
    assert key_1[1] < len(LANG.alphabet)

    key_2 = (
        input(
            "Enter the second key -- two numbers separated by space.\n"
            f"The first one should be selected from the list below and the second is less than {len(LANG.alphabet)}.\n"
            f"{LANG.multiplicative_group} \n"
            "enter two numbers, e. g. 17 20: \n"
        )
        .strip()
        .upper()
    )
    assert " " in key_2, "wrong"
    key_2 = list(map(int, key_2.split(" ")))
    assert len(key_2) == 2
    assert str(key_2[0]) in LANG.multiplicative_group
    assert key_2[1] < len(LANG.alphabet)

    return (sequence, key_1, key_2)

    # TODO check len of sequence > 2

def decrypt(sequence: str, key_1: Tuple[int, int], key_2: Tuple[int, int], LANG: Lang = LANG) -> str:
    alpha_1, beta_1 = key_1
    alpha_2, beta_2 = key_2
    m = len(LANG.alphabet)
    y = [LANG.alphabet.find(i) for i in sequence]
    x = []

    x.append( ((y[0] - beta_1) * inv_el(alpha_1)) % m )
    # print(alpha_1, inv_el(alpha_1), beta_1, y[0], x[0])

    x.append( ((y[1] - beta_2) * inv_el(alpha_2)) % m )
    # print(alpha_2, inv_el(alpha_2), beta_2, y[1], x[1])

    for i in range(2, len(y)):
        alpha = alpha_1 * alpha_2 % m
        beta = (beta_1 + beta_2) % m

        x.append( ((y[i] - beta) * inv_el(alpha)) % m )

        # print(alpha, inv_el(alpha), beta, y[i], ( ((y[i] - beta) * inv_el(alpha)) ), x[i])

        alpha_1 = alpha_2
        beta_1 = beta_2
        alpha_2 = alpha
        beta_2 = beta

    return ''.join([ LANG.alphabet[i] for i in x ])

        # print(
        #     LANG.alphabet.find(i),
        #     alpha * LANG.alphabet.find(i) + beta,
        #     (alpha * LANG.alphabet.find(i) + beta) % m,
        #     LANG.alphabet[(alpha * LANG.alphabet.find(i) + beta) % m],
        # )
    # print(
        # "Elements of plain text: (",
        # ", ".join(map(str, x)),
        # ").",
    # )

def encrypt(sequence: str, key_1: Tuple[int, int], key_2: Tuple[int, int]) -> str:
    alpha_1, beta_1 = key_1
    alpha_2, beta_2 = key_2
    m = len(LANG.alphabet)
    x = [LANG.alphabet.find(i) for i in sequence]
    y = []

    y.append((alpha_1 * x[0] + beta_1) % m)
    # print(alpha_1, beta_1, x[0], y[0])

    y.append((alpha_2 * x[1] + beta_2) % m)
    # print(alpha_2, beta_2, x[1], y[1])

    for i in range(2, len(x)):
        alpha = alpha_1 * alpha_2 % m
        beta = (beta_1 + beta_2) % m

        y.append((alpha * x[i] + beta) % m)

        # print(alpha, beta, x[i], (alpha * x[i] + beta), y[i])

        alpha_1 = alpha_2
        beta_1 = beta_2
        alpha_2 = alpha
        beta_2 = beta

    return ''.join([ LANG.alphabet[i] for i in y ])

        # print(
        #     LANG.alphabet.find(i),
        #     alpha * LANG.alphabet.find(i) + beta,
        #     (alpha * LANG.alphabet.find(i) + beta) % m,
        #     LANG.alphabet[(alpha * LANG.alphabet.find(i) + beta) % m],
        # )
    # print(
        # "Elements of ciphertext: (",
        # ", ".join(map(str, y)),
        # ").",
    # )
    # return ''.join([ LANG.alphabet[(alpha * LANG.alphabet.find(i) + beta) % m] for i in sequence ])


if __name__ == "__main__":
    sequence, key_1, key_2 = user_input()
    if MODE.value == "d":
        print(decrypt(sequence, key_1, key_2))
    else:
        print(encrypt(sequence, key_1, key_2))

# wearediscovered
# ZEBRASCDFGHIJKLMNOPQTUVWXY
# VAZOARFPBLUAOAR

# 11 10
# SCKPCRUAGIHCPCR

# 11 10 17 20
# SKENMHOAIAFSPEF

# срочно
# ЧЯЮЭЫЬЁЩШЦЙХФУБДТЗВРПМЛКАИОЪЖЕСГН
# ВЗДАБД

# 17 20
# ЬЛКЯЪК

# 13 10 17 20
# МЛЛЬФЙ