def to_roman(n):
    """Returns a string representing the roman numeral for n"""

    if n <= 0 or n >= 4000:
        raise ValueError(f'{n} is too big or has no Roman equivalent')

    map = [(1000, 'M'), (900, 'CM'), (500, 'D'), (400, 'CD'), (100, 'C'), (90, 'XC'),
        (50, 'L'), (40, 'XL'), (10, 'X'), (9, 'IX'), (5, 'V'), (4, 'IV'), (1, 'I')]
    
    result = []
    for value, name in map:
        while (value <= n):
            result.append(name)
            n -= value
    return ''.join(result)

if __name__ == "__main__":
    n = int(input('Enter an integer: '))
    print(f'{n} is {to_roman(n)}')
    print('And here are other interesting roman numerals')
    for n in [3, 89, 22, 11]:
        print(f'{n} is {to_roman(n)}')