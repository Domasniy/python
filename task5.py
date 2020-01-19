my_list = [7, 5, 3, 3, 2]
original_list = my_list[:]
new_rate = int(input('Введите число рейтинга для добавления: '))

if my_list.count(new_rate) != 0:
    index_to_insert = len(my_list[::-1]) - my_list[::-1].index(new_rate) - 1
    my_list.insert(index_to_insert+1,new_rate)
elif new_rate < my_list[-1]:
    my_list.append(new_rate)
else:
    for index,el in enumerate(my_list):
        if new_rate > el:
            my_list.insert(index,new_rate)
            break        

print(original_list)
print(my_list)