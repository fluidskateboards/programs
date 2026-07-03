dozen: int = 12
found: bool
found = False
def first_two(a: List[float]) -> Tuple[float,float]:
    return (a[0], a[1])
print(first_two([False, 0, 12, 2.2, []]))
