# Endsem Lab - Practical 11

## Aim

To design and implement reusable Stack and Queue data structures in Python using dataclasses and type hints. The Stack is used to demonstrate browser history operations such as visiting a web page with `push()`, going back with `pop()`, and viewing the current page with `peek()`. The Queue is used to demonstrate download request processing using `enqueue()` and `dequeue()`.

## Description

Stack and Queue are fundamental linear data structures used to store and manage data in different orders. A Stack follows the LIFO (Last In, First Out) principle, where the most recently added element is removed first. In this practical, the Stack represents recently visited web pages, similar to the Back operation of a web browser.

A Queue follows the FIFO (First In, First Out) principle, where the first element added is processed first. In this practical, the Queue represents download requests, so downloads are processed in the same order in which they were added. Python dataclasses are used to simplify class creation, while type hints specify the type of data stored and passed to the methods.

## Program

The program implements:
- `push()` - adds a web page to the Stack.
- `pop()` - removes the most recently visited web page.
- `peek()` - displays the current web page.
- `enqueue()` - adds a download request to the Queue.
- `dequeue()` - processes the first download request.

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

The Stack successfully manages browser history using the LIFO principle. When YouTube is added after Google, it becomes the current page and is removed first when the user goes back. The Queue successfully processes download requests using the FIFO principle, so Movie.mp4 is processed before Notes.pdf. Thus, all required Stack and Queue operations work correctly.

## Viva Questions and Answers

### 1. What is a Stack?

A Stack is a linear data structure that follows LIFO (Last In, First Out). The last inserted element is removed first.

### 2. What is a Queue?

A Queue is a linear data structure that follows FIFO (First In, First Out). The first inserted element is removed first.

### 3. What is push() and pop()?

`push()` adds an element to the Stack. `pop()` removes the most recently added element from the Stack.

### 4. What is enqueue() and dequeue()?

`enqueue()` adds an element to the Queue. `dequeue()` removes the first element from the Queue.

### 5. What is peek()?

`peek()` displays the top element of the Stack without removing it.
