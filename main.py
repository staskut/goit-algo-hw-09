from time import time
import matplotlib.pyplot as plt


def find_coins_greedy(amount, coins=[50, 25, 10, 5, 2, 1]):
    result = {}
    for coin in coins:
        if amount >= coin:
            count = amount // coin
            amount -= coin * count
            result[coin] = count
            if amount == 0:
                break
    return result


def find_min_coins(amount, coins=[50, 25, 10, 5, 2, 1]):
    dp = [float('inf')] * (amount + 1)  # кількість монет для кожної підсуми
    dp[0] = 0
    coin_used = [0] * (amount + 1)  # максимальний номінал щоб потім відновити набір монет

    for i in range(1, amount + 1):
        for coin in coins:
            if i >= coin:
                if dp[i - coin] + 1 < dp[i]:
                    dp[i] = dp[i - coin] + 1
                    coin_used[i] = coin

    result = {}
    while amount > 0:
        coin = coin_used[amount]
        if coin in result:
            result[coin] += 1
        else:
            result[coin] = 1
        amount -= coin

    return result


def measure_time(func, args):
    start = time()
    func(args)
    return time() - start


def measure_mean_time(func, args):
    results = []
    for _ in range(10):
        results.append(measure_time(func, args))
    return sum(results) / len(results)


if __name__=="__main__":
    amount = 436
    greedy_result = find_coins_greedy(amount)
    dynamic_result = find_min_coins(amount)

    print(greedy_result)
    print(dynamic_result)

    amount_values = list(10 ** i for i in range(20))
    greedy_times = [measure_mean_time(find_coins_greedy, amount) for amount in amount_values]

    plt.figure(figsize=(10, 6))
    plt.plot(amount_values, greedy_times, label='Greedy Algorithm', marker='o')
    plt.xscale("log")
    plt.xlabel('Amount')
    plt.ylabel('Time (seconds)')
    plt.title('Жадібний алгоритм має сталий час виконання для різних сум')
    plt.legend()
    plt.grid(True)
    plt.show()

    amount_values = list(range(1, 10001, 50))
    dynamic_times = [measure_time(find_min_coins, amount) for amount in amount_values]

    plt.figure(figsize=(10, 6))
    plt.plot(amount_values, dynamic_times, label='Dynamic Programming', marker='x')
    plt.xlabel('Amount')
    plt.ylabel('Time (seconds)')
    plt.title('Алгоритм динамічного програмування показує лінійну залежність від суми')
    plt.legend()
    plt.grid(True)
    plt.show()

    amount_values = list(10**i for i in range(5))
    greedy_times = [measure_time(find_coins_greedy, amount) for amount in amount_values]
    dynamic_times = [measure_time(find_min_coins, amount) for amount in amount_values]

    plt.figure(figsize=(10, 6))
    plt.plot(amount_values, greedy_times, label='Greedy Algorithm', marker='o')
    plt.plot(amount_values, dynamic_times, label='Dynamic Programming', marker='x')
    plt.xscale("log")
    plt.xlabel('Amount')
    plt.ylabel('Time (seconds)')
    plt.title('Execution Time Comparison')
    plt.legend()
    plt.grid(True)
    plt.show()
