my_list = [42, 69, 0, 322, 13, 0, 99, -5, 9, 8, 7, -6, 5]
index_number = -1
len_my_list = len(my_list)
while (index_number + 1 < len_my_list):
    index_number += 1
    if my_list[index_number] == 0:
        continue
    if my_list[index_number] > 0:
        print(my_list[index_number])
    else:
        break
