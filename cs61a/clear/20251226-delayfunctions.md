# Tricky Examples with Clear understanding 

``` python
#A 
x = add(5, 6)
# B
def f():
    return add(5, 6)
# C
def f():
    return add

```

- Q: 
- 1 In which cases does add(5,6) run immediately?
- 2 In which case is it delayed until a later call?

``` python
#A 
x = add(5, 6)
# add(5,6) execute immediately 
# B
def f():
    return add(5, 6)
# add(5,6) is delayed 
# it runs only when calling f()
```
# C
```python
def f():
    return add
```
**nothing is executed or delayed only returnning a function object**

- f() first get function add
- f()(5,6)then call the function add on (5,6)

## One-sentence compression 
- in Python, defining creates function objects.
- calling them means executing them 
- dealying them means **wraping the call inside another function** so execution happens later under control 