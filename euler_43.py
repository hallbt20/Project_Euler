from itertools import permutations

prime_nums = [2, 3, 5, 7, 11, 13, 17]

def substring_divisibility(n):
    for i in range(1, 8):
        if int(n[i:i+3]) % prime_nums[i - 1]:
            return False
    return True


counter = 0
for perm in list(permutations(range(10))):
    perm = ''.join([str(num) for num in perm])
    if substring_divisibility(perm):
        counter += int(perm)
print(counter)