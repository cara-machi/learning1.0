---
title: "CS61a -- Lect 03：Life Cycle of a User-Defined Function "
author:
date: Dec 3 2025 Wed
---

# Lecture 03 - Life Cycle of a User-Defined Function

This note summarizes my understading how Python executes user-defined function 

User-Defined Function
```python
def squre(x):
    return x*x
Steps:
1) Python creates a new function object in memory 
2) The function name square is an abstract way of the whole def statement including function signature function body and current environment or frame/ usually the global frame 
```

## Example 
```python 
from operator import floordiv, mod

def divide_exact(n, d):
    # Returns two values packed in a tuple
    return floordiv(n, d), mod(n, d)

# Call the function and unpack the result into two variables
q, r = divide_exact(2013, 10)

# Nothing prints yet because return + assignment ≠ print
# To see the values, we explicitly print them
print(q, r)  # Output: 201 3
```
### Step by Step Explanaiton 
- Function call: divide_exact(2013, 10)
- Python creates a local frame for the function.
- n = 2013, d = 10 live in the local frame.
- Compute results inside the function: floordiv(n, d) → 201 mod(n, d) → 3
- Return value: The function returns a tuple (201, 3) to the caller.
- The local frame is destroyed, but the tuple survives on the heap.
- Assignment + unpacking: q, r = (201, 3) q gets 201 r gets 3 
- This happens in the global frame (your top-level script). No output appears automatically.
- Printing: Only print(q, r) explicitly shows the result: 201 3.
### Key Points to Remember
- Return ≠ Print: Returning a value only passes it to the caller.
- Unpacking: Python takes one object (tuple) and binds each element to the variables on the left-hand side.
- Frames: Function execution happens in a local frame, while assignment to q and r happens in the global frame.
- Tuples are invisible in CS61A diagrams, but including them can help understand what Python actually returns.
### My Confusion Point
1. Why nothing prints: 
Returning and assigning are separate from printing. Python only prints automatically in interactive interpreters (REPL) when an expression is evaluated at the top level — but not for q, r = ... or inside scripts.
2. is this a Higher Order Function 
is not a higher-order function because it returns results, not functions.
-  ✔It uses other functions (floordiv and mod).
- ✘But it does not return functions.
- → Therefore, it is not a higher-order function.