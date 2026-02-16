data = [
    ["Yes", "Yes", "No", "Yes", "Spam"],       
    ["Yes", "No",  "No", "Yes", "Spam"],       
    ["No",  "No",  "Yes", "No",  "Not Spam"],  
    ["No",  "Yes", "Yes", "No",  "Not Spam"]   
]

positive_examples = [row[:-1] for row in data if row[-1] == "Spam"]

hypothesis = positive_examples[0].copy()

for example in positive_examples[1:]:
    for i in range(len(hypothesis)):
        if hypothesis[i] != example[i]:
            hypothesis[i] = "?"

print("Learned Hypothesis:")
print(hypothesis)

def classify(email, hypothesis):
    for i in range(len(hypothesis)):
        if hypothesis[i] != "?" and hypothesis[i] != email[i]:
            return "Not Spam"
    return "Spam"

print("\nTesting on dataset:")

for row in data:
    email_features = row[:-1]
    prediction = classify(email_features, hypothesis)
    print(email_features, "-> Predicted:", prediction, "| Actual:", row[-1])
