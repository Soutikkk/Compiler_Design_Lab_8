
import ast

# Simple BNF grammar:
# <statement> ::= <identifier> "=" <expression>
# <expression> ::= <term> (("+" | "-") <term>)*
# <term>       ::= <factor> (("*" | "/") <factor>)*
# <factor>     ::= <number> | <identifier> | "(" <expression> ")"

def convert_to_ast(program):
    try:
        tree = ast.parse(program)
        print("Abstract Syntax Tree (AST):")
        print(ast.dump(tree, indent=4))
    except SyntaxError as e:
        print("Syntax Error:", e)

# Example program
program = "a = 10 + 5 * 2"

convert_to_ast(program)
