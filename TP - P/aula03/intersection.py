
def intersection(a, b, c, d):
    assert a <= b
    assert c <= d
    if b < c or d < a:
        return None
    else:
        e = max(a, c)
        f = min(b, d)
    return (e, f)

def testIntersection(a, b, c, d, x, y):
    """Call intersection, print result and check against expected result."""
    print(f"intersection({a}, {b}, {c}, {d})", end=" ")
    (e, f) = intersection(a, b, c, d)
    check = "OK" if (e, f) == (x, y) else "FAIL"
    print(f"--> ({e}, {f}) {check}")

def main():
    testIntersection(1, 6, 4, 8,  4, 6)
    testIntersection(1, 6, 3, 5,  3, 5)
    testIntersection(5, 8, 6, 18,  6, 8)

main()

