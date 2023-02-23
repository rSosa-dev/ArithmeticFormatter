import re

def arithmetic_arranger(problems, showAnsw=False):
  arranged_problems = ""
  if len(problems) > 5:
    arranged_problems = "Error: Too many problems"
    return arranged_problems

  # Check if all operators are '+' or '-'.
  for problem in problems:
    if not(problem.__contains__("+" or "-")):
      arranged_problems = "Error: Operator must be '+' or '-'."
      return arranged_problems


  # Add all operands into a list.
  number = []
  for problem in problems:
    p = problem.split() # The default split value is whitespace (' ').
    number.extend(p)
