"""gen rsa keys"""

from random import randrange, getrandbits


def is_prime(n: int, k: int = 128) -> bool:
    """Test if a number is prime

    :param n: prime candidate
    :type n: int
    :param k: number of test iterations, defaults to 128
    :type k: int, optional
    :return: return True if n is prime
    :rtype: bool
    """
    # Test if n is not even.
    # But care, 2 is prime !
    if n == 2 or n == 3:
        return True
    if n <= 1 or n % 2 == 0:
        return False

    # # Fermat primality test
    # for _ in range(k):
    #     a = randrange(2, n)
    #     r = pow(a, n - 1, n)
    #     if r != 1:
    #         return False
    # return True

    # find r and s
    s = 0
    r = n - 1
    while r & 1 == 0:
        s += 1
        r //= 2
    # do k tests
    for _ in range(k):
        a = randrange(2, n - 1)
        x = pow(a, r, n)
        if x != 1 and x != n - 1:
            j = 1
            while j < s and x != n - 1:
                x = pow(x, 2, n)
                if x == 1:
                    return False
                j += 1
            if x != n - 1:
                return False
    return True



def generate_prime_candidate(length: int) -> int:
    """Generate an odd integer randomly

    :param length: the length of the number to generate, in bits
    :type length: int
    :return: prime_candidate
    :rtype: int
    """

    # generate random bits
    p = getrandbits(length)
    # apply a mask to set MSB and LSB to 1
    p |= (1 << length - 1) | 1
    return p


def generate_prime_number(length: int = 1024) -> int:
    """Generate a prime

    :param length: length of the prime to generate, in bits, defaults to 1024
    :type length: int, optional
    :return: return a prime
    :rtype: int
    """

    p = 4
    # keep generating while the primality test fail
    while not is_prime(p, 128):
        p = generate_prime_candidate(length)
    return p


if __name__ == "__main__":
    print(generate_prime_number(20))
