def solve1(a, b, c):
    if a == 0 and b == 0 and c == 0:
        print("Rownanie tozsamosciowe")
    elif a == 0 and b == 0 and c != 0:
        raise ValueError("Rownanie sprzeczne")
    elif (a == 0 and b != 0 and c == 0) or (a != 0 and b == 0 and c == 0):
        print("x = 0 , y = 0")
    else:
        if a == 0 and b != 0:
            y = - c / b
            print("x dowolne , y = " + str(y))
        elif a != 0 and b == 0:
            x = - c / a
            print("x = " + str(x) + ", y dowolne")
        else:
            x = - c / a
            y = c / b
            print("x = " + str(x) + ", y = " + str(y))
