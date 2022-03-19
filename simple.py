from enum import Enum


class Lang(Enum):
    EN = 1
    RU = 2

    @property
    def alphabet(self):
        if self.value == 1:
            return "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        return "АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ"


class Mode(Enum):
    Decrypt = "d"
    Encrypt = "e"


LANG = Lang(1)
MODE = Mode("d")


def user_input():
    global LANG
    global MODE

    t = int(
        input(
            "simple substitution cipher\n"
            "select language:\n"
            "1 - EN\n"
            "2 - RU\n"
            "Enter 1 or 2: "
        )
    )
    assert t in (1, 2)
    LANG = Lang(t)

    t = input("Encrypt or decrypt? Enter:\n" "d - decrypt\n" "e - encrypt: ")
    assert t in ("d", "e")
    MODE = Mode(t)

    sequence = input("Enter a sequence: ").strip().upper()
    assert set(sequence).issubset(set(LANG.alphabet))

    key = (
        input("Enter key. This is a transposition of the aplphabet:\n" + LANG.alphabet + "\n")
        .strip()
        .upper()
    )
    assert set(key) == set(LANG.alphabet)

    return (sequence, key)


def decrypt(sequence: str, key: str) -> str:
    return "".join([LANG.alphabet[key.find(i)] for i in sequence])


def encrypt(sequence: str, key: str) -> str:
    return "".join([key[LANG.alphabet.find(i)] for i in sequence])


if __name__ == "__main__":
    sequence, key = user_input()
    if MODE.value == "d":
        print(decrypt(sequence, key))
    else:
        print(encrypt(sequence, key))

# wearediscovered
# ZEBRASCDFGHIJKLMNOPQTUVWXY
# VAZOARFPBLUAOAR

# срочно
# ЧЯЮЭЫЬЁЩШЦЙХФУБДТЗВРПМЛКАИОЪЖЕСГН
# ВЗДАБД
