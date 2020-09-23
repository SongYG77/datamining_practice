import random
def main() :# 메인
    ex1()
    ex2()
def ex1() :#문제 1
    lst1 = [random.randint(1,100) for i in range(20)]
    lst2 = [random.randint(1,100) for i in range(20)]
    lst1.extend(lst2)
    a= set(lst1)
    print(a)
def ex2() : #문제 2
    data = [
        ['A', 'B', 'A', 'C', 'C', 'D', 'E', 'E', 'A', 'D'],
        ['D', 'B', 'A', 'B', 'C', 'A', 'E', 'E', 'A', 'D'],
        ['E', 'D', 'D', 'A', 'C', 'B', 'E', 'E', 'A', 'D'],
        ['C', 'B', 'A', 'E', 'D', 'C', 'E', 'E', 'A', 'D'],
        ['A', 'B', 'D', 'C', 'C', 'D', 'E', 'E', 'A', 'D'],
        ['B', 'B', 'E', 'C', 'C', 'D', 'E', 'E', 'A', 'D'],
        ['B', 'B', 'A', 'C', 'C', 'D', 'E', 'E', 'A', 'D'],
        ['E', 'B', 'E', 'C', 'C', 'D', 'E', 'E', 'A', 'D']
    ]
    ctr = 0
    sum = 0
    answer = ['D', 'B', 'D', 'C', 'C', 'D', 'A', 'E', 'A', 'D']
    for i in range(len(data)) :
        for j in range(len(data[i])) :
            if data[i][j] == answer[j] : sum +=1
        print(i,"번 학생의 정답 문항의 개수는",sum,"입니다.")
        sum = 0
main()#메인 호출
