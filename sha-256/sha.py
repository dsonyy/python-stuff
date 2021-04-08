"""
Implementation of SHA-256 (secure hash algorithm). Created for educational purposes.
"""


def rotate_right(a, n):
    a %= 2**32
    n %= 32
    x = a % 2**n
    a >>= n
    a += 2**(32 - n) * x
    return a


def shift_right(a, n):
    return a >> n


def choose(x, y, z):
    return (x & y) ^ (~x & z)


def majority(x, y, z):
    return (x & y) ^ (x & z) ^ (y & z)


def sigma0(x):
    return rotate_right(x, 2) ^ rotate_right(x, 13) ^ rotate_right(x, 22)


def sigma1(x):
    return rotate_right(x, 6) ^ rotate_right(x, 11) ^ rotate_right(x, 25)


def gamma0(x):
    return rotate_right(x, 7) ^ rotate_right(x, 18) ^ shift_right(x, 3)


def gamma1(x):
    return rotate_right(x, 17) ^ rotate_right(x, 19) ^ shift_right(x, 10)


def fractional_part(n):
    r = 0
    for i in range(32):
        n *= 2
        r += int(n) * 2**(32 - i - 1)
        n -= int(n)
    return r


def calculate_primes_cube_roots():
    PRIMES = [2,   3,   5,   7,   11,  13,  17,  19,  23,  29,  31,  37,  41,  43,  47,  53,
              59,  61,  67,  71,  73,  79,  83,  89,  97,  101, 103, 107, 109, 113, 127, 131,
              137, 139, 149, 151, 157, 163, 167, 173, 179, 181, 191, 193, 197, 199, 211, 223,
              227, 229, 233, 239, 241, 251, 257, 263, 269, 271, 277, 281, 283, 293, 307, 311]
    K = []
    for i in range(64):
        n = PRIMES[i] ** (1/3)
        n -= int(n)
        K.append(fractional_part(n))
    return K


def print_primes_cube_roots(K):
    for n in K:
        print(hex(n))


if __name__ == "__main__":
    K = calculate_primes_cube_roots()
    print_primes_cube_roots(K)
    print(gamma0(123456))
