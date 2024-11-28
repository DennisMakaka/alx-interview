# 0x08. Making Change

## Project Overview
The "0x08. Making Change" project addresses the optimization problem of finding the minimum number of coins required to achieve a given total. Using a list of available coin denominations, the goal is to implement an efficient solution for determining the fewest coins needed to meet a target total.

This project leverages algorithms, including greedy approaches and dynamic programming, to solve the problem while considering edge cases like when the total is zero or cannot be achieved.

## Learning Objectives
By completing this project, you will:
- Apply greedy algorithms to optimization challenges.
- Explore dynamic programming concepts, including overlapping subproblems and optimal substructure.
- Analyze algorithmic complexity to ensure efficiency.
- Enhance your Python programming skills, particularly in handling lists and control flow structures.

## General Requirements
- Code must execute on Ubuntu 20.04 LTS with Python 3.4.3.
- All files must conform to PEP 8 style guide (version 1.7.x).
- A mandatory `README.md` file must be included in the project directory.
- All Python scripts should start with `#!/usr/bin/python3`.
- Files must be executable and end with a new line.

## Function Objective
The task involves implementing a function that:
- Determines the fewest number of coins required to meet a given total.
- Returns -1 if the total cannot be achieved using the provided denominations.

### Examples
- A total of 37 with coins `[1, 2, 25]` requires 7 coins.
- A total of 1453 with coins `[1256, 54, 48, 16, 102]` is impossible, returning -1.

## Key Concepts
- **Greedy Algorithms**: Make locally optimal choices at each step to attempt a global solution. This approach may not work for all coin sets.
- **Dynamic Programming**: Divide the problem into smaller sub-problems, solving each optimally and reusing results to avoid redundant calculations.
- **Algorithm Complexity**: Focus on minimizing both time and space complexity for efficiency.

## Useful Resources
- **Python Documentation**: Explore tools like loops, conditional statements, and lists.
- **GeeksforGeeks**: Articles on solving the coin change problem using both dynamic programming and greedy algorithms.
- **YouTube Tutorials**: Visual explanations of the coin change problem and its solutions.
