from question_model import Question
from data import question_data
from quiz_brain import QuizBrain

question_bank = []
for q in question_data:
    new_q = Question(text=q["text"], answer=q["answer"])
    question_bank.append(new_q)

quiz_brain = QuizBrain(question_bank)
quiz_brain.next_question()

# for i in question_bank:
#     print(i.text, i.answer)

