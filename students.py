lloyd = {
  "name": "Lloyd",
  "homework": [90.0, 97.0, 75.0, 92.0],
  "quizzes": [88.0, 40.0, 94.0],
  "tests": [75.0, 90.0]
}
alice = {
  "name": "Alice",
  "homework": [100.0, 92.0, 98.0, 100.0],
  "quizzes": [82.0, 83.0, 91.0],
  "tests": [89.0, 97.0]
}
tyler = {
  "name": "Tyler",
  "homework": [0.0, 87.0, 75.0, 22.0],
  "quizzes": [0.0, 75.0, 78.0],
  "tests": [100.0, 100.0]
}

"""Define a function called average that has one argument, numbers.
Inside that function, call the built-in sum() function with the numbers list as a parameter. Store the result in a variable called total.
 use float() to convert total and store the result in total.
Divide total by the length of the numbers list. Use the built-in len()"""

def average(numbers):
  total = sum(numbers)
  total = float(total)
  return total / len(numbers)