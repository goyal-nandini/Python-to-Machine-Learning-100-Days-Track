import html
import requests
from question_model import Question
from quiz_brain import QuizBrain

url = "https://opentdb.com/api.php?amount=10&category=18&type=boolean"
response = requests.get(url)
data = response.json()

question_bank = []

for q in data["results"]:
    quest = html.unescape(q["question"]) 
    question = Question(quest, q["correct_answer"])
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
'''
