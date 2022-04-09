import backend, questions
from datetime import date
from flask import Flask, request, jsonify
import json

app = Flask(__name__)



#We get today's date

#date_time = date.today().strftime("%m/%d/%Y")
#questionOfTheDay = backend.questionList[date_time]


# send them question
#questionTextToSend = questionOfTheDay.getText()
@app.route('/problem')
def getTodayProblem():
    date_time = date.today().strftime("%m/%d/%Y")
    questionOfTheDay = backend.questionList[date_time]
    questionTextToSend = questionOfTheDay.getText()
    return jsonify(questionTextToSend)

# get input code
#inputCodeFromServer: str = ("""def addN ums(num1, num2):
#    return num1 + num2""") # get code with api

# send them results
@app.route('/api')
def getResults():
    date_time = date.today().strftime("%m/%d/%Y")
    questionOfTheDay = backend.questionList[date_time]
    return questionOfTheDay.getResultsWithInput(request.get_json())


