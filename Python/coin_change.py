def coin_change(S, n):
  if n < 0:
      return 0
  table = [0] * (n + 1)
  table[0] = 1
  for coin_val in S:
      for j in range(coin_val, n + 1):
          table[j] += table[j - coin_val]
  return table[n]

if __name__ == "__main__":
    coin_array = input("Enter the array of coins (e.g: 1,2,3): ").split(",")
    amount = input("Enter the amount to derive: ")
    for i in range(0, len(coin_array)):
        coin_array[i] = int(coin_array[i])
    print("The number of possible ways the given sum can be made is: ",coin_change(coin_array,int(amount)))
