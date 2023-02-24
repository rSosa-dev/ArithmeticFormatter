import re

def arithmetic_arranger(problems, showAnsw=False):
  arranged_problems = ""
  if len(problems) > 5:
    arranged_problems = "Error: Too many problems"
    return arranged_problems

  # Check if all operators are '+' or '-'.
  operators = []
  operators = list(map(lambda x: x.split()[1], problems)) # The default split value is whitespace (' '). Getting the operator here.
  if set(operators) != {"+", "-"}: # Check if the operators are missed in the list.
    arranged_problems = "Error: Operator must be '+' or '-'." # If so, the error is throwed.
    return arranged_problems
  
  if len(set(operators)) > 5: # By getting the length of the list operators we can get the amount of problems.
    arranged_problems = "Error: Too many problems."
    return arranged_problems

  # Add all operands into a list.
  number = []
  for problem in problems:
    p = problem.split()
    number.extend([p[0], p[2]]) # Add to numbers list the two operands.

  for n in number:
    if str(n).isdigit() == False: # Check if every item in list 'number' is a number.
      arranged_problems = "Error: Numbers must only contain digits."
      return arranged_problems