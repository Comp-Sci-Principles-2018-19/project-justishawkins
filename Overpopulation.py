# Find the total amount of contraceptive pills you will need yearly based on the growing population
# Birth rate of 131 million
# Mortality rate of 55 million
# Subtract birth rate by the mortality and add it to the given population
import sys

def test(did_pass):
    """  Print the result of a test.  """
    linenum = sys._getframe(1).f_lineno   # Get the caller's line number.
    if did_pass:
        msg = "Test at line {0} ok.".format(linenum)
    else:
        msg = ("Test at line {0} FAILED.".format(linenum))
    print(msg)

def growthrate(cur, pre, y):
    """User enters current population and population from previous year, and number of years in between.
Program returns the amount of contraceptive pills needed yearly."""
    return (cur-pre)/y

def test_suite():
    """ Run the suite of tests for code in this module (this file).
    """
    test(growthrate(1,1,1) == 0)
    test(growthrate(1000,500,10) == 50)
    test(growthrate(50,100,1) == -50)
    test(growthrate(50,50,1) == 0)
    test(growthrate(200,100,1) == 100)
    test(growthrate(300,200,1) == 100)
    test(growthrate(300,200,2) == 50)
    test(growthrate(80,40,2) == 20)
    test(growthrate(100,300,-2) == 100)
    test(growthrate(500,100,-1) == -400)

test_suite()

cur_pop=int(input("What is the current population"))
prev_pop=int(input("What is the previous population"))

years=int(input("How many years"))
print(growthrate(cur_pop, prev_pop, years))

