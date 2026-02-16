# Machine Learning Assignment 1

## Overview

This repository contains solutions for three machine learning problems focusing on fundamental concepts such as Concept Learning, Decision Trees with Continuous Attributes, and the ID3 Algorithm. The assignment demonstrates theoretical understanding, algorithm implementation, and practical application using Python.

---

## Assignment Objectives

* Understand concept learning for classification tasks.
* Apply entropy and information gain for decision tree construction.
* Implement the ID3 algorithm from scratch.
* Analyze datasets and make predictions.
* Document methodology using GitHub and Wiki.

---

## Question 1 — Concept Learning (Spam Email Classification)

### Problem Statement

Design a simple machine learning system to classify emails as Spam or Not Spam using labeled examples and identify patterns in email features.

### Approach

* Used the Find-S algorithm to learn the most specific hypothesis from positive examples.
* Analyzed features such as promotional words, suspicious links, known sender, and use of capital letters.
* Built a classifier that predicts whether a new email is spam.

### Key Concepts

* Hypothesis space
* Positive and negative examples
* Pattern learning
* Rule-based classification

### Outcome

The system successfully learns rules that distinguish spam emails based on common characteristics.

---

## Question 2 — Decision Tree with Continuous Attributes (Loan Default Prediction)

### Problem Statement

Predict whether a customer will default on a loan using continuous attributes like income and credit score.

### Approach

* Calculated entropy of the dataset.
* Generated possible threshold splits for income.
* Computed information gain for each threshold.
* Selected the best split and constructed a decision rule.

### Key Concepts

* Entropy calculation
* Threshold splitting
* Information gain
* Decision tree construction

### Outcome

The optimal split separates defaulters and non-defaulters effectively, producing an interpretable decision rule.

---

## Question 3 — ID3 Algorithm (Buy Computer Dataset)

### Problem Statement

Build a decision tree using the ID3 algorithm and predict whether a customer will buy a computer based on demographic attributes.

### Approach

* Implemented ID3 from scratch.
* Calculated entropy and information gain for all attributes.
* Recursively built the decision tree.
* Predicted the class for a new example.

### Key Concepts

* Recursive tree building
* Attribute selection
* Entropy reduction
* Classification prediction

### Outcome

The model correctly predicts that the given customer example will buy a computer.

---

## Repository Structure

```
ML-Assignment-1/
│
├── concept_learning_spam_assignment.py
├── loan_default_decision_tree_assignment.py
├── id3_buy_computer_assignment.py
├── README.md
└── Wiki (Documentation)
```

---

## Tools and Technologies

* Python
* Basic data structures
* Mathematical computation (entropy, log functions)
* GitHub for version control
* GitHub Wiki for documentation

---

## Learning Outcomes

Through this assignment, the following skills were developed:

* Understanding of supervised learning concepts
* Ability to implement machine learning algorithms manually
* Interpretation of decision trees
* Analytical thinking for model evaluation
* Documentation and reproducibility practices

---

## Conclusion

This assignment provides hands-on experience with foundational machine learning techniques. By implementing algorithms such as Find-S and ID3 and analyzing decision tree behavior, we gain insights into how models learn patterns from data and make predictions in real-world scenarios.

---


