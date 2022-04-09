

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
            print(self.correctOutput)

    #This function tests the output. It creates a field outputList which will store the results of running each test.
    #def testOutput(self):
    #    self.outputList = [0, 0, 0, 0, 0, 0]
    #    for i in range(len(self.correctOutput)):
    #        try:
    #            self.outputList[i] = self.tests[i]()
    #        except:
    #            #catch exception - we can provide more details as to exception here
    #            print("fail")
    #            self.outputList[i] = "FAILURE - EXCEPTION"
    
    #def getOutputList(self):
    #    return self.outputList


    #Unlike testOutput, this function returns a tuple with whether or not the tests were successful
    #def getResults(self):
    #    outputList = ["", 2, 3, 4 ,5, 6]
    #    for i in range(len(self.correctOutput)):
    #        try:
    #            outputList[i] = (self.correctOutput[i] == self.tests[i]())
    #        except:
    #            #catch exception
    #            print("fail")
    #            outputList[i] = "failure - exception thrown"
    #            
    #    return outputList

    def getResultsWithInput(self, inputString: str):
        outputList = ["", 2, 3, 4 ,5, 6]

        try:
            exec(inputString, globals())
        
        except:
            #catch exception
            print("failure during function definition")
            outputList = [3, 3, 3, 3, 3, 3]        #3's mean failed during function definition
            return outputList
           
        
        for i in range(len(self.correctOutput)):
            try:
                exec(inputString, globals())
                if (self.correctOutput[i] == self.tests[i]()):
                    outputList[i] = 1 #1 is correct case
                else: 
                    outputList[i] = 0 #0 is incorrect case
            except Exception as e:
                #catch exception
                print("fail")
                outputList[i] = -1 #-1 means throws error
                print(e)
                
        return outputList

#def fun1():
#    return 5

#def fun2():
#   return giveNum()

#questionTest = question("What's 5?", [5, 5, 5, 5, 5, 5], fun1, fun1, fun1, fun1, fun1, fun2)


#print(questionTest.getResultsWithInput("""def giveNum():
#    return 8"""))

    

def q1_t1():
    return addNums(5, 8)

def q1_t2():
    return addNums(6, 9)

def q1_t3():
    return addNums(-100, 5)

def q1_t4():
    return addNums(100, 35)

def q1_t5():
    return addNums(95, 99)

def q1_t6():
    return addNums(0, 0)

q1 = question("How can we add two numbers?", [13, 15, -95, 135, 194, 0], q1_t1, q1_t2, q1_t3, q1_t4, q1_t5, q1_t6)


#sample_string = """def addNums(num1, num2):
#    return num1 + num2"""

#exec(sample_string, globals())
#print(q1.getResultsWithInput(sample_string))




questionList = {"04/09/2022" : q1}
questionList["04/10/2022"] = q1
        






