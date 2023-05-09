def name_score(name, rank):
    score = 0
    
    for letter in name:
        score += ord(letter) - 64

    return score*rank

with open('names.txt', 'r') as file:
    names = sorted(file.read().replace('"', '').split(","))

counter = 0

for i in range(len(names)):
    counter += name_score(names[i], i + 1)
