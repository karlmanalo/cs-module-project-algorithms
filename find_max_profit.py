# Returns the maximum profit that can be made from a single buy and sell of Bitcoin.

# bitcoin_prices = [1050, 270, 1540, 3800, 2]
def find_max_profit(arr):
    potential_profit = []
    for i in range(len(arr) - 1, 0, -1):
        for j in range(len(arr) - 2, 0, -1):
            potential_profit.append(arr[i] - arr[j])
    return max(potential_profit)