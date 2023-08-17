seq = [2, 1, 2]

for i in range(100 - 3):
    if i % 3 == 2:
        seq.append(2 * (i // 3) + 4)
    else:
        seq.append(1)

seq = seq[::-1]

def f(numer, denom, next_num):
    return numer + denom * next_num, denom

output = f(1, seq[0], seq[1])

for i in range(1, len(seq) - 1):
    output = f(output[1], output[0], seq[i + 1])

print(sum([int(n) for n in str(output[0])]))
