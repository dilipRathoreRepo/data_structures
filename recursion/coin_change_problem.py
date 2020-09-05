tgt = 63
list_of_coins = [1, 5, 10]


# OPTION 1 : Using recursion (not ideal solution)
def rec_coin(target, coins):
    if target in coins:
        return 1

    num_coins = target

    for i in [c for c in coins if c <= target]:
        min_coins = 1 + rec_coin(target-i, coins)

        if min_coins < num_coins:
            num_coins = min_coins

    return num_coins


# print(rec_coin(tgt, list_of_coins))


# Option 2 : using cache to minimize recursion calls
def rec_coin_dynamic(target, coins, known_results):
    num_coins = target
    if target in coins:
        known_results[target] = 1
        return 1
    elif known_results[target] is not None:
        return known_results[target]
    else:
        for i in [c for c in coins if c <= target]:
            min_coins = 1 + rec_coin_dynamic(target-i, coins, known_results)

            if min_coins < num_coins:
                num_coins = min_coins
                known_results[target] = min_coins
    return num_coins


cache = [None] * (tgt + 1)
print(rec_coin_dynamic(tgt, list_of_coins, cache))
