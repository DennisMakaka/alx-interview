# 0x02. Minimum Operations

## Project Overview

This project focuses on calculating the minimum number of operations needed to achieve exactly `n` characters in a text file using only two operations: **Copy All** and **Paste**.

### Key Concepts

- **Dynamic Programming**: Decompose the problem into subproblems for efficient calculation.
- **Prime Factorization**: Reduce the problem to finding the sum of the prime factors of `n`.

### Task: Minimum Operations

Write a function `minOperations(n)` that returns the fewest number of operations required to get exactly `n` characters.

#### Prototype
```python
def minOperations(n):

