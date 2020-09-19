# Collatz Conjecture - Start with a number n > 1. 
# Find the number of steps it takes to reach one 
# using the following process: If n is even, divide 
# it by 2. If n is odd, multiply it by 3 and add 1.
import matplotlib.pyplot as plt

def evenOrOdd(n):
    n = n / 2
    if n.is_integer() == False:
        nValue = 1
        return nValue
    else:
        nValue = 2
        return nValue

def graph(x, y):

    plt.plot(x, y)

    plt.xlabel("Number of Steps")
    plt.ylabel("Number Value")

    plt.title("Collatz Conjecture")

    plt.show()


def run():

    running = True
    startup = True

    step = 0

    stepList = []
    nList = []

    while startup:

        n = input("Enter a number greater than 1: ")
        n = int(n)

        if n == 1:
            print("Please input a number greater than 1.")
            print("Try again.")
        else:
            startup = False
        
    while running:
        
        if n == 1:
            running = False
            break

        nValue = evenOrOdd(n)
        
        if n == 1:
            running = False
            break
        elif nValue == 2:
            n = n /2
            print(int(n))
        elif nValue == 1:
            n = n * 3
            n += 1
            print(int(n))
        
        step += 1

        stepList.append(step)
        nList.append(n)

    print("It took " + str(step) + " steps to get to 1")

    graph(stepList, nList)
        
run()