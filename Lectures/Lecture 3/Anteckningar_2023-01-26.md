# Lektion 3

Lösning för stack implementerat med pythons inbyggda lista ligger under mappen _python_.
Lösning för stack implementerat med std::vector i C++ ligger under mappen _cpp_.

Nedan utdata från körningar



## Python
### Stack
```
my_stack: None
Empty? True

my_stack: hello -> None
my_stack: world -> hello -> None
Empty? False
peek: world

pop: world
my_stack: hello -> None
pop: hello
my_stack: None
peek: None
```

### Queue
```
my_queue: None
Empty? True

my_queue: hello -> None
my_queue: world -> hello -> None
Empty? False
peek: hello

dequeue: hello
my_queue: world -> None
dequeue: world
my_queue: None
peek: None
```

## C++

### Stack
```
$ ./stack.exe
My stack: []
Empty?: true

My stack: ['1']
My stack: ['2', '1']
Empty?: false
Size:2
Peek: 2

Pop: 2
My stack: ['1']
Pop: 1
My stack: []
Peek:terminate called after throwing an instance of 'std::out_of_range'
  what():  Stack is empty

```

### Queue
```
$ ./queue.exe
My queue: []
Empty?: true

My queue: ['1']
My queue: ['2', '1']
Empty?: false
Size: 2
Peek: 1

Dequeue: 1
My queue: ['2']
Dequeue: 2
My queue: []
Peek: terminate called after throwing an instance of 'std::out_of_range'
  what():  Queue is empty

```

## Komplexitet

