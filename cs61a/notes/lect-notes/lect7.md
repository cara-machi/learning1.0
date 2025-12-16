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