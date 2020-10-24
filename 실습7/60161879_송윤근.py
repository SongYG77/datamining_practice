import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

def top(df, n=5, column='tip_pct'):
    return df.sort_values(by=column)[-n:]
def ex1(data):
    ptData = data.pivot_table(['Age', 'Salary'], index=['Position', 'Team'])
    print(ptData)
def ex2(data):
    MAX_SALARY = lambda a: a.max()
    maxsalary_group = data.groupby(['Position'])
    answer_data = maxsalary_group['Salary'].agg(MAX_SALARY)
    plt.figure(1)
    plt.bar(answer_data.index,answer_data)
    plt.xticks(answer_data.index, ['C', 'PF', 'PG', 'SF', 'SG'])
    plt.show()
def ex3(data):
    ch = lambda x : ''.join([i[0] for i in x.split()])
    MAX_SALARY = lambda a: a.max()
    teams_age = []
    teams_salary = []
    team_max_age = data.groupby(['Team']).apply(top, n=1, column = 'Age')['Age']
    temp = team_max_age.index
    for i in temp :
        teams_age.append(ch(i[0]))
    tt = data.groupby(['Team'])
    team_max_salary = tt['Salary'].agg(MAX_SALARY)
    temp = team_max_salary.index
    for i in temp:
        teams_salary.append(ch(i))
    plt.figure(figsize=(10, 7))
    plt.subplot(2,1,2)
    plt.bar(teams_age,team_max_age)
    plt.xticks(teams_age,teams_age)
    plt.subplot(2, 1, 1)
    plt.bar(teams_salary, team_max_salary)
    plt.xticks(teams_salary, teams_salary)
    plt.show()
def main() :
    data = pd.read_csv('nba.csv')
    ex1(data)
    ex2(data)
    ex3(data)
main()
