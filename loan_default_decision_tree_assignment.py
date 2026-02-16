import math

data = [
    ("C1", 2.5, 580, "Yes"),
    ("C2", 3.0, 600, "Yes"),
    ("C3", 3.5, 650, "No"),
    ("C4", 4.0, 700, "No"),
    ("C5", 4.5, 720, "No"),
    ("C6", 5.0, 750, "No")
]

print("\n===== Handling Continuous Attributes =====")
print("Decision trees handle continuous attributes by testing threshold splits like Income ≤ value.\n")


def entropy(labels):
    total = len(labels)
    counts = {}

    for label in labels:
        counts[label] = counts.get(label, 0) + 1

    ent = 0
    for count in counts.values():
        p = count / total
        ent -= p * math.log2(p)

    return ent

# Compute dataset entropy
labels = [row[3] for row in data]
dataset_entropy = entropy(labels)

print("Dataset Entropy:", round(dataset_entropy, 4))

# -------------------------
# Find Thresholds for Income
# -------------------------
incomes = sorted([row[1] for row in data])
thresholds = [(incomes[i] + incomes[i+1]) / 2 for i in range(len(incomes)-1)]

print("\nPossible Thresholds:", thresholds)


def info_gain(threshold):
    left = [row for row in data if row[1] <= threshold]
    right = [row for row in data if row[1] > threshold]

    left_labels = [row[3] for row in left]
    right_labels = [row[3] for row in right]

    weighted_entropy = (
        len(left)/len(data) * entropy(left_labels) +
        len(right)/len(data) * entropy(right_labels)
    )

    return dataset_entropy - weighted_entropy

best_threshold = None
best_gain = -1

print("\n===== Information Gain for Each Threshold =====")

for t in thresholds:
    gain = info_gain(t)
    print(f"Threshold {t:.2f} -> Gain {gain:.4f}")

    if gain > best_gain:
        best_gain = gain
        best_threshold = t

print("\nBest Threshold:", best_threshold)
print("Best Information Gain:", round(best_gain, 4))

# -------------------------
# Decision Rule
# -------------------------
print("\n===== Decision Tree =====")

print(f"If Income ≤ {best_threshold}: Default = Yes")
print(f"If Income > {best_threshold}: Default = No")
