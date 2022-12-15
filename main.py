import numpy as np

mas = np.array([0, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0, 0, 0, 0, 1])
mas = mas.reshape(5, 5)
arif = "3*3 + 4 / 2 × (3 − 5)"


def task1():
    s = 0
    for i in range(5):
        for j in range(5):
            if mas[i][j] == mas[j][i] and i != j:
                s += s
    if s == 20:
        print("Graph is non-orientd")
    else:
        print("Graph can be as oriented and non-oriented")

def preorder_traversal():
    print("Preorder traversal:")
    print("+*33:4*2-35")
    a = "+*33:4*2-35"
    i = len(a)
    A = list()
    k = 0
    print("Step by step")
    while i >= 0:
        i = i - 1
        A.insert(0, a[i])
        k += 1
        print(k, ')', A)
        if a[i] == '-':
            e = int(float(a[i + 1])) - int(float(a[i + 2]))
            del (A[0])
            del (A[0])
            del (A[0])
            A.insert(0, e)
        if a[i] == '*':
            e = int(float(a[i + 1])) * int(float(A[2]))
            del (A[0])
            del (A[0])
            del (A[0])
            A.insert(0, e)
        if a[i] == ':':
            e = int(int(float(A[1])) / int(float(A[2])))
            del (A[0])
            del (A[0])
            del (A[0])
            A.insert(0, e)
        if a[i] == '+':
            e = int(int(float(A[1])) + int(float(A[2])))
            del (A[0])
            del (A[0])
            del (A[0])
            A.insert(0, e)
            print(k, ')', A)
            break


def postorder_traversal():
    print("Postorder traversal:")
    print("3 3 * 4 2 3 5 - * : +")
    print("Step by step")
    a = list("33*4235-*:+")
    A = list()
    k = 0
    for i in range(len(a)):
        k += 1
        A.insert(0, a[i])
        print(k, ')', A)
        if a[i] == "*":
            k += 1
            e = int(float(A[2])) * int(float(A[1]))
            del (A[1])
            del (A[1])
            del (A[0])
            A.insert(0, e)
            print(k, ')', A)
        if a[i] == "-":
            k += 1
            e = int(float(A[2])) - int(float(A[1]))
            del (A[1])
            del (A[1])
            del (A[0])
            A.insert(0, e)
            print(k, ')', A)
        if a[i] == ":":
            k += 1
            e = int(int(float(A[2])) / int(float(A[1])))
            del (A[1])
            del (A[1])
            del (A[0])
            A.insert(0, e)
            print(k, ')', A)
        if a[i] == "+":
            k += 1
            e = int(float(A[2])) + int(float(A[1]))
            del (A[1])
            del (A[1])
            del (A[0])
            A.insert(0, e)
            print(k, ')', A)


task1()
preorder_traversal()
postorder_traversal()
