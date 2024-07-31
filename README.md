# goit-algo-hw-09

Homework 9. Basic Algorithms and Data Structures at GoIT Neoversity

# Coin Change Problem: Greedy vs Dynamic Programming

## Overview
In this task, we implemented two algorithms to solve the coin change problem: a greedy algorithm and a dynamic programming approach. We compared their efficiency and analyzed which method performs better for large amounts.

## Algorithms

### Greedy Algorithm
The greedy algorithm selects the largest coin denomination that does not exceed the remaining amount. This process repeats until the remaining amount is zero. While fast and easy to implement, the greedy approach does not always produce the optimal solution in terms of the minimum number of coins.

### Dynamic Programming Algorithm
The dynamic programming algorithm systematically considers all possible ways to achieve the target amount using the available coin denominations. It guarantees an optimal solution with the minimum number of coins but is more complex and computationally intensive than the greedy algorithm.

## Results

### Example for amount 113:
- **Greedy approach:** {50: 2, 10: 1, 2: 1, 1: 1}
- **Dynamic Programming approach:** {50: 2, 10: 1, 2: 1, 1: 1}

### Performance Comparison for large amount (100000):
- **Greedy approach:**
  - Time: 0.000001 seconds
- **Dynamic Programming approach:**
  - Time: 0.033370 seconds

## Test Environment
The results were obtained on a MacBook Pro 2021 with an Apple M1 Pro processor.

## Conclusion
- The greedy algorithm is generally faster and simpler but might not provide the optimal solution in terms of the number of coins.
- The dynamic programming algorithm, while more computationally expensive, ensures the optimal solution.
- For very large sums, the greedy algorithm outperforms the dynamic programming approach in terms of execution time but should be used only when the coin denominations allow it to return the optimal result.

This comparison demonstrates the trade-offs between simplicity and optimality when choosing between a greedy algorithm and dynamic programming for solving the coin change problem.
