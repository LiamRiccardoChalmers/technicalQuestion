import numpy as np
import matplotlib.pyplot as plt
from io import StringIO

"""
Graph class to render the graph the idea of it being a class was so it could be
extend to other types of graphs and charts
"""
class graphs:

    def __init__(self, months, income, expenses):
        self.months = months
        self.income = income
        self.expenses = expenses


    def make(self):
        X_axis = np.arange(len(self.months))
        fig = plt.figure()
        plt.bar(X_axis - 0.2 ,self.income, 0.4, label="income")
        plt.bar(X_axis + 0.2 ,self.expenses, 0.4, label="expenses")

        plt.xticks(X_axis, self.months)
        plt.xlabel("Months")
        plt.ylabel("Rand")
        plt.title("Finances")
        plt.legend()
        imgdata = StringIO()
        fig.savefig(imgdata, format='svg')
        data = imgdata.getvalue()
        return data
