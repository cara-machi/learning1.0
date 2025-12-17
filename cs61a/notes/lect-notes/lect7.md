```python
Example:
a=1
def f(g):
    a=2
    return lambda y: a* g(y)
f(lambda y: a+y)(a)
```

## Bottlenecs / Confusion 
1. i could not understand ``` f(lambda y: a + y)```lambda y: a+y seems to have a parent as f1 frame not the global,like nested defnition. 

## Bottlenecks / Confusion
1. what does g(y) represent? 
2. Answer: it is just the line 7 in the parenthese where a lambda function around foraml parameter y
## Key distinoction i initailly overlooked regarding question 
1. g(y) iis just the function regarding y and passed as the argument to f(g) represented by lambday: a+y


```python
f(lambda y: a+y)(a)
```
## Bottlenecks / Confusion 
1. i am confused why ```f(lambda y: a + y)(a)``` the second a should be 1; i think i should apply the lexical scope to get the value of a from f1 frame a=2

## Key distinoction i initailly overlooked regarding question 
1. i forget about the call expression procedure again
**Call Expression Procedure**
1. Evaluate the operator to a function object # h=lambda y:a+y
2. Evaluate the operand **in the current frame**
**The function body has not started yet No new frame exists yet**
3. Apply the function
4. Create a new frame (parent = the environment where function was defined, the lexical scope)
5. Bind formal parameters (**Bind the value of the arguments to the formal parameters**)
6. Execute the function body, and resolve the free variable with the lexical scope solution. 
**Argument expressions are evaluated in the caller’s environment before the function is called**

## Key distinoction i initailly overlooked regarding question 2
2. i am confsued with the lexical scope is applied for free varibale not for argument. 
**Lexical Scoping applies only for free variables inside function bodies**
**Not to arguments on the site call**

# in Summary
1. Evaluate operator
2. Evaluate operands
3. Apply → create frame
**even the operand or the operator itself is the function, stilll no frame created**
**A frame is only created when the function is applied**
**Frames are created only when a function body starts executing. Evaluating the operator or operands is just evaluation; no frames yet.**

```python
Example:
a=1
def f(g):
    a=2
    return lambda y: a* g(y)
f(lambda y: a+y)(a)
```

# Key distcinctions i initially overlooked
1. y in lambda y is the formal parameter, does not represent function itself.
2. a in f(lambda...)(a) a is an argument and ready to pass value to the formal parameter -- parameters receive arugments provide 
3. tomorrow i will draw diagrams again. 

## Bottlenecks / Confusion 
1. print (5) why it is evaluated to none and still print something out 