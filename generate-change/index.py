def generate_change(cents):
  coins = [
    ["dollar", 100],
    ["half-dollar", 50],
    ["quarter", 25],
    ["dime", 10],
    ["nickle", 5],
    ["penny", 1]
  ]
  change = {}
  for i in range(len(coins)):
    change[coins[i][0]] = round(cents/coins[i][1])
    cents %= coins[i][1]
  for coin in change:
    print(coin + ": " + str(change[coin]))

generate_change(1234)
