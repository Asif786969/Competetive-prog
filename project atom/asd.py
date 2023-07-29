def hash_string(s):
    p = 31  # a prime number
    m = 10**9 + 9  # a large prime number

    hash_value = 0
    p_pow = 1
    for c in s:
        hash_value = (hash_value + (ord(c) - ord('a') + 1) * p_pow) % m
        p_pow = (p_pow * p) % m

    return hash_value
print(hash_string("aab"))