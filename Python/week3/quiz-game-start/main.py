from question_model import Question
from data import question_data2
from quiz_brain import QuizBrain
import os
import time

question_bank = list()

for data in question_data2:
    question_text = data['question']
    question_answer = data['correct_answer']
    new_question = Question(question_text, question_answer)
    question_bank.append(new_question)

quiz = QuizBrain(question_bank)

while quiz.still_has_questions():
    quiz.next_question()
    time.sleep(2)
    os.system('cls')

print("You've completed the quiz.")
print(f"Your final score is {quiz.score}/{quiz.question_number}.")
