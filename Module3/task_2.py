list1 = [1, 3, 5, 7, 9]
list2 = [2, 4, 5, 6, 8, 10]

res = []
l1_index = 0
l2_index = 0

while l1_index < len(list1) and l2_index < len(list2):
    if list1[l1_index] < list2[l2_index]:
        res.append(list1[l1_index])
        l1_index += 1
    elif list1[l1_index] > list2[l2_index]:
        res.append(list2[l2_index])
        l2_index += 1
    else:
        res.append(list1[l1_index])
        l1_index += 1
        l2_index += 1

while l1_index < len(list1):
    res.append(list1[l1_index])
    l1_index += 1

while l2_index < len(list2):
    res.append(list2[l2_index])
    l2_index += 1

print(res)

# list1 = [1, 3, 5, 7, 9]
# list2 = [2, 4, 5, 6, 8, 10]
#
# list1.extend(list2)
# print(sorted(set(list1)))