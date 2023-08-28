from itertools import permutations

r = list(permutations(range(1, 11), 3))

counter = []

for pair1 in [tup for tup in r if tup[0] < 7]:
    s = sum(pair1)
    for pair2 in [
        tup for tup in r if tup[0] > pair1[0]
            and tup[0] not in pair1
            and tup[1] == pair1[2]
            and tup[2] not in pair1
            and sum(tup) == s
    ]:
        for pair3 in [
            tup for tup in r if tup[0] > pair1[0]
                and tup[0] not in pair1 + pair2
                and tup[1] == pair2[2]
                and tup[2] not in pair1 + pair2
                and sum(tup) == s
        ]:
            for pair4 in [
                tup for tup in r if tup[0] > pair1[0]
                    and tup[0] not in pair1 + pair2 + pair3
                    and tup[1] == pair3[2]
                    and tup[2] not in pair1 + pair2 + pair3
                    and sum(tup) == s
            ]:
                last_value = list(set(range(1, 11)) - set(pair1 + pair2 + pair3 + pair4))[0]
                if last_value > pair1[0] and s == last_value + pair4[2] + pair1[1]:
                    output = pair1 + pair2 + pair3 + pair4 + (last_value, pair4[2], pair1[1])
                    counter.append(''.join(map(str, output)))

print(max([int(num) for num in counter if len(num) == 16]))
