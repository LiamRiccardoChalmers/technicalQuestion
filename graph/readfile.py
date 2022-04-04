import pandas as pd
import os

"""
The idea is to have a module library reading and supplying data off of the excel
file in a structured way and also if the neeed to read other file formats came
up then the functions to facilitate that would be stored hear
"""  # Enable auto-doc for data member
def read_xlsx(filename):
    var = pd.read_excel(os.path.dirname(os.path.dirname(__file__)) + "/" + filename)
    income = []
    expense = []
    months = []
    for i in var:
        if var[i][0] != "Income":
            income.append(var[i][0])
            expense.append(var[i][1])
            months.append(i)
    return months,income,expense

if __name__ == '__main__':
    read_xlsx("test.xlsx")
