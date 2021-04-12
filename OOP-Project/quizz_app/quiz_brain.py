from question_model import Question


class QuizBrain:

    def __init__(self, question_list):
        self.question_number = 0
        self.question_list = question_list
        self.score = 0

    def still_has_questions(self):
        if self.question_number < len(self.question_list):
            return True
        else:
            print("\n")
            print("You have completed the quiz")
            print(f"Your final score is: {self.score}/{len(self.question_list)}")
            return False

    def next_question(self):
        while self.still_has_questions():
            current_question: Question = self.question_list[self.question_number]
            self.question_number += 1
            answer = input(f"Q.{self.question_number}: {current_question.text} (True/False): ").lower()
            self.check_answer(answer, current_question.answer)

    def check_answer(self, user_answer, question_answer):
        if question_answer.lower() == user_answer.lower():
            self.score += 1
            print("You got it right!")
        else:
            print("Wrong")
        print(f"Correct Answer was: {question_answer}")
        print(f"Your score is: {self.score}/{self.question_number}")
        print("\n")
