"""encrypt with rsa"""


from math import floor, log


def dec_to_bin(dec: int, block_length: int = 7) -> str:
    # assert dec < 128
    return '0' * (block_length - len(bin(dec)[2:])) + bin(dec)[2:]


def ascii_to_binary(letter: str, block_length: int = 7) -> str:
    assert len(letter) == 1
    return dec_to_bin(ord(letter), block_length)


def main(bits: str, d: int, n: int):

    block_length = floor(log(n, 2)) + 1
    if len(bits) % (block_length) > 0:
        bits = '0' * (block_length - len(bits) % block_length) + bits
    print("block_length: ", block_length, len(bits) % block_length > 0, block_length - len(bits) % block_length)
    print(bits)

    out_numbers = []
    out_bits = []
    for k in range(0, len(bits), block_length):
        c = eval('0b' + bits[k:k + block_length])
        m = pow(c, d, n)
        out_numbers.append(m)
        out_bits.append(dec_to_bin(m, block_length=block_length - 1))
        print(f"{bits[k:k + block_length]} | {c} | {m} | {dec_to_bin(m, block_length=block_length - 1)}")

    # to ascii 7-bit
    res = ''
    bits = ''.join(out_bits)
    block_length = 7
    if len(bits) % block_length > 0:
        bits = '0' * (block_length - len(bits) % block_length) + bits
    for k in range(0, len(bits), block_length):
        c = eval('0b' + bits[k:k + block_length])
        res += repr(chr(c))

    return res, out_bits, out_numbers


print("Bits / Text? ")
t = input()

if t.casefold() == 'b':
    mode = 'b'
    bits = input('type your bits (0 & 1): ')
    # print(set(bits))
    assert set(bits) == {'0', '1'}
elif t.casefold() == 't':
    mode = 't'
    text = input('type your message in plain text: ')
    bits = ''.join([ascii_to_binary() for letter in text])
    for d in text:
        print(f"{d} | {ord(d)} | {ascii_to_binary(d)}")

d = int(input('enter d: '))
n = int(input('enter n: '))

res, out_bits, out_numbers = main(bits, d, n)
# res, out_bits, out_numbers = main('1001100110011100000110110111011010001100000011010101011011100100100011', 953, 1147)
print('plain text: ', res)
print('plain bits: ', ''.join(out_bits))
print('plain numbers: ', out_numbers)

