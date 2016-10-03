def multiply(x, y):
    len_x = len(str(x))
    len_y = len(str(y))
    # print len_x, len_y

    n = max(len_x, len_y)

    if n == 1:
        return x * y

    n = (n / 2) + (n % 2)
    multiplier = 10 ** n

    b = x / multiplier
    a = x - (b * multiplier)
    d = y / multiplier
    c = y - (d * multiplier)

    z0 = multiply(a, c)
    z1 = multiply(a + b, c + d)
    z2 = multiply(b, d)

    return z0 + ((z1 - z0 - z2) * multiplier) + (z2 * (10 ** (2 * n)))


print multiply(1234, 5678)
