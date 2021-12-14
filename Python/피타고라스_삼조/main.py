for a in range(1, 400):
    for b in range(1, 400):
        for c in range(1, 400):
            if a * a +  b * b == c * c and a < b < c and a + b + c == 400:
                print(a * b * c)