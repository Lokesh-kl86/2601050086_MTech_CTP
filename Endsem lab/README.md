# Endsem Lab - Practical 11

## Aim

To implement Stack and Queue in Python using dataclasses and type hints.

## Description

A Stack follows LIFO (Last In, First Out) and is used to maintain recently visited web pages.

A Queue follows FIFO (First In, First Out) and is used to process download requests in the order they are added.

## Program

The program implements:
- `push()`
- `pop()`
- `peek()`
- `enqueue()`
- `dequeue()`

See `practical11.py` for the complete program.

## Output

```text
Current page: YouTube
Going back: YouTube
Current page: Google

Downloads:
Movie.mp4
Notes.pdf
```

## Analysis and Inference

The Stack successfully manages browser history using LIFO. The Queue processes download requests using FIFO. The program correctly demonstrates push, pop, peek, enqueue, and dequeue operations.

## Viva Questions and Answers

### 1. What is a Stack?

A Stack is a data structure that follows LIFO (Last In, First Out).

### 2. What is a Queue?

A Queue is a data structure that follows FIFO (First In, First Out).

### 3. What is push() and pop()?

`push()` adds an element to the Stack. `pop()` removes the last element.

### 4. What is enqueue() and dequeue()?

`enqueue()` adds an element to the Queue. `dequeue()` removes the first element.

### 5. What is peek()?

`peek()` displays the top element of the Stack without removing it.
