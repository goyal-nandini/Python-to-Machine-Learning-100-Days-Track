# 🐢 Turtle Race Game (Python Turtle)

A fun and interactive **Turtle Race Game** built using Python’s **Turtle graphics** module. The user places a bet on a turtle color, and the turtles race across the screen with random movement until a winner is declared.

---

# 📸 Preview
<img width="616" height="533" alt="Screenshot 2026-01-13 223159" src="https://github.com/user-attachments/assets/2ca37cfe-a8b3-4327-8fd5-a4df77f69bad" />
<img width="617" height="533" alt="Screenshot 2026-01-13 223250" src="https://github.com/user-attachments/assets/3cdbd2b6-b5bc-4f25-bcbe-a9960f1e8b8c" />

<img width="619" height="535" alt="Screenshot 2026-01-13 223230" src="https://github.com/user-attachments/assets/fb6b50f2-d5ea-4a51-b9ec-0f3aa5a9ee5f" />

---

## 🎮 Game Overview

* Six turtles of different colors participate in a race
* The user bets on which turtle will win
* Each turtle moves forward by a random distance every round
* The first turtle to cross the finish line wins
* The result is displayed both in the terminal and on the screen

---

## ✨ Features

* User input using a pop-up dialog box
* Randomized turtle movement for unpredictability
* Visual race animation using Turtle graphics
* Winner announcement displayed on the screen
* Simple and beginner-friendly logic

---

## 🛠️ Tech Stack

* **Language:** Python
* **Library:** Turtle
* **Concepts Used:**

  * Loops and conditionals
  * Lists and iteration
  * Randomization
  * Event-driven graphics

---

## 📁 Project Structure

```
Turtle-Race-Game/
│
├── main.py      # Complete turtle race game logic
└── README.md    # Project documentation
```

---

## 🎨 Turtle Colors

The available turtles (and betting options) are:

* Red
* Orange
* Yellow
* Green
* Blue
* Purple

---

## 🚀 How to Run the Game

1. Ensure **Python 3.x** is installed on your system
2. Clone this repository or download the source code
3. Navigate to the project folder
4. Run the game using:

```bash
python main.py
```

---

## 🧠 Game Logic Explanation

* The user is prompted to place a bet by choosing a turtle color
* All turtles start from the same x-position but different y-positions
* In each iteration of the race loop:

  * Turtle order is shuffled to reduce bias
  * Each turtle moves forward by a random distance (0–10)
* When a turtle crosses the finish line:

  * The race stops
  * The winning turtle’s color is compared with the user’s bet
  * The result is announced

---

## ⚠️ Known Behavior / Observation

* If a turtle crosses the finish line during a loop iteration, the race ends immediately
* Turtles later in the loop may not get a move in that round
* This can introduce a very small advantage depending on iteration order
* Shuffling the turtle list each round helps minimize this bias

---

## 📚 Learning Outcomes

* Understanding of Turtle graphics
* Using randomness to simulate real-world behavior
* Handling user input via dialog boxes
* Managing simple game states
* Identifying and reasoning about algorithmic bias

---

Happy Racing! 🐢🏁
