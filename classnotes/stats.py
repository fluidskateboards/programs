import sys

def median(a):
    """Return the median of sequence a"""
    a = sorted(a)
    length = len(a)
    if length % 2 == 1:
        return a[length // 2]
    else:
        return (a[length // 2] + a[length // 2 - 1]) / 2

def mean(a):
    """Return the mean of the values in sequence a"""
    return sum(a)/len(a)
print("input array is:", sys.argv)
numbers = [int(x) for x in sys.argv[1:]]
print(mean.__doc__)
print("mean is:", mean(numbers))
print(median.__doc__)
print("median is:", median(numbers))
