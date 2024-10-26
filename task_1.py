import time

def find_coins_greedy(amount):
    coins = [50, 25, 10, 5, 2, 1]
    result = {}
    remaining = amount
    for coin in coins:
        count = remaining // coin
        if count > 0:
            result[coin] = count
            remaining -= coin * count
    return result

def find_min_coins(amount):
    coins = [1, 2, 5, 10, 25, 50]
    max_amount = amount + 1
    dp = [max_amount] * (amount + 1)
    dp[0] = 0
    coin_used = [0] * (amount + 1)
    for a in range(1, amount + 1):
        for coin in coins:
            if coin <= a:
                if dp[a - coin] + 1 < dp[a]:
                    dp[a] = dp[a - coin] + 1
                    coin_used[a] = coin
    if dp[amount] == max_amount:
        return {}
    result = {}
    a = amount
    while a > 0:
        coin = coin_used[a]
        if coin in result:
            result[coin] += 1
        else:
            result[coin] = 1
        a -= coin
    return result

if __name__ == "__main__":
    amount = 113

    start_time = time.time()
    greedy_result = find_coins_greedy(amount)
    finish_time = time.time() - start_time
    print(f"Жадібний алгоритм: {greedy_result}, час: {finish_time}")

    start_time = time.time()
    dp_result = find_min_coins(amount)
    finish_time = time.time() - start_time
    print(f"Динамічне програмування: {dp_result}, час: {finish_time}")

    amount = 1111111

    start_time = time.time()
    greedy_result = find_coins_greedy(amount)
    finish_time = time.time() - start_time
    print(f"Жадібний алгоритм: {greedy_result}, час: {finish_time}")

    start_time = time.time()
    dp_result = find_min_coins(amount)
    finish_time = time.time() - start_time
    print(f"Динамічне програмування: {dp_result}, час: {finish_time}")
