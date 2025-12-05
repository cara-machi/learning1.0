---
title: "CS61a -- Lect 05：Environment "
author: 
date: Dec5 2025 Fri
---

## 1.Core Definitions

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
- Arguments vs parameters vs varaibles 
- Operand evaluation vs frame creation 
- Nested function calls: inner frames created first


## 3. Digrams Folder

### 3.1 make_adder

### 3.2 compose

### 3.3 compose_make_adder_call

### 3.4 lambda_closure_example.md

## 4. Exercise Folder



