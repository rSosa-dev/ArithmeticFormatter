
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
  # Handle max four digits per operands problem.
  numbers = []
  for problem in problems:
    p = problem.split()
    if len(p[0]) > 4 or len(p[2]) > 4: # If one of the operands have more than 4 digits, the error is thrown.
      arranged_problems = "Error: Numbers cannot be more than four digits."
      return arranged_problems
    else:
      numbers.extend([p[0], p[2]]) # Add to numbers list the two operands.

  for n in numbers:
    if str(n).isdigit() == False: # Check if every item in list 'number' is a number.
      arranged_problems = "Error: Numbers must only contain digits."
      return arranged_problems

  topRow = ''
  dashes = ''
  values = list(map(lambda x: eval(x), problems)) # Get all the numbers of the problems list.
  solutions = ''
  for i in range(0, len(numbers), 2): # Step by 2 into the list.
      operationWidth = max(len(numbers[i]), len(numbers[i+1])) + 2 # We get the max length between the two operands, and we add two more lines counting the operator and the space.
      topRow += numbers[i].rjust(operationWidth) # The function rjust() aligns the text to the right.
      dashes += '-' * operationWidth # We 
      solutions += str(values[i // 2]).rjust(operationWidth) # Calculate the results of the operations.
      if i != len(numbers) - 2:
          topRow += ' ' * 4
          dashes += ' ' * 4
          solutions += ' ' * 4

  bottomRow = '' # Same procedure as above.
  for i in range(1, len(numbers), 2):
      operationWidth = max(len(numbers[i - 1]), len(numbers[i])) + 1
      bottomRow += operators[i // 2]
      bottomRow += numbers[i].rjust(operationWidth)
      if i != len(numbers) - 1:
          bottomRow += ' ' * 4

  if showAnsw == True:
      arranged_problems = '\n'.join((topRow, bottomRow, dashes, solutions)) # If showAnsw (bool) parameter is true, the answers will be shown.
  else:
      arranged_problems = '\n'.join((topRow, bottomRow, dashes)) # If not, the answers will be hiden.
  return arranged_problems



    