'''requests is a third-party Python library, which we import as a module, and it 
provides functions like get() that return Response objects.
all doubts 🤔 👇'''
import requests
from question_model import Question
from quiz_brain import QuizBrain

url = "https://opentdb.com/api.php?amount=10&category=18&type=boolean"
response = requests.get(url)
data = response.json()

question_bank = []

for q in data["results"]:
    question = Question(q["question"], q["correct_answer"])
    question_bank.append(question)


quizbrain = QuizBrain(question_bank) 
while quizbrain.still_has_questions(): 
    quizbrain.next_question()

print(f"You've completed the quiz,\nYour Final Score was: {quizbrain.score}/{len(question_bank)}")

''' WORKING FLOW:
Internet
   ↓
GET request
   ↓
JSON response
   ↓
Python dictionary
   ↓
Question objects
   ↓
QuizBrain

👉⌚add info:
requests → library (big)

requests → module (what you import)

Response → class inside it

get() → function you call

👉⌚que as doubt and ans:
Q🤔: What does .json() do?

It converts JSON response data into a Python dictionary.

Q🤔: Difference between JSON and dictionary?

JSON is a text-based data format, while a dictionary is a Python data structure.

Q🤔: What is requests?

requests is a Python module used to send HTTP requests.

Q🤔: What is response?

response is an object returned by requests.get() containing server response data.
'''
