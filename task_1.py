import time
from coins_funcs import find_coins_greedy, find_min_coins


def compare_algorithms(amount, coins):
    # Greedy algorithm
    start_time = time.time()
    greedy_result = find_coins_greedy(amount, coins)
    greedy_time = time.time() - start_time

    # Dynamic Programming algorithm
    start_time = time.time()
    dp_result = find_min_coins(amount, coins)
    dp_time = time.time() - start_time

    print(f"Greedy approach: {greedy_result}, Time: {greedy_time:.6f} seconds")
    print(f"Dynamic Programming approach: {dp_result}, Time: {dp_time:.6f} seconds")


coins = [50, 25, 10, 5, 2, 1]

# Test with small amount
amount = 113
compare_algorithms(amount, coins)

# Test with large amount
large_amount = 100000
compare_algorithms(large_amount, coins)
