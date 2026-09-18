bucket = [
    [1, 50, 2.50],
    [51, 100, 3.00],
    [101, 200, 3.50],
    [200, None, 4.00]
]

x = 220
total = 0

for first, end, price in bucket:
    if x <= 0:
        break

    if end is None:
        used = x
        total += used * price
        print(f"your {used} items are charged at {price} each = {used * price}")
        break

    used = min(x, end - first + 1)
    segment_total = used * price
    total += segment_total
    x -= used
    print(f"your {used} items are charged at {price} each = {segment_total}")

print(f"Total = {total}")