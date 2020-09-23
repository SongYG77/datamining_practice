import numpy as np
Score = np.random.randint(100, size=(10, 4))
def main() :
    global Score
    func1(Score)
    func2(Score)
    Score2 = func3(Score)
    Score2 = func4(Score2)

def func1(arr1) : #문제 1
    arr2 = np.where((arr1 >= 70), 'C', 'D')
    arr2 = np.where((arr1 >= 80), 'B', arr2)
    arr2 = np.where((arr1 >= 90), 'A', arr2)
    print("\n 문제 1")
    print(arr2)

def func2(arr1) : #문제 2
    arrmean = arr1.mean(0)
    arr2 = arr1- arrmean
    print("\n 문제 2")
    print(arr2)

def func3(arr1) : #문제 3
    arrsum = arr1.sum(1)
    arrsum=arrsum.reshape(10,1)
    arr1 = np.concatenate([arr1,arrsum], axis = 1)
    print("\n 문제 3")
    print(arr1)
    return arr1

def func4(arr1) : #문제 4
    temparr = arr1[:,:-1]
    arravg = temparr.mean(1).reshape(10,1)
    arr1 = np.concatenate([arr1,arravg], axis = 1)
    arravg = temparr.mean(0).reshape(1,4)
    temp = arr1[:,4].sum().reshape(1,1)
    arravg = np.concatenate([arravg,temp],axis = 1).reshape(1,5)
    temp = arr1[:,5].mean().reshape(1,1)
    arravg = np.concatenate([arravg, temp], axis=1)
    arr1 = np.concatenate([arr1, arravg], axis=0)
    print("\n 마지막 결과")
    print(arr1)
    return arr1
main()