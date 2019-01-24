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

test_suite()

cur_pop=input("What is the current population")
prev_pop=input(growthrate)

test(growthrate(1,1,1) == 0)
test(input(100,50,5) == 10)
