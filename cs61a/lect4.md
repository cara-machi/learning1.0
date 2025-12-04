---
title: "CS61a -- Lect 04：Higher-Order Function "
author: 
date: Dec 4 2025 Thur
---

##1. Core Definitons

### 1.1 Higher-Order Function (HOF)
-A function that either:
- **accepts a functino as a parameter**,or 
- **return a function**

**Example:** `make_adder(n)` returns a fucntion `adder(x)`

### 1.2 Closure
A function + the environment it remebers when it was created 
-Even if the outer function frame ends, the inner function can still access variables. 
-Example: `n` in `adder(x)`is remembered even after `make_adder(5)` returns. 
-### Closure remembers the object reference from the outer enviornment; mdoifications mayight happen depending on the nature of the formal parameter
    1. immutable objects: `int` `str` 
    2. mutable objects: `list`,`dict`

### 3. Coing Example 
```python
def make_adder(n):
    def adder(x):
        return x+n
    return adder
```
### 4.Diagram description
    1.Gloal frame
    - add5 points to adder function (closure n=5))
    2.call add(10)
    - x =10 (argument)
    - n=5 (from closure)
    -return 15

### 5. Thinking Problem
1. Can we pass a functino as an argumnet to make_adder? how does that work?

1) First Trial --wrong 
```python
def make_adder(f(add5,n)):
    def add5(x):
        return x+5
    return add5+n
```
Explanatin:
1) f(add,n) is not allowed in a function definion
- python syntax only allows def make_adder(f,n): to declare parameters
- add5 is a function objdect, n is a number. (TypeError) should change to `return add5(x)+n` THis way, add5(x)returns a number, and adding n is valid. 
Correct thinking 
1. Accept a function and a parameter n as inputs. 
2. Return a new function
3. When the new function is called, it uses f and n to compute a result
2) Second Trial 
```python
def make_adder(f,n):
    return adder(x)+5
make_adder(f,5)

Problem 1: adder is not defined 
Problem 2:x is not defined: x is used in adder(x),but x is not passed to make_adder
Fix: adder should be a function that takes x as a parameter, add mkae_adder should return the function instead of calling it immediately 
Problem 3: 