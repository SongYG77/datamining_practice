import numpy as np
def num1(a): #1번 문제
    t = a[:,2]
    return t
def num2(a) :#2번 문제
    t=0
    for i in a :
        t += sum(i)
    return t
def num3(a) :#3번 문제
    lst = [True, False, False, False, True, False, True, False, True, True]
    t = a[lst]
    return t
def num4(a) :#4번 문제
    t= a.transpose((1,0))
    return t
Score = np.random.randint(100, size=(10,4))
print(Score)
print(num1(Score))
print(num2(Score))
print(num3(Score))
print(num4(Score))