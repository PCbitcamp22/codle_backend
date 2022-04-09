import backend, questions
from datetime import date


#We get today's date
date_time = date.today().strftime("%m/%d/%Y")
questionOfTheDay = backend.questionList[date_time]


# send them question
questionTextToSend = questionOfTheDay.getText()

# get input code
inputCodeFromServer: str = ("""def addNums(num1, num2):
    return nums + num2""") # get code with api

# send them results

#exec(inputCodeFromServer, globals())
results = questionOfTheDay.getResultsWithInput(inputCodeFromServer)
print(results)


