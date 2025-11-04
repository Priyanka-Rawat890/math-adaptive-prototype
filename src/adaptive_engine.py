def adjust_difficulty(performance, current):
    if performance["accuracy"] > 80 and performance["avg_time"] < 10:
        return "Hard" if current == "Medium" else "Medium" if current == "Easy" else "Hard"
    elif performance["accuracy"] < 50:
        return "Easy" if current == "Medium" else "Medium" if current == "Hard" else "Easy"
    else:
        return current
