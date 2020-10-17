import pandas as pd
import matplotlib.pyplot as plt
data = pd.read_csv("nba.csv")

def ex1(data) :
    print('ex1')
    plt.hist(data['Age'])
    print()
def ex2(data) :
    print('ex2')
    print(data.loc[int(data['Salary'].idxmax())])
    print()
def ex3(data) :
    print('ex3')
    Salarymean = data['Salary'].groupby(data['Team']).mean()
    index = Salarymean.index
    plt.bar(range(len(index)), Salarymean)
    print()
def ex4(data) :
    print('ex4')
    Collegedata = data['College']
    Collegecount = pd.value_counts(Collegedata)
    print(Collegecount)
    print()
def ex5(data) :
    print('ex5')
    temp1 = data['Age'].mean()
    temp2 = data['Salary'].mean()
    print('Avg Age:',temp1)
    print('Avg Salary:', temp2)
def ex6(data) :
    print('ex6')
    temp = data['Name'].groupby(data['Position'])
    for name, group in temp:
        print(name)
        print(group)
    print()
def main() :
    plt.figure()
    ex1(data)
    ex2(data)
    plt.figure()
    ex3(data)
    ex4(data)
    ex5(data)
    ex6(data)
    plt.show()
main()