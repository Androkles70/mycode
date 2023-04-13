#!/usr/bin/env python
"""Alexandra Howarter | What Jedi Class Are You?"""

# Jedi Quiz

# Question 1
print("Question 1: What is your preferred method of solving conflicts?")
print("a) Through negotiation and diplomacy.")
print("b) By analyzing situations and making calculated decisions.")
print("c) By confronting and facing challenges head-on.")

answer1 = input("Enter your choice (a/b/c): ")

# Question 2
print("\nQuestion 2: How do you approach difficult tasks?")
print("a) With patience and careful planning.")
print("b) With a balance of caution and boldness.")
print("c) With determination and strength.")

answer2 = input("Enter your choice (a/b/c): ")

# Question 3
print("\nQuestion 3: What is your primary focus in a mission?")
print("a) Understanding the needs and emotions of others.")
print("b) Protecting and preserving the balance of the Force.")
print("c) Achieving the mission's objective at all costs.")

answer3 = input("Enter your choice (a/b/c): ")

# Calculate result
score = {'a': 0, 'b': 0, 'c': 0}
score[answer1] += 1
score[answer2] += 1
score[answer3] += 1

# Determine Jedi class
if score['a'] > score['b'] and score['a'] > score['c']:
    jedi_class = "Jedi Counselor"
elif score['b'] > score['a'] and score['b'] > score['c']:
    jedi_class = "Jedi Sentinel"
else:
    jedi_class = "Jedi Guardian"

# Print result
print("\nYou are a", jedi_class)
