import backend, questions
from datetime import date


#We get today's date

#date_time = date.today().strftime("%m/%d/%Y")
#questionOfTheDay = backend.questionList[date_time]


# send them question
#questionTextToSend = questionOfTheDay.getText()

def getTodayProblem():
    date_time = date.today().strftime("%m/%d/%Y")
    questionOfTheDay = backend.questionList[date_time]
    questionTextToSend = questionOfTheDay.getText()
    return questionTextToSend

# get input code
#inputCodeFromServer: str = ("""def addN ums(num1, num2):
#    return num1 + num2""") # get code with api

# send them results

def getResults(inputCodeFromServer: str):
    date_time = date.today().strftime("%m/%d/%Y")
    questionOfTheDay = backend.questionList[date_time]
    return questionOfTheDay.getResultsWithInput(inputCodeFromServer)


