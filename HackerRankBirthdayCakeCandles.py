def birthdayCakeCandles(candles):
    x = 0
    candles = sorted(candles, reverse=True)
    for i in candles:
        if i == candles[0]:
            x += 1
    return x


candles_count = int(input().strip())

candles = list(map(int, input().rstrip().split()))

print(birthdayCakeCandles(candles))
