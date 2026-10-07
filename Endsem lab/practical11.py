from dataclasses import dataclass, field


@dataclass
class Stack:
    items: list[str] = field(default_factory=list)

    def push(self, x: str):
        self.items.append(x)

    def pop(self):
        return self.items.pop()

    def peek(self):
        return self.items[-1]


@dataclass
class Queue:
    items: list[str] = field(default_factory=list)

    def enqueue(self, x: str):
        self.items.append(x)

    def dequeue(self):
        return self.items.pop(0)


# Browser History
s = Stack()
s.push("Google")
s.push("YouTube")

print("Current page:", s.peek())
print("Going back:", s.pop())
print("Current page:", s.peek())

# Download Queue
q = Queue()
q.enqueue("Movie.mp4")
q.enqueue("Notes.pdf")

print("\nDownloads:")
print(q.dequeue())
print(q.dequeue())
