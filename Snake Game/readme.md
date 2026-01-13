# 🐍 Snake Game (Python Turtle)

A classic **Snake Game** built using **Python's Turtle graphics** and **Object-Oriented Programming (OOP)** principles. The player controls a snake that grows in length by eating food while avoiding collisions with the wall and its own body.

---

## 🎮 Features

* Smooth snake movement using `screen.tracer()` and manual screen updates
* Keyboard controls (⬆️ ⬇️ ⬅️ ➡️)
* Random food generation
* Score tracking with a scoreboard
* Game over detection:

  * Collision with walls
  * Collision with snake's own body
* Clean and modular OOP-based structure

---

## 🛠️ Tech Stack

* **Language:** Python
* **Library:** Turtle Graphics
* **Concepts Used:**

  * Object-Oriented Programming (OOP)
  * Event handling
  * Game loop
  * Collision detection

---

## 📁 Project Structure

```
Snake-Game/
│
├── main.py          # Main game loop
├── snake.py         # Snake class (movement & growth)
├── food.py          # Food class (random food placement)
├── scoreboard.py    # Scoreboard & game-over logic
└── README.md        # Project documentation
```

---

## ⌨️ Controls

| Key | Action     |
| --- | ---------- |
| ↑   | Move Up    |
| ↓   | Move Down  |
| ←   | Move Left  |
| →   | Move Right |

---

## 🚀 How to Run the Game

1. Make sure **Python (3.x)** is installed on your system
2. Clone this repository:

```bash
git clone https://github.com/your-username/snake-game.git
```

3. Navigate to the project folder:

```bash
cd snake-game
```

4. Run the game:

```bash
python main.py
```

---

## 🧠 Game Logic Overview

* The snake moves continuously using a game loop
* Food appears at random positions
* When the snake eats food:

  * Snake length increases
  * Score increases
* Game ends if:

  * Snake hits the wall
  * Snake collides with its own body

---

## 📸 Preview


<img width="748" height="785" alt="Screenshot 2026-01-13 222907" src="https://github.com/user-attachments/assets/46fec41f-aa58-4066-83d9-ab66a4c71124" />

---

## ✨ Learning Outcomes

* Improved understanding of **Python OOP**
* Hands-on experience with **Turtle graphics**
* Better grasp of game loops and collision logic
* Code organization using multiple classes

