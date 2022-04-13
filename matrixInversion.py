# System Of Linear Equation (Martix Inversion)
import numpy as np
from numpy.linalg import inv, qr
def creatArray():
    print("===== Enter the Entries in a single line seperated by space ====="\n)
    
    R = int(input("Enter the number of rows: "))
    C = int(input("Enter the number of columns: "))
    
    print("===== Now Enter the values =====")

    entries = list(map(int, input().split()))

    matrix = np.array(entries).reshape(R, C)
    return matrix

def creatAnullArray():
    print("=========================================")
    u = int(input("Enter the number of unknown variables: "))
    a = [i for i in range(u)]
    b = []
    for c in a:
        i = 0
        if(i <= 2):
            i = i + 1
            tut = 'x{0}'.format(c)
            b.append(tut)
    m = np.array(b).reshape(u,1)
    return m


def solve():
    print("========================================\n Enter the Matrix 'A': \n")
    A = creatArray()
    print("========================================\n Enter the Matrix 'B': \n")
    B = creatArray()
    #np.array((['x1'],['x2'],['x3']), dtype = str)
    X = creatAnullArray()
    Q = inv(A)
    M = np.dot(Q,B)
    tut = []
    count = -1
    for u in X:
        count = count + 1
        ret = count + 1
        tier = 'x{0}: {1}'.format(ret, M[count])
        tut.append(tier)
        result = np.array((tut), dtype = str)
        
    return result
    
solve()
