class QuizBrain:

    def __init__(self, q_list):
        self.question_number = 0
        self.question_list = q_list
        self.score = 0

    def nextQuestion(self):
        currentQuestion = self.question_list[self.question_number]
        self.question_number += 1
        userAnswer = input(
            f"Q.{self.question_number}: {currentQuestion.question} (True/False): "
        )
        self.checkAnswer(userAnswer, currentQuestion.answer)

    #def calculateScore(self, operation):
    #    if operation == "add":
    #        return self.score + 1
    #    else:
    #        return self.score - 1

    def checkAnswer(self, userAnswer, correctAnswer):
        if userAnswer.lower() == correctAnswer.lower():
            print(
                f"you got it right! \n The correct answer was: {correctAnswer} \n The next question is below"
            )
            #currentScore = calculateScore("add")
            self.score+=1
            print(
                f"your currect score is {self.score}/{self.question_number} \n"
            )

        else:
            print(f"That's wrong. \n The correct answer was: {correctAnswer}")
            #currentScore = calculateScore("sub")
            print(
                f"your currect score is {self.score}/{self.question_number} \n"
            )

    def stillHasQuestions(self):
        return self.question_number < len(self.question_list)
