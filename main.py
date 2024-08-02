from data import question_data
from question_model import Question
from quiz_brain import QuizBrain

question_bank = []
for items in question_data:
    question_text = items["text"]
    question_answer = items["answer"]
    new_question = Question(question_text, question_answer)
    #print(new_question.question)
    question_bank.append(new_question)
quiz = QuizBrain(question_bank)
quiz.nextQuestion()

while quiz.stillHasQuestions():
    quiz.nextQuestion()
print("You've completed the quiz")
print(f"yor final sores were : {quiz.score}/{quiz.question_number}")