class QuizzBrain:

    def __init__(self, q_list):
        self.question_number = 0
        self.question_list = q_list
        self.score = 0
        self.score_total = 0

    def next_question(self):
        current_question = self.question_list[self.question_number]
        user = input(f"Q.{self.question_number+1} {current_question.text} (True/False) ?")


        if user.capitalize() == current_question.answer:
            self.score += 1
            score_total = (f"{self.score}/{self.question_number + 1}")
            print(f"You got it right! \nThe correct answer was {current_question.answer}\nYour current score is {score_total}")
        else:
            score_total = (f"{self.score}/{self.question_number+1}")
            print(f"You got it wrong :(  \nThe correct answer was {current_question.answer}\nYour current score is {score_total}")
        self.question_number +=1
        self.score_total = score_total