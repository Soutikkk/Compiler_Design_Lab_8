
import ast


def generate_ast_and_assembly(program):
    try:
        # Step 1: Parse the source program
        tree = ast.parse(program)

        # Step 2: Display the Abstract Syntax Tree
        print("=" * 50)
        print("ABSTRACT SYNTAX TREE (AST)")
        print("=" * 50)
        print(ast.dump(tree, indent=4))

        # Step 3: Generate assembly-like instructions
        print("\n" + "=" * 50)
        print("ASSEMBLY OUTPUT")
        print("=" * 50)

        for statement in tree.body:
            if isinstance(statement, ast.Assign):
                target = statement.targets[0]

                if isinstance(target, ast.Name):
                    print(f"; Assignment to {target.id}")
                    generate_expression(statement.value)
                    print(f"STORE {target.id}")

                else:
                    print("Unsupported assignment target")

            else:
                print("Unsupported statement")


    except SyntaxError as e:
        print("Syntax Error:", e)


def generate_expression(node):
    # Handle numeric constants
    if isinstance(node, ast.Constant):
        if isinstance(node.value, (int, float)):
            print(f"PUSH {node.value}")
        else:
            raise ValueError("Unsupported constant")

    # Handle variable names
    elif isinstance(node, ast.Name):
        print(f"LOAD {node.id}")

    # Handle arithmetic operations
    elif isinstance(node, ast.BinOp):
        generate_expression(node.left)
        generate_expression(node.right)

        operators = {
            ast.Add: "ADD",
            ast.Sub: "SUB",
            ast.Mult: "MUL",
            ast.Div: "DIV"
        }

        operator = operators.get(type(node.op))

        if operator is None:
            raise ValueError("Unsupported operator")

        print(operator)

    else:
        raise ValueError("Unsupported expression")


# Example source program
source_code = "a = 10 + 5 * 2"

generate_ast_and_assembly(source_code)
