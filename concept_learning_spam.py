

dataset = [
    ["Yes", "Yes", "No", "Yes", "Spam"],       
    ["Yes", "No",  "No", "Yes", "Spam"],       
    ["No",  "No",  "Yes", "No",  "Not Spam"],  
    ["No",  "Yes", "Yes", "No",  "Not Spam"]   
]

attributes = ["Promotional Words", "Suspicious Links", "Known Sender", "All Caps"]


positive_examples = [row[:-1] for row in dataset if row[-1] == "Spam"]


hypothesis = positive_examples[0].copy()


for example in positive_examples[1:]:
    for i in range(len(hypothesis)):
        if hypothesis[i] != example[i]:
            hypothesis[i] = "?"

print("\n===== Learned Hypothesis =====")
for attr, val in zip(attributes, hypothesis):
    print(f"{attr}: {val}")


def classify(email):
    for i in range(len(hypothesis)):
        if hypothesis[i] != "?" and hypothesis[i] != email[i]:
            return "Not Spam"
    return "Spam"


correct = 0

print("\n===== Predictions on Dataset =====")

for row in dataset:
    features = row[:-1]
    actual = row[-1]
    prediction = classify(features)

    print(f"Email {features} -> Predicted: {prediction} | Actual: {actual}")

    if prediction == actual:
        correct += 1

accuracy = correct / len(dataset) * 100
print(f"\nModel Accuracy: {accuracy:.2f}%")


print("\n===== Test New Email =====")

test_email = []

for attr in attributes:
    value = input(f"Enter {attr} (Yes/No): ")
    test_email.append(value)

result = classify(test_email)

print("\nPrediction for new email:", result)
