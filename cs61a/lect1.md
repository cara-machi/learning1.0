# CS61A Lecture 1 Notes — Call Expressions & Metaprogramming Insight

## 1. Call Expression Overview

A **call expression** invokes a function with arguments.

**Example:**
```scheme
(add 2 3)
Components:

    Operator: add (the function before parentheses)

    Operands: 2, 3 (the arguments)

    ⚡ Both operators and operands are expressions that evaluate to values.

2. Evaluation Process

    Call expressions follow a strict evaluation procedure:
        (operator operand1 operand2 ...)
    Step 1: Evaluate the Operator

        The operator is an expression that must evaluate to a function

        Example: add → function object that performs addition

    Step 2: Evaluate Each Operand

        Each operand expression is evaluated to produce its value

        Example: 2 → number 2, 3 → number 3

    Step 3: Apply the Function

        Apply the function from Step 1 to the arguments from Step 2

        Example: add(2, 3) → 5

3. Evaluation Flow
    Call Expression: (add 2 3)
        │
        ▼
    Evaluate Operator: add → function
        │
        ▼
    Evaluate Operands: 2 → 2, 3 → 3
        │
        ▼
    Apply Function: add(2, 3) → 5

4. Key Insight: Why Evaluate Everything?

Initial Question: Why evaluate operators like mul if they're just "actions"?

Metaprogramming Answer:
Scheme is homoiconic — code is data. The program can read, analyze, and transform code as if it were any other list. This enables powerful metaprogramming where programs can manipulate other programs.

Technical Reason:
mul is a variable bound to a procedure. The interpreter must evaluate it to get the actual function before application.

5. Personal Reflection
This revelation sparked my interest in LISP/Scheme philosophy:

    Abstraction Depth: Coding transcends syntax to become data manipulation

    Philosophical Foundation: Programs that write programs

    Expressive Power: Minimal syntax exposes profound computational concepts

    AI Connections: This approach enables systems that generate and reason about code

6. Key Takeaways
    Uniform Evaluation: Operators and operands follow the same evaluation rules

    Evaluation Order Matters: Operator first, then operands, then application

    Code as Data: Enables metaprogramming and higher-order abstractions

    Elegant Design: Scheme's minimalism reveals computational fundamentals