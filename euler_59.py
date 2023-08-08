from itertools import product
import nltk
nltk.download('words')
from nltk.corpus import words

f = open("0059_cipher.txt", "r")
l = f.read().split(',')
l = [int(n) for n in l]

eng = set(words.words())

lower_char = list(product(range(97, 123), repeat=3))

phrase = ""

for code in lower_char:
    temp = ""
    for i in range(len(l)):
        temp += chr(l[i] ^ code[i % 3])
    if temp.split(' ')[0].lower() in eng and temp.split(' ')[1].lower() in eng:
        phrase = temp
        break

phrase_ascii = sum([ord(n) for n in phrase])

print(phrase_ascii)