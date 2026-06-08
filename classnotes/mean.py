import sys
import operator

def mean(a):
    """Return the mean of the values in sequence a"""
    return sum(a)/len(a)
print("input array is:", sys.argv)
numbers = [int(x) for x in sys.argv[1:]]
print("mean is:", mean(numbers))
print(mean.__doc__)