import backend as bk

def q1_t1():
    addNums(5, 8)

def q1_t2():
    addNums(6, 9)

def q1_t3():
    return addNums(-100, 5)

def q1_t4():
    return addNums(100, 35)

def q1_t5():
    return addNums(95, 99)

def q1_t6():
    return addNums(0, 0)

q1 = bk.question("How can we add two numbers?", [13, 15, -95, 135, 194, 0], q1_t1, q1_t2, q1_t3, q1_t4, q1_t5, q1_t6)


inputString = """def addNums(num1, num2):
    return num1 + num2"""

print(q1.getResultsWithInput(inputString))



