#  Math Adventures — Adaptive Learning Prototype

### 📘 Objective

This project demonstrates an **AI-powered adaptive math learning prototype** that dynamically adjusts problem difficulty based on learner performance.

###  Features

- Three difficulty levels: **Easy**, **Medium**, **Hard**
- Tracks **accuracy** and **response time**
- Uses **rule-based adaptive logic** to modify difficulty
- Displays **end-of-session summary** with recommended next level

###  How It Works

1. User enters name and selects starting difficulty.  
2. Program generates math puzzles based on the difficulty.  
3. User answers puzzles; correctness and response time are recorded.  
4. Adaptive engine adjusts the difficulty automatically:
   - If accuracy > 80% and avg time < 10s → increase difficulty  
   - If accuracy < 50% → decrease difficulty  
   - Otherwise → keep same level  
5. Displays performance summary after 5 puzzles.

###  Folder Structure

math-adaptive-prototype/
├─ README.md
├─ requirements.txt
└─ src/
├─ main.ipynb
├─ puzzle_generator.py
├─ tracker.py
└─ adaptive_engine.py


###  How to Run

1. Open `src/main.ipynb` in **Jupyter Notebook**.  
2. Run all cells in order.  
3. Answer each math question when prompted.  
4. View your performance summary at the end.

###  Adaptive Logic Used

A **rule-based approach** — it uses accuracy and average response time to adapt the next question’s difficulty dynamically.

###  Developer

**Priyanka Rawat**

---
