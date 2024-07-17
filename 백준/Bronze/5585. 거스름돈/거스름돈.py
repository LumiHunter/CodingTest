price = int(input())
exchange = 1000 - price
coins = [500, 100, 50, 10, 5, 1]
ans = 0
for coin in coins:
    if exchange == 0:
        break
    cnt = exchange // coin
    ans += cnt
    exchange -= cnt * coin
print(ans)