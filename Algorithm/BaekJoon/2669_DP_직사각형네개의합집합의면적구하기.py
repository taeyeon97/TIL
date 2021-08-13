box = [[0] * 100 for _ in range(100)]

for i in range(4):
    x, y, xx, yy = map(int, input().split())
    for j in range(x, xx):
        for k in range(y, yy):
            if box[j][k] == 0:
                box[j][k] += 1

final_list = []

for b in box:
    final_list += b

print(sum(final_list))
