list1 = [1, 3, 5, 7, 9]
list2 = [2, 4, 5, 6, 8, 10]

res = []
l1_index = 0
l2_index = 0
last_append_num = 0

for _ in range(len(list1) + len(list2)):
    if l2_index != len(list2) and (l1_index == len(list1) or list1[l1_index] > list2[l2_index]):
        if list2[l2_index] != last_append_num:
            res.append(list2[l2_index])
            last_append_num = list2[l2_index]
        l2_index += 1
    else:
        if list1[l1_index] != last_append_num:
            res.append(list1[l1_index])
            last_append_num = list1[l1_index]
        l1_index += 1

print(res)

# list1 = [1, 3, 5, 7, 9]
# list2 = [2, 4, 5, 6, 8, 10]
#
# list1.extend(list2)
# print(sorted(set(list1)))