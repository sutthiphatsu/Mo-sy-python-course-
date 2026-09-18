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
        total += x * price
        print(f"your {x} electity {price} each = {x * price}")
        break

    x = first(x, end - first + 1)
    segment_total = x * price
    total += segment_total
    x -= x
    print(f"your {x} electity {price} each = {segment_total}")
total += 25
print(f"Total = {total}")
print(f"add tax 25")
