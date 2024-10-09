# 0x01. Lockboxes

## Project Overview

In this project, you will write a Python algorithm to determine whether all locked boxes can be opened, given a collection of boxes that contain keys to other boxes. You will utilize concepts from graph theory, recursion, and data structures to implement an efficient solution.

## Requirements

### General Requirements

- Allowed editors: vi, vim, emacs
- All files must be interpreted/compiled on Ubuntu 20.04 LTS using Python3 (version 3.4.3)
- All files should end with a new line
- The first line of all your files should be exactly: `#!/usr/bin/python3`
- A `README.md` file, at the root of the folder of the project, is mandatory
- Your code should be documented
- Your code should follow the PEP 8 style (version 1.7.x)
- All files must be executable

## Concepts Required

To successfully complete this project, the following concepts are critical:

### 1. Lists and List Manipulation
- Work with lists, including accessing elements, iterating over lists, and dynamically modifying lists.
- **Resource**: [Python Lists (Python Official Documentation)](https://docs.python.org/3/tutorial/datastructures.html)

### 2. Graph Theory Basics
- Understanding of graph theory and traversal algorithms like **Depth-First Search (DFS)** or **Breadth-First Search (BFS)** can be very helpful, as the problem involves navigating through nodes and edges.
- **Resource**: [Graph Theory (Khan Academy)](https://www.khanacademy.org/math/geometry/hs-geo-logic)

### 3. Algorithmic Complexity
- Understanding time and space complexity will help you write more efficient algorithms.
- **Resource**: [Big O Notation (GeeksforGeeks)](https://www.geeksforgeeks.org/analysis-of-algorithms-big-o-analysis/)

### 4. Recursion
- Some solutions may require a recursive approach to traverse through boxes and keys.
- **Resource**: [Recursion in Python (Real Python)](https://realpython.com/python-recursion/)

### 5. Queue and Stack
- Knowledge of how to implement queues and stacks is crucial for BFS and DFS.
- **Resource**: [Python Queue and Stack (GeeksforGeeks)](https://www.geeksforgeeks.org/stack-vs-queue/)

### 6. Set Operations
- Using sets for keeping track of visited boxes and available keys can optimize the search process.
- **Resource**: [Python Sets (Python Official Documentation)](https://docs.python.org/3/tutorial/datastructures.html)

## Task

### Task 0: Lockboxes
#### Mandatory
You have `n` number of locked boxes in front of you. Each box is numbered sequentially from 0 to n - 1, and each box may contain keys to other boxes.

Write a method that determines if all the boxes can be opened.

**Prototype**:
```python
def canUnlockAll(boxes):
    """
    Determines if all boxes can be opened.
    
    :param boxes: List of lists, where each list represents a box and contains keys to other boxes.
    :return: True if all boxes can be opened, otherwise False.
    """
```

## File Structure

- **GitHub Repository**: `alx-interview`
- **Directory**: `0x01-lockboxes`
- **File**: `0-lockboxes.py`


## Installation and Usage

1. Clone the repository:
   ```bash
   git clone https://github.com/alx-interview/0x01-lockboxes.git
```

2. Navigate to the project directory:
```bash
cd 0x01-lockboxes
```

3. Make sure the Python script is executable:
```bash
chmod u+x 0-lockboxes.py
```

4. Run the script:
```bash
./0-lockboxes.py
```

