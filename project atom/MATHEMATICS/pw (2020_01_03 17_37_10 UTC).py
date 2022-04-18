import sys

cache_limit = 5000001
results = [0] * cache_limit
results[0] = 1

def create_sequence(starting_number):

    if starting_number < cache_limit and results[starting_number - 1] != 0:
        return results[starting_number - 1]
    else:
        result = 0
        if starting_number % 2 == 0:
            result = 1 + create_sequence(starting_number >>1)
        else:
            result = 1 + create_sequence(3 * starting_number + 1)
        if starting_number < cache_limit:
            results[starting_number-1] = result

        return result

for i in range(1, 5000000):
    create_sequence(i)
j
