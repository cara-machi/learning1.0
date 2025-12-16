---
title: "CS61a -- Lect 04：Higher-Order Function "
author: 
date: Dec 4 2025 Thur
---

## 1.Evaluating Boolean Expressions
1. **And**
    1. Evaluate the left operand; 
    2. If the left is false, **short-circuit**, return the lfet;
    3. If the left is right, evaluate the right and return the right. 
    Example:
    ```python
    [] and 5
    #left=[], false, return 5
    5 and 0
    #left=5 , true, evaluate right
    #right=0 return 0
    5 and 7
    #left=5, true, evalaute right 
    #right=7 return 7
2. **Or**
    1. Evaluate the left operand;
    2. If the left is false, return the right;
    3. If the left is right, **short-circuit**, return the left. 
    Example:
    ```python
    5 or 0
    #the left is right, short-circuit, return 5
    0 or[]
    #the left is false, return the right[]
3. **Not**
    1. If true, return false
    2. If false, return true 
    3. Always return a boolean 
    Example:
    ```python
    not [] 
    #return true 

## 2. Design Functions

## 3 Higher-Order Function (HOF)
-A function that either:
- **accepts a functino as a parameter**,or 
- **return a function**

**Example:** `make_adder(n)` returns a fucntion `adder(x)`

## 1.2 Closure
A function + the environment it remebers when it was created 
-Even if the outer function frame ends, the inner function can still access variables. 
-Example: `n` in `adder(x)`is remembered even after `make_adder(5)` returns. 
-### Closure remembers the object reference from the outer enviornment; mdoifications mayight happen depending on the nature of the formal parameter
    1. immutable objects: `int` `str` 
    2. mutable objects: `list`,`dict`

## 3. Coing Example 
```python
def make_adder(n):
    def adder(x):
        return x+n
    return adder
```
## 4.Diagram description
    1.Gloal frame
    - add5 points to adder function (closure n=5))
    2.call add(10)
    - x =10 (argument)
    - n=5 (from closure)
    -return 15

