![ALT Text](https://media.geeksforgeeks.org/wp-content/uploads/tower-of-hanoi.png)

# Tower of Hanoi
The <b>Tower of Hanoi</b> is a classic puzzle that involves moving disks from one peg to another peg while following specific rules. 
The puzzle consists of three pegs and a number of disks of different sizes, 
which can be stacked in decreasing order of size on any peg.

The rules of the Tower of Hanoi puzzle are as follows:

    1. Only one disk can be moved at a time.
    2. Each move consists of taking the top disk from one of the stacks and placing it on top of another stack.
    3. A larger disk cannot be placed on top of a smaller disk.
    
## Working:
Two functions:

1. hanoi(n, f, h, t): use recursion to move disks from f to t using h as helper 


    * n as number of disks
    * f as from 
    * h as helper position
    * t as target
2. move(f,t): just outputs the disks on each step of recursion

    * f as from
    * t as to
# Run
To run this you just need python.
```python Tower-of-hanoi-Recursion-Python.py```
