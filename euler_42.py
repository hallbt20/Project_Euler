tri_num = [n * (n + 1) // 2 for n in range(1, 100)]


def is_triangular(n):
    return n in tri_num


def word_to_num(word):
    output = 0
    for letter in word:
        output += (ord(letter) - 64)
    return output


with open('words.txt') as f:
    lines = f.readlines()
counter = 0
for word in lines[0].split(","):
    if is_triangular(word_to_num(word.strip('"'))):
        counter += 1
print(counter)