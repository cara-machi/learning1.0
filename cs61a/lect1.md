# CS61A Lecture 1 Notes — Call Expressions & Metaprogramming Insight

Author: 

Date: Dec8 2025 


## 1. Core Definition 

-  Expressions: process of computing things 
-  Call expressions: an expression which use an operator on the opearnd to get a value. 
-  Operator: one **expression** evaluated to a function object; add, mul, max... 
-  OPerand: one **expression** evalutated to the value, whihch will be passed to the formal parameters: in ``` add(2,3) ```, operands are 2 and 3

## 2. Evaluation Procedure 
1. Evaluate the operator
2. Evaluate each operand
3. Apply the operand on the opeartor 

## 3. Mini Example
```python 
mul(add(2,3),4)
```
1. Evaluate mul 
2. Evaluate operand add(2,3) and operand 4
3. Evaluate operator add 
4. Evaluate operand (2,3)
5. Apply the operator add on the operand (2,3) and get function add(2,3)=5
6. Apply the operator mul on the operand (5,4) get function mul(5,4)=20


## 6. Key Takeaways
1. uniform evalutaion: operators and operands follow the same evaluation rules; 
2. Evaluation Order Matters: Operator first, then operands, then application; from outer to inner

## 7. Personal Bottelnecks
1. Why do operators need to be evaluated at all, if they are just actions?
Insight: Operators are names bound to function objects, so Python must look up the object before apply it
