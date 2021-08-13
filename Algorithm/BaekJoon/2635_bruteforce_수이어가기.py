num = int(input())

max_value = 0
max_list = []
for i in range(num):
    num2 = num - i
    my_list = [num, num2]
    # print(my_list)

    while True:
        if my_list[-1] > my_list[-2]:
            break

        elif my_list[-1] <= my_list[-2]:
            my_list.append(my_list[-2] - my_list[-1])

        if max_value < len(my_list):
            max_value = len(my_list)
            max_list = my_list[:]

print(max_value)
for max_l in max_list:
    print(max_l, end=" ")
