from prime import generate_prime_number
from math import gcd


def generate_keys(length: int):
    def _generate_keys(length: int):
        p = generate_prime_number(length)
        q = generate_prime_number(length)
        n = p * q
        phi = (p - 1) * (q - 1)
        # phi = 480
        for e in [3, 5, 17, 257, 65537]:
            if e != p and e != q and gcd(phi, e) == 1:
                break
        # print(p, q, n, phi, e)

        d = pow(e, -1, phi)
        return e, d, n, p, q, phi

    e, d, phi = 1, 1, 1
    while (e * d % phi != 1):
        e, d, n, p, q, phi = _generate_keys(length)
    return e, d, n, p, q
    
        

    

if __name__ == "__main__":
    l = int(input())
    e, d, n, p, q = generate_keys(l)
    print('e =', e, ' n =', n, ' d =', d, p, q)
