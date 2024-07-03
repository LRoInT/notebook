list1 = [1, 2, 3, 4, 5]
list2 = [4, 5, 6, 7, 8]

# 使用集合操作获取不同的项
diff = list(set(list1) - set(list2))

print(diff)  # 输出: [1, 2, 3]
