# Takes in a string from front end and runs it with exec
# Need to account for malicious input 


# Each question has 6 test function parameters as functions
# There will be ONE question for each day.
# correctOutput MUST have length 6 (to match the 6 test functions)
# text is the question/problem text i.e. create a function that returns the ....

class question():
    def __init__(self, text: str, correctOutput: list, fun1, fun2, fun3, fun4, fun5):
        self.text = text
        self.correctOutput = correctOutput
        self.tests = [fun1, fun2, fun3, fun4, fun5]

    def getText(self):
        return self.text

    def getCorrectOutput(self):
            print(self.correctOutput)

    #This function tests the output. It creates a field outputList which will store the results of running each test.
    #def testOutput(self):
    #    self.outputList = [0, 0, 0, 0, 0]
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
    #    outputList = ["", 2, 3, 4 ,5]
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
        outputList = [-2, -2, -2, -2, -2]
        if "import " in inputString:
            print("PLEASE DO NOT ATTEMPT IMPORTS")
            return [3, 3, 3, 3, 3]

        try:
            exec(inputString, globals())
        
        except:
            #catch exception
            print("failure during function definition")
            outputList = [3, 3, 3, 3, 3]        #3's mean failed during function definition
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
    return add_nums(0, 0)

def q1_t2():
    return add_nums(6, 9)

def q1_t3():
    return add_nums(-100, 5)

def q1_t4():
    return add_nums(100, 35)

def q1_t5():
    return add_nums(95, 99)

q1 = question("Sometimes, you just need to add two numbers. Write a function add_nums(num1, num2) that takes two int parameters and returns their sum.",
[0, 15, -95, 135, 194], q1_t1, q1_t2, q1_t3, q1_t4, q1_t5)


#sample_string = """def addNums(num1, num2):
#    return num1 + num2"""

#exec(sample_string, globals())
#print(q1.getResultsWithInput(sample_string))

def q2_t1():
    return generate_lucas_sequence(0)

def q2_t2():
    return generate_lucas_sequence(1)

def q2_t3():
    return generate_lucas_sequence(2)

def q2_t4():
    return generate_lucas_sequence(15)

def q2_t5():
    return generate_lucas_sequence(23)



q2 = question("""The Lucas Number sequence is defined as follows:\nL(n) = 2 for n = 0, L(n) = 1 for n = 1, and L(n) = L(n-1) + L(n-2) for n > 1\n 
Write a function generate_lucas_sequence(param_1) that takes an int parameter to compute the value of L(n) given any n between 0 and 25""",
[2, 1, 3, 1364, 640], q2_t1, q2_t2, q2_t3, q2_t4, q2_t5)


def q3_t1():
    return repeating_substr("abababab")

def q3_t2():
    return repeating_substr("")

def q3_t3():
    return repeating_substr("     ")

def q3_t4():
    return repeating_substr("momdadmomdad")

def q3_t5():
    return repeating_substr("?!_?!_gqinfowmo")


q3 = question("""Write the function repeating_substr(str) that takes a string parameter and returns the longest repeating substring.
For example, the longest substring in the string "abababab" would be "abab". The longest substring in the string "ababa" would be "ab".
An empty string should be returned when there is no repeating substring.""",
["abab", "", "   ", "momdad", "?!_"], q3_t1, q3_t2, q3_t3, q3_t4, q3_t5)
 


def q4_t1():
    return caesar_shift("abc", 1)

def q4_t2():
    return caesar_shift("can this work?", 5)

def q4_t3():
    return caesar_shift(" ?a! ", 26)

def q4_t4():
    return caesar_shift("abc", 1)

def q4_t5():
    return caesar_shift("Welcome to Bitcamp!", 1)


q4 = question("""A Caesar cipher is a way to encrypt text. Caesar ciphers use a substitution method where the letters in the alphabet are shifted by a fixed number
to provide encoding letters. For example, encoding "abc" with a Caesar shift of 1 would yield "bcd." Write a function caesar_shift(str, shift_num) 
that takes a string parameter and encodes it using a Caesar shift with a shift of size shift_num. The encrypted string should be returned. 
Non-alphabetic characters should not be changed, and it can be assumed all text is lowercase. Additionally, all shifts will be positive""",
["bcd", "itjx ymnx btwp?", "abc", " ?a! ", "Qyfwigy ni Vcnwugj!"], q4_t1, q4_t2, q4_t3, q4_t4, q4_t5)


def q5_t1():
    return to_hex(1)

def q5_t2():
    return to_hex(29)

def q5_t3():
    return to_hex(256)

def q5_t4():
    return to_hex(15191)

def q5_t5():
    return to_hex(0)


q5 = question("""Write a function to_hex(num) that converts the parameter num to hexadecimal, and returns a string of the hexadecimal number. Note that num is 
in base 10. Example: converting 31 to hexadecimal would yield "1F".""",
["1", "1D", "100", "3B57", "0"], q5_t1, q5_t2, q5_t3, q5_t4, q5_t5)


questionList = {"04/09/2022" : q1}
questionList["04/10/2022"] = q2
questionList["04/11/2022"] = q3
questionList["04/12/2022"] = q4
questionList["04/13/2022"] = q5


print(questionList["04/13/2022"].getText())
        






