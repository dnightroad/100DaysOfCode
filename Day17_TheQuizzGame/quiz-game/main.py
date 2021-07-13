from question_model import Question
from data import question_data
from quiz_brain import *
question_bank = []
new_quizz = QuizzBrain(question_bank)
for question in question_data:
        question_text = question["text"]
        question_answer = question["answer"]
        new_question = Question(question_text, question_answer)
        question_bank.append(new_question)
        new_quizz.next_question()
score = new_quizz.score_total
print()
print(f"You've completed the quiz\nYour final score is {score}")



