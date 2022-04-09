

# Takes in a string from front end and runs it with exec
# Need to account for malicious input 


# Each question has 6 test function parameters as functions
# There will be ONE question for each day.
# correctOutput MUST have length 6 (to match the 6 test functions)
# text is the question/problem text i.e. create a function that returns the ....

class question():
    def __init__(self, text: str, correctOutput: list, fun1, fun2, fun3, fun4, fun5, fun6):
        self.text = text
        self.correctOutput = correctOutput
        self.tests = [fun1, fun2, fun3, fun4, fun5, fun6]

    def getText(self):
        return self.text

    def getCorrectOutput(self):
        print(self.getCorrectOutput())

    #This function tests the output. It creates a field outputList which will store the results of running each test.
    def testOutput(self):
        self.outputList = [0, 0, 0, 0, 0, 0]
        for i in range(len(self.correctOutput)):
            try:
                self.outputList[i] = self.tests[i]()
            except:
                #catch exception - we can provide more details as to exception here
                print("fail")
                self.outputList[i] = "FAILURE - EXCEPTION"
    
    def getOutputList(self):
        return self.outputList


    #Unlike testOutput, this function returns a tuple with whether or not the tests were successful
    def getResults(self):
        self.correctList = [1, 2, 3, 4, 5, 6]
        outputList = ["", 2, 3, 4 ,5, 6]
        for i in range(len(self.correctOutput)):
            try:
                outputList[i] = (self.correctOutput[i] == self.tests[i]())
            except:
                #catch exception
                print("fail")
                outputList[i] = "failure - exception thrown"
                
        return outputList

    def getResultsWithInput(self, inputString: str):
        exec(inputString, globals)
        self.correctList = [1, 2, 3, 4, 5, 6]
        outputList = ["", 2, 3, 4 ,5, 6]
        for i in range(len(self.correctOutput)):
            try:
                outputList[i] = (self.correctOutput[i] == self.tests[i]())
            except:
                #catch exception
                print("fail")
                
        return outputList

        




#Test Case - works perfectly. We see that, when using a function that works, "5" is correctly placed in the results list, and
#when using a function that does not work, an exception is thrown which is added to the results
def fun1():
    return 5

def fun2():
    return dog()

questionTest = question("What's 5?", [5, 5, 5, 5, 5, 5], fun1, fun1, fun1, fun1, fun1, fun2)

questionTest.testOutput()
output = questionTest.getOutputList()
print(questionTest.getResults())
print(output)



