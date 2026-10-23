
import ast


class ASTVisualizer(ast.NodeVisitor):
    def __init__(self):
        self.level = 0

    def generic_visit(self, node):
        details = []

        if isinstance(node, ast.Name):
            details.append(f"id={node.id}")

        elif isinstance(node, ast.Constant):
            details.append(f"value={node.value!r}")

        elif isinstance(node, ast.FunctionDef):
            details.append(f"name={node.name}")

        elif isinstance(node, ast.ClassDef):
            details.append(f"name={node.name}")

        elif isinstance(node, ast.arg):
            details.append(f"arg={node.arg}")

        elif isinstance(node, ast.operator):
            details.append(type(node).__name__)

        info = ", ".join(details)
        label = type(node).__name__

        if info:
            label += f" ({info})"

        print("  " * self.level + label)

        self.level += 1
        for child in ast.iter_child_nodes(node):
            self.visit(child)
        self.level -= 1


def visualize_ast(source_code):
    """Parse Python source and display its AST."""
    try:
        tree = ast.parse(source_code)
        print("\nAbstract Syntax Tree")
        print("====================")
        ASTVisualizer().visit(tree)
    except SyntaxError as error:
        print(f"Syntax error: {error}")


if __name__ == "__main__":
    sample_code = """
def add(a, b):
    result = a + b
    return result

print(add(10, 20))
"""

    visualize_ast(sample_code)
