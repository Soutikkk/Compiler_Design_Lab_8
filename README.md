# Abstract Syntax Tree (AST) Generator in Python

## 📌 Overview

This project demonstrates how to generate and display an **Abstract Syntax Tree (AST)** from a Python program using the built-in `ast` module.

An AST represents the syntactic structure of source code in a tree format. It is commonly used in compiler design, interpreters, static code analysis, and programming language processing.

## 🎯 Objectives

- Understand the concept of an Abstract Syntax Tree.
- Explore Python's built-in `ast` module.
- Parse a Python statement into an AST.
- Display the AST in a readable, indented format.
- Detect and handle syntax errors in the input program.

## 🛠️ Technologies Used

- **Programming Language:** Python
- **Module:** `ast` (Python Standard Library)

No external libraries are required.

## 📖 Grammar Specification

The following simplified BNF grammar describes basic assignment statements and arithmetic expressions:

```text
<statement> ::= <identifier> "=" <expression>
<expression> ::= <term> (("+" | "-") <term>)*
<term>       ::= <factor> (("*" | "/") <factor>)*
<factor>     ::= <number> | <identifier> | "(" <expression> ")"
```

**Note:** This grammar illustrates the intended language structure. The program uses Python's built-in parser, which supports Python syntax rather than enforcing this specific BNF grammar.

## ⚙️ How It Works

1. The `ast` module is imported.
2. The `convert_to_ast()` function accepts a Python program as a string.
3. `ast.parse()` parses the source code and generates an AST.
4. `ast.dump()` displays the AST with indentation for readability.
5. If the input contains invalid Python syntax, a `SyntaxError` is caught and displayed.

## 💻 Example Code

```python
import ast

def convert_to_ast(program):
    try:
        tree = ast.parse(program)
        print("Abstract Syntax Tree (AST):")
        print(ast.dump(tree, indent=4))
    except SyntaxError as e:
        print("Syntax Error:", e)

program = "a = 10 + 5 * 2"
convert_to_ast(program)
```

## ▶️ How to Run

**Step 1:** Ensure Python is installed on your system.

Check the installation:

```bash
python --version
```

**Step 2:** Save the Python code in a file named `ast_generator.py`.

**Step 3:** Open a terminal in the project directory and run:

```bash
python ast_generator.py
```

## 📤 Sample Output

For the input:

```python
a = 10 + 5 * 2
```

The output will be similar to:

```text
Abstract Syntax Tree (AST):
Module(
    body=[
        Assign(
            targets=[
                Name(id='a', ctx=Store())],
            value=BinOp(
                left=Constant(value=10),
                op=Add(),
                right=BinOp(
                    left=Constant(value=5),
                    op=Mult(),
                    right=Constant(value=2))))],
    type_ignores=[])
```

The exact formatting may vary slightly between Python versions.

## 🧠 Key Concepts

- **AST:** A tree representation of the syntactic structure of source code.
- **Parsing:** The process of analyzing source code according to a programming language's syntax.
- **Operator Precedence:** Multiplication is evaluated before addition, so `10 + 5 * 2` is represented as `10 + (5 * 2)`.
- **Syntax Error Handling:** Invalid Python syntax is caught using `try` and `except`.

## 🚀 Applications

- Compiler design and construction.
- Interpreter development.
- Static code analysis.
- Source code transformation.
- Understanding parsing and syntax trees.

## 🔮 Future Improvements

- Implement a custom lexer and parser based on the specified BNF grammar.
- Visualize the AST as a graphical tree.
- Support additional operators and expression types.
- Add unit tests for valid and invalid inputs.
- Validate input against the custom grammar rather than Python's full syntax.


## 📄 License

This project is available for educational and learning purposes.
