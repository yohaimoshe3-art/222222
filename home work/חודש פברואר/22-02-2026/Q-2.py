def a_b(a: int, b: int) -> list:
    if b == 0:
        return []
    return [a + b, a-b, a/b, a*b]
result = a_b(a=4, b=4)
print(result)