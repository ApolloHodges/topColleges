''' By Laura Finkelstein and Apollo Hodges'''


import numpy as np
import matplotlib.pyplot as plt


def getValues(f):
    ''' Decorator to print the return values'''
    def inner(*args, **kwargs):
        rv = f(*args, **kwargs)
        print(rv)
        return rv
    return inner


class Colleges:
    ''' Class for all the top college attributes and graphing methods '''
    def __init__(self):
        self._data = dict()
        scores = np.loadtxt("scores.csv", dtype=int, delimiter=",")
        self._colInfo = np.loadtxt("Colleges.csv", dtype=str, delimiter=",")

        with open('header.csv') as hd:
            self._headers = hd.readline().strip().split(",")

        for i in range(len(scores[0])):
            self._data[self._headers[i]] = scores[:, i]

        self._costStd = round(np.std(self._data['Total Annual Cost'][(self._data['Total Annual Cost'] > 0)]))
        self._costMean = round(np.mean(self._data['Total Annual Cost'][(self._data['Total Annual Cost'] > 0)]))
        self._SATStd = round(np.std(self._data['SAT Lower'][(self._data['SAT Lower'] >= 0)]))
        self._SATMean = round(np.mean(self._data['SAT Lower'][(self._data['SAT Lower'] >= 0)]))
        self._ACTStd = round(np.std(self._data['ACT Lower'][(self._data['ACT Lower'] >= 0)]))
        self._ACTMean = round(np.mean(self._data['ACT Lower'][(self._data['ACT Lower'] >= 0)]))
        args = np.argsort(self._data["Alumni Salary"])[::-1]
        self._salArgs = args[self._data["Alumni Salary"][args] >= 0]

    def getCost(self):
        # cost_str = "Mean Total Cost: " + str(self._costMean) + ", standard deviation: " + str(self._costStd)
        return [self._costMean, self._costStd]

    def getSAT(self):

        # sat_str = "Mean SAT Lower: " + str(self._SATMean) + ", standard deviation: " + str(self._SATStd)
        return [self._SATMean, self._SATStd]

    def getACT(self):
        act_lower = "Mean ACT Lower: " + str(self._ACTMean) + ", standard deviation: " + str(self._ACTStd)
        return [self._ACTMean, self._ACTStd]

    def getHeader(self):
        return self._headers

    @getValues
    def costDist(self):
        ''' Plot distribution of total annual cost of schools '''
        plt.hist((self._data["Total Annual Cost"]))
        plt.title("College Cost Distribution")
        plt.xlabel("Costs")
        plt.ylabel("Number of Schools")
        return [np.max(self._data["Total Annual Cost"]), np.min(self._data["Total Annual Cost"])]

    @getValues
    def bestSal(self, num):
        ''' Top salaries by school name'''
        nameList = [self._colInfo[self._salArgs[k], 1] for k in range(num, -1, -1)]
        salaryList = [self._data["Alumni Salary"][self._salArgs[m]] for m in range(num, -1, -1)]
        plt.bar(nameList, salaryList, align="center")
        plt.xticks(rotation=90, fontsize=8)
        plt.yticks(fontsize=8)
        plt.xlabel("College")
        plt.ylabel("Salary (dollars")
        plt.title("Top %d schools by salary" % num)
        plt.ylim(60000, 170000)
        plt.tight_layout()
        return [self._data["Alumni Salary"][self._salArgs[0]], self._data["Alumni Salary"][self._salArgs[-1]]]

    @getValues
    def rankComp(self, cat):
        ''' Graph of attributes vs. rank'''
        catIndex = self._data[cat] >= 0
        catList = self._data[cat][catIndex]
        rankList = self._data["Rank"][catIndex]
        plt.plot(rankList, catList)
        plt.title(f"{cat} by School Rank")
        plt.xlabel("Rank")
        plt.ylabel(cat)
        plt.tight_layout()
        return [np.max(catList), np.min(catList)]

