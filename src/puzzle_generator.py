import random

def generate_puzzle(level):
    if level == "Easy":
        a, b = random.randint(1, 10), random.randint(1, 10)
        op = random.choice(["+", "-"])
    elif level == "Medium":
        a, b = random.randint(10, 50), random.randint(1, 10)
        op = random.choice(["+", "-", "*"])
    else:
        a, b = random.randint(10, 100), random.randint(2, 12)
        op = random.choice(["+", "-", "*", "/"])
    
    question = f"{a} {op} {b}"
    correct = eval(question)
    return question, round(correct, 2)
