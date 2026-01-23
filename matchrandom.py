import random
import string

possibleCharacters = string.ascii_lowercase + string.digits + \
                        string.ascii_uppercase + ' ., !? ;:'


t = "geek"

def generate_random_string(length):
    return ''.join(random.choice(possibleCharacters) for _ in range(length))

def fitness(current):
    return sum(1 for a,b in zip(current, t) if a==b)

def mutate(parent):
    index = random.randint(0, len(parent) - 1)
    child = list(parent)
    child[index] = random.choice(possibleCharacters)
    return ''.join(child)

attempt = generate_random_string(len(t))
iteration = 0

while attempt != t:
    print(attempt)
    new_attempt = mutate(attempt)
    if fitness(new_attempt) >= fitness(attempt):
        attempt = new_attempt
    
    iteration += 1

print(f"Target matched after {iteration} iterations")

