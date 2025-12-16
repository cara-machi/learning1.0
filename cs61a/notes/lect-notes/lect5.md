---
title: "CS61a -- Lect 05：Environment "
author: 
date: Dec5 2025 Fri
---

### 1.1 Frames & Environments:
- Frame = mapping of variables
- Parent environment chain for variable lookup
- Global frame created at program start
- Local frame created at function call

### 1.2 Lexical Scoping
- Variables are lookedd up in the frame where the function was defined 

### 1.3 Call Expression Evaluation Order
1. Evaluate operator: Function Object
2. Evluate operand: argument values 
3. Create local frame: bind parameters
4. Exectue function body 

### 1.4 Closures & HOFs
- Returned functions remember preant frame environment 

### 1.5 Lambda Functions 
- Anonymous functions, smae rules as normal functions 
- Captures the defnining environments 
- Local frame created when called 

## 2. Common Confusions 
- formall parameters vs operands vs arguments vs variables
1. formal parameters: names in the function definition 
2. Operands: expressions in the function call
3. Arguments: the evalated results of operands
4. Variables: bindings inside a frame

- Nested function calls: inner frames created first

## Compose Example & Bottlenecks
[compose on github] 
```python 
from compose import compose1, square, make_adder
add2 = make_adder(2)
f=compose1(square,make_adder(2))
print f(3)
```
**My Question**:
1. when drawing diagrams, why drawing make_adder as the f1 frame instead of square?
Answer: 
1. we should evaluate the compose1(squre,make_adder(2)) in a call-expression order. 
2. So, the order should be operator compose1, and operand square and operand make_adder(2)
3. The reason calling the operand make_adder(2) under f1 instead of compose
Because although operator evaluated first, all operands should be evaluated fully to values then we could apply operator on operands. 
4. The reason calling the opearnd make_adder(2) under f1 instead of square
Becaue square has already been the function object, and make_adder(2)is a call expression, the first step for it is to  evalaute it to a function object
**MY Takeaway**
1. I still sometimes call expression is evaluated to a functino object. 
2. Simplest way to differ from function object and call expression is to find ()
Example:
square is a function object, square(x) is a call expression.



