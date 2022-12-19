# Rolling dice program that simulates rolling a dice 1000 times

import random,time
from tabulate import tabulate

# Variables to store the counters
first = 0
second = 0
third = 0
fourth = 0
fifth = 0
sixth = 0

def throwDice(): # Dice rolling to generate numbers

    # For loop to generate numbers between 0 and 1 for 1000 times
    for i in range(1000):
        check(random.random())

def check(num): # Function to check where random number lies

    global first,second,third,fourth,fifth,sixth,total

    if num >= float(0/6) and num < float(1/6):
        first += 1
    elif num >= float(1/6) and num < float(2/6):
        second += 1
    elif num >= float(2/6) and num < float(3/6):
        third += 1
    elif num >= float(3/6) and num < float(4/6):
        fourth += 1
    elif num >= float(4/6) and num < float(5/6):
        fifth +=1
    elif num >= float(5/6) and num < float(6/6):
        sixth +=1
    else:
        pass

    # Sum all numbers to get total
    total = first + second + third + fourth + fifth + sixth
    

def display(): # Function to display results

    global first,second,third,fourth,fifth,sixth,total
    
    # 2-d array to store number outputted, number of times the specific number has appeared 
    # and its percentage appearing
    data = [[1, first, (first / total * 100)],
            [2, second, (second / total * 100)],
            [3, third, (third / total * 100)],
            [4, fourth, (fourth / total * 100)],
            [5, fifth, (fifth / total * 100)],
            [6, sixth, (sixth / total * 100)],
            ['Total',total, (total / total * 100)]
            ]
    print (tabulate(data, headers=["Number", "Occurence", "Percentage"]))

# Main function
if __name__ == "__main__":
    begin = time.time() # Track execution time of program
    throwDice()
    display()
    end = time.time()   # Track execution time of program
    print(f"\n\nTotal runtime of the program is {round((end - begin),2)} seconds")