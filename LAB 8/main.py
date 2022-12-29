import numpy as np


def task_b():
    s = ["0A", "0B"]
    t = ["01", "10"]
    l = []

    def task_b_1():
        temp = ""
        for i in range(len(s)):
            for j in range(len(s[i])):
                if s[i][j] == "S":
                    print("Recursive grammar")
                    while len(l) < 3:
                        temp = temp + s[i].replace('S', t[i])
                        l.append(temp)
                elif s[i][j] == "A":
                    temp = s[i].replace('A', t[i])
                    l.append(temp)
                elif s[i][j] == "B":
                    temp = s[i].replace('B', t[i])
                    l.append(temp)
        print(l)

    def task_b_2():
        for i in range(len(t)):
            for j in range(len(t[i])):
                if t[i][j] != "A" and t[i][j] != "B":
                    print("Context-dependent grammar")
                    break
                elif t[i][j] == "A" or t[i][j] == "B" or t[i] == "0A" or t[i] == "0B" or t[i] == "1A" or t[i] == "1B" or t[i] == "A0" or t[i] == "B0" or t[i] == "A1" or t[i] == "B1":
                    print("Regular grammar")
                    break
                else:
                    print("Context free grammar")
                    break

    def task_b_3():
        tablArr = [["S0", "S1"], ["S2", "S2"]]
        print("          f")
        print("Стан    Вхід")
        print("       01  10")
        for i in range(0, len(tablArr)):
            print("S{}".format(i), end="     ")
            for j in tablArr[i]:
                print(j, end="  ")
            print()
    task_b_1()
    task_b_2()
    task_b_3()


def task_c(arr):
    print("c. L(G)={ 0^n 2^3m, n, m = 0, 1, 2}")
    array_helping = []
    array_hel = [[], [], []]
    array_param_g = [["S"], [], ["P", "S"]]
    array_l = [[], [], []]
    param = ""

    # remove spaces
    arr = arr.replace(" ", "")

    # array_helping
    for _ in range(0, len(arr)):
        if arr[_] == "," or arr[_] == "=":
            array_helping.append(param)
            param = ""
            continue
        param += arr[_]

    array_helping[0] = array_helping[0].replace("^", "")
    array_helping[0] = array_helping[0].replace("+", "")

    for _ in range(0, len(array_helping[0])):
        array_param_g[0] += array_helping[0][_]

    text = array_helping[0]

    array_helping[0] = array_helping[0].replace("n", "")
    array_helping[0] = array_helping[0].replace("m", "")

    for _ in range(0, len(array_helping[0])):
        array_param_g[1] += array_helping[0][_]

    print("G =", array_param_g)

    for _ in range(1, len(arr)):
        param = arr[_-1]
        if arr[_] == "^":
            array_hel[0].append(param)
        param = arr[_+1]
        if arr[_] == "=":
            array_hel[1].append(param)
            break

    param = ""
    const = int(array_hel[1][0])

    for _ in range(0, 3):
        text_n = text
        for i in range(0, const):
            param += array_hel[1][0]

        text_n = text_n.replace("m", 3 * param)
        text_n = text_n.replace("n", "")
        array_l[_].append(text_n)

        param = ""
        const += 1
    print("P = [S->0A, A->01, S->0B, B ->10]")
    print("Мова:", array_l)


def task_d():
    f = [0, 1]
    stan = ["S0", "S1", "S2", "S3", "S4", "S5"]

    def dsa(s):
        res = []
        k = 0
        for i in stan:
            res.append(i)
            res.append(s[0])
            if k == len(stan) - 1:
                res.append("-")
            else:
                res.append(s[k + 1])
            k += 1
        res = np.array(res).reshape(len(s), 3)
        return res

    print(dsa(stan))


def task_e():
    def table():
        print("    inpt  S0 S2 S1")
        for i in range(16):
            binary = bin(i)[2:]
            if len(binary) < 4:
                binary = '0' * (4 - len(binary)) + binary
            if i < 10:
                print(str(i) + ")  " + binary, end="")
            else:
                print(str(i) + ") " + binary, end="")
            checkLine(binary)

    def grammar():
        print("\nТаблиця станів")
        table()

        print("\nТаблиця переходів")
        print(" δ  0  1")
        print("S0" + " S0 S1")
        print("S1" + " S1 S2")
        print("S2" + " S2 S2")

        print("\nQ (Стани автомата): " + "{S0, S1, S2}")
        print("Σ (алфавіт): " + "{0, 1}")
        print("q0 (Початковий стан): " + "{S0}")
        print("F (Кінцеві стани): " + "{S1, S2}")
        print("Мова породжена автоматом: " + "L(G) = {0^n10^n,0^n10^n1b |n = 0, 1, 2,...; b — довільний ланцюжок}.")

    def checkLine(expression):
        S0(expression, 0)

    def S0(expression, recursionNumber):
        if expression:
            if recursionNumber == 0:
                print("  0", end="")
            if expression[0] == '0':
                expression = expression[1:]
                S0(expression, recursionNumber + 1)
            elif expression[0] == '1':
                S3(expression, 0)
        else:
            print()

    def S1(expression, recursionNumber):
        if expression:
            if recursionNumber == 0:
                print("  " + expression[0], end="")
            expression = expression[1:]
            S1(expression, recursionNumber + 1)
        else:
            print()

    def S2(expression, recursionNumber):
        if recursionNumber == 0:
            print("  " + expression[0], end="")
        expression = expression[1:]
        if expression:
            if expression[0] == '1':
                S2(expression, recursionNumber + 1)
            elif expression[0] == '0':
                S1(expression, 0)
        else:
            print()

    def S3(expression, recursionNumber):
        if recursionNumber == 0:
            print("  " + expression[0], end="")
        expression = expression[1:]
        if expression:
            if expression[0] == '1':
                S3(expression, recursionNumber + 1)
            elif expression[0] == '0':
                S2(expression, 0)
        else:
            print()
    grammar()


task_b()
print()
task_c(" 0^n 2^3m, n, m = 0, 1, 2,  ")
print()
task_d()
print()
task_e()
