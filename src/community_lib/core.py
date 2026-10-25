# math:
def subtract(a: int, b: int):
  sum = a - b
  return sum
def multiply(a: int, b: int):
  product = a * b
  return product 
def divide(a: int, b: int):
  output = a / b
  if b == 0:
    raise ValueError("> denominator cannot be 0")
  return output
def divide_round(a: int, b: int):
  output = a // b
  if b == 0:
    raise ValueError("> denominator cannot be 0")
  return output 
# other:
