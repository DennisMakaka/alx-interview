# 0x0A. Prime Game

## Project Overview
This project involves implementing an algorithm to solve a game played with prime numbers. The goal is to write a Python function that determines the winner of the "Prime Game" based on the rules described below.

## Game Rules
- The game is played by two players, Maria and Ben.
- An array `nums` contains integers. Each round uses a number from the array.
- For a number `n`:
  - Maria and Ben take turns picking prime numbers less than or equal to `n`.
  - When a prime is chosen, it and all its multiples are removed.
  - The player unable to make a move loses that round.
- The winner is the one who wins the most rounds.

## Steps to Implement the Solution

### Understand Primes
You need an efficient method to find prime numbers and handle large values of `n`. Using the **Sieve of Eratosthenes** is recommended for this purpose.

### Core Functionality
Write a function `isWinner(x, nums)` where:
- `x`: Number of rounds.
- `nums`: Array of integers for each round.

The function should return the name of the player who won the most rounds ("Maria" or "Ben"). If there is a tie, return `None`.

### Plan the Logic
1. Precompute primes up to the largest number in `nums` using the Sieve of Eratosthenes.
2. Simulate the game for each round and determine the winner based on the rules.
