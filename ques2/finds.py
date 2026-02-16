import pandas as pd
import math

def entropy(data):
    total = len(data)
    yes = len(data[data["Default"] == "Yes"])
    no = len(data[data["Default"] == "No"])

    def calc(p):
        return -p * math.log2(p) if p > 0 else 0

    return calc(yes/total) + calc(no/total)

def best_income_split(csv_file):
    data = pd.read_csv(csv_file)

    base_entropy = entropy(data)

    incomes = sorted(data["Income"].unique())
    thresholds = [(incomes[i] + incomes[i+1]) / 2 for i in range(len(incomes)-1)]

    best_gain = -1
    best_threshold = None

    for t in thresholds:
        left = data[data["Income"] <= t]
        right = data[data["Income"] > t]

        weighted_entropy = (len(left)/len(data))*entropy(left) + \
                           (len(right)/len(data))*entropy(right)

        gain = base_entropy - weighted_entropy

        if gain > best_gain:
            best_gain = gain
            best_threshold = t

    return best_threshold, best_gain

def predict(income, threshold):
    return "Yes" if income <= threshold else "No"
