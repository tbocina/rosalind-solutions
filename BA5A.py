# BA5A
# The Change Problem
# Find the minimum number of coins needed to make change

def dpChangeMoney(money, coins):
    minNumCoins = {0: 0}
    for i in range(1, money + 1):
        minNumCoins[i] = float('inf')
        for j in range(0, len(coins)):
            if i >= coins[j]:
                if minNumCoins[i - coins[j]] + 1 < minNumCoins[i]:
                    minNumCoins[i] = minNumCoins[i - coins[j]] + 1
    return minNumCoins[money]


if __name__ == "__main__":
    """
    money = 40
    coins = [1, 5, 10, 20, 25, 50]
    print(dpChangeMoney(money, coins))
    """
    with open("./rosalind_ba5a.txt") as myfile:
        inlines = [x.strip("\n") for x in myfile.readlines()]
        money = int(inlines[0])
        coins = [int(x) for x in inlines[1].split(",")]
    print(dpChangeMoney(money, coins))
