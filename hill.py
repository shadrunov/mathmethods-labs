from enum import Enum
from typing import List, Tuple

import numpy as np
from numpy.typing import ArrayLike


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
        return [1, 2, 4, 5, 7, 8, 10, 13, 14, 16, 17, 19, 20, 23, 25, 26, 28, 29, 31, 32]

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
    n: int
    key: ArrayLike

    def input_params(self):

        t = int(input("hill cipher\n" "select language:\n" "1 - EN\n" "2 - RU\n" "Enter 1 or 2: "))
        assert t in (1, 2)
        self.lang = Lang(t)

        t = input("Encrypt or decrypt? Enter:\n" "d - decrypt\n" "e - encrypt: ")
        assert t in ("d", "e")
        self.mode = Mode(t)

        t = int(input("Enter N (length of blocks):\n"))
        assert t > 0
        self.n = t

        det = 0
        while det not in self.lang.multiplicative_group:
            key: List[List[int]] = []
            print(
                "Enter the key. It is an invertible matrix.\n"
                "Enter it row by row, separate numbers with spaces,\n"
                "press enter after each line. \n"
                f"remember, every line contains {self.n} values\n"
                f"and matrix contains {self.n} rows: \n"
            )
            for _ in range(self.n):
                line = list(map(int, input().strip().split(" ")))
                assert len(line) == self.n
                assert all(i < self.lang.modulo for i in line)
                key.append(line)

            self.key = np.array(key)
            det = round(np.linalg.det(self.key)) % self.lang.modulo
            print(det)
            if det not in self.lang.multiplicative_group:
                print("incorrect matrix, try again")

    def input_text(self) -> str:
        sequence = input("Enter a sequence: ").strip().upper()
        assert set(sequence).issubset(set(self.lang.alphabet))
        return sequence

    def inverse_matrix(self, A, p):  # Finds the inverse of matrix A mod p
        n = len(A)
        A = np.matrix(A)
        adj = np.zeros(shape=(n, n))
        for i in range(0, n):
            for j in range(0, n):
                adj[i][j] = ((-1) ** (i + j) * int(round(np.linalg.det(self.minor(A, j, i))))) % p
        return (pow(int(round(np.linalg.det(A))), -1, p) * adj) % p

    def minor(self, A, i, j):  # Return matrix A with the ith row and jth column deleted
        A = np.array(A)
        minor = np.zeros(shape=(len(A) - 1, len(A) - 1))
        row = 0
        for minor_row in range(0, len(minor)):
            if row == i:
                row = row + 1
            col = 0
            for minor_col in range(0, len(minor)):
                if col == j:
                    col = col + 1
                minor[minor_row][minor_col] = A[row][col]
                col = col + 1
            row = row + 1
        return minor

    def decrypt(self, text: str) -> str:
        sequence = [self.lang.alphabet.find(i) for i in text]

        res = []
        for i in range(0, len(sequence), self.n):
            block = sequence[i : i + self.n]
            res_block = (
                np.matmul(self.inverse_matrix(self.key, self.lang.modulo), block) % self.lang.modulo
            )
            res.extend(res_block)
            # print(res)

        return "".join([self.lang.alphabet[int(i)] for i in res])

    def encrypt(self, text: str) -> str:

        sequence = [self.lang.alphabet.find(i) for i in text]
        # print(sequence)
        while len(sequence) % self.n > 0:
            sequence.append(0)
        # print(sequence)

        res = []
        for i in range(0, len(sequence), self.n):
            block = sequence[i : i + self.n]
            res_block = np.matmul(self.key, block) % self.lang.modulo
            res.extend(res_block)
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

