def generate_intermediate_code(expression):
expression = expression.replace(" ", "")
operators = "+-*/"

stack = []
precedence = {'+': 1, '-': 1, '*': 2, '/': 2}
postfix = []

# Convert infix expression to postfix
for char in expression:
    if char.isalnum():
        postfix.append(char)
    elif char == '(':
        stack.append(char)
    elif char == ')':
        while stack and stack[-1] != '(':
            postfix.append(stack.pop())
        if stack:
            stack.pop()
    elif char in operators:
        while (stack and stack[-1] != '(' and
               precedence[stack[-1]] >= precedence[char]):
            postfix.append(stack.pop())
        stack.append(char)

while stack:
    postfix.append(stack.pop())

# Generate three-address code
stack = []
code = []
temp_count = 1

for token in postfix:
    if token.isalnum():
        stack.append(token)
    elif token in operators:
        if len(stack) < 2:
            raise ValueError("Invalid arithmetic expression")

        right = stack.pop()
        left = stack.pop()
        temp = f"t{temp_count}"

        code.append(f"{temp} = {left} {token} {right}")
        stack.append(temp)
        temp_count += 1

if len(stack) != 1:
    raise ValueError("Invalid arithmetic expression")

code.append(f"Result = {stack[0]}")
return code

if name == "main":
expression = input("Enter an arithmetic expression: ")

try:
    intermediate_code = generate_intermediate_code(expression)
    print("\nThree-Address Intermediate Code:")
    for instruction in intermediate_code:
        print(instruction)
except (ValueError, IndexError):
    print("Error: Invalid arithmetic expression.")
