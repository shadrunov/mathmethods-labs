"""encrypt with rsa"""


from math import floor, log


def dec_to_bin(dec: int, block_length: int = 7) -> str:
    # assert dec < 128
    return "0" * (block_length - len(bin(dec)[2:])) + bin(dec)[2:]


def ascii_to_binary(letter: str, block_length: int = 7) -> str:
    assert len(letter) == 1
    return dec_to_bin(ord(letter), block_length)


def main(test: str, e: int, n: int):

    bits = "".join([ascii_to_binary(letter) for letter in text])
    print("plain bits: ", bits)

    for d in text:
        print(f"{d} | {ord(d)} | {ascii_to_binary(d)}")

    block_length = floor(log(n, 2))
    print(
        "block_length: ",
        block_length,
        len(bits),
        len(bits) % block_length > 0,
        block_length - (len(bits) % block_length),
    )
    if len(bits) % block_length > 0:
        bits = "0" * (block_length - (len(bits) % block_length)) + bits

    out_numbers = []
    plain_numbers = []
    out_bits = []
    for k in range(0, len(bits), block_length):
        m = eval("0b" + bits[k : k + block_length])
        c = pow(m, e, n)
        plain_numbers.append(m)
        out_numbers.append(c)
        out_bit = dec_to_bin(c, block_length=block_length + 1)
        out_bits.append(out_bit)
        print(f"{bits[k:k + block_length]} | {m} | {c} | {out_bit}")

    print("plain numbers: ", plain_numbers)

    # to ascii 7-bit
    res = ""
    bits = "".join(out_bits)
    block_length = 7
    if len(bits) % block_length > 0:
        bits = "0" * (block_length - len(bits) % block_length) + bits
    for k in range(0, len(bits), block_length):
        m = eval("0b" + bits[k : k + block_length])
        res += repr(chr(m))

    return res, out_bits, out_numbers


text = input("type your message: ")
e = int(input("enter e: "))
n = int(input("enter n: "))
res, out_bits, out_numbers = main(text, e, n)
print("ciphertext: ", res)
print("cipher bits: ", "".join(out_bits))
print("cipher numbers: ", out_numbers)
