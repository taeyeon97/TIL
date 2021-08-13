row, col = map(int, input().split())
cnt = int(input())

box = [[0] * row for _ in range(col)]
print(box)


for _ in range(cnt):
    start, end = map(int, input().split())
    for i in range(col):
        for j in range(row):
            if start == 0:
                box[end][i] += 1
                box.append([0] * row)
                row += 1
            elif start == 1:
                box[j][end] += 1
                for k in range(len(box)):
                    col += 1
                    box[k] = [0] * col

    print(box)
