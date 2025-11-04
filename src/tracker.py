import time

class PerformanceTracker:
    def __init__(self):
        self.records = []

    def start_timer(self):
        self.start = time.time()

    def stop_timer(self):
        return time.time() - self.start

    def log(self, correct, time_taken, difficulty):
        self.records.append({
            "correct": correct,
            "time": time_taken,
            "difficulty": difficulty
        })

    def summary(self):
        total = len(self.records)
        correct = sum(1 for r in self.records if r["correct"])
        avg_time = sum(r["time"] for r in self.records) / total
        accuracy = correct / total * 100
        return {"accuracy": accuracy, "avg_time": round(avg_time, 2)}
