current_list = [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123]
print([current_list[el] for el in range(1,len(current_list)) if current_list[el] > current_list[el-1]])