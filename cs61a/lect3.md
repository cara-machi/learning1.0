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

Why global usually?
on top of the module/ script





Part A Difficult for me part:
1. different names for the same thing under different circumstances. 
for example: def square(x): 
x could be formal parameter; could be argument; could be assinged value. 
2. some expressions lecturers his unique way making me difficult to understand 
local frame is followed by global frame. it took me a while to realize local frame comes first, then global frame comes next. 
3. new words: quotient 
(this part is fine, i could use the words freely as well.)