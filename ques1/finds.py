import pandas as pd

def train_finds(csv_file):
    data = pd.read_csv(csv_file)

    # Remove Email column
    data = data.drop(columns=["Email"])

    attributes = data.columns[:-1]
    target = data.columns[-1]

    hypothesis = ['Ø'] * len(attributes)

    for _, row in data.iterrows():
        if row[target] == "Spam":
            for i, attr in enumerate(attributes):
                if hypothesis[i] == 'Ø':
                    hypothesis[i] = row[attr]
                elif hypothesis[i] != row[attr]:
                    hypothesis[i] = '?'

    return hypothesis, list(attributes)


def predict(hypothesis, attributes, input_data):
    for i in range(len(hypothesis)):
        if hypothesis[i] == '?':
            continue
        if hypothesis[i] != input_data[i]:
            return "Not Spam"
    return "Spam"
