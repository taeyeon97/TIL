num = int(input())
status = list(map(int, input().split()))
student = int(input())
# print(num, status, student)
for _ in range(student):
    gender, give_num = map(int, input().split())
    # print(gender, give_num)
    if gender == 1:
        n = 1
        give_num_list = []
        while give_num * n <= num:
            give_num_list.append(give_num * n)
            n += 1
        for i in give_num_list:
            if status[i - 1] == 1:
                status[i - 1] = 0
            else:
                status[i - 1] = 1

    elif gender == 2:
        cnt = 1
        give_num_list = []
        for i in range(give_num - 1):
            if status[give_num - 1 : give_num + i + 1] == status[give_num - i - 2 : give_num][::-1]:
                cnt += 2
        if cnt >= 3:
            for i in range(cnt // 2):
                if status[give_num - 2 - i] == 1:
                    status[give_num - 2 - i] = 0
                else:
                    status[give_num - 2 - i] = 1
                if status[give_num + i] == 1:
                    status[give_num + i] = 0
                else:
                    status[give_num + i] = 1

        if status[give_num - 1] == 1:
            status[give_num - 1] = 0
        else:
            status[give_num - 1] = 1

for pr in range(0, len(status), 20):
    print(*status[pr : pr + 20])
