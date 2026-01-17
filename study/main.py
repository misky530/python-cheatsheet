def main():
    print("Hello World")

    list_a = [1, 2, 3, 4]

    print(list_a[0])  # 第一个元素
    print(list_a[-1])  # 最后一个元素

    list_a[1] = 99  # 修改第二个元素
    print(list_a)

    # slice
    list_a = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

    print(list_a[2:7])  # 从 index 2 到 6
    print(list_a[:5])  # 前 5 个
    print(list_a[::2])  # 每隔 2 个取一个
    print(list_a[::-1])  # 反转

    # append vs extend
    print("append vs extend")
    a = [1, 2, 3]

    a.append(4)
    print(a)  # [1,2,3,4]

    a.extend([5, 6, 7])
    print(a)  # [1,2,3,4,5,6,7]

    # sort vs sorted
    print("sort vs sorted")
    a = [3, 1, 4, 2]

    a.sort()  # 原地排序
    print(a)

    b = [3, 1, 4, 2]
    c = sorted(b)  # 返回新列表
    print(b)  # 原列表不变
    print(c)  # 新的排序结果

    # reversed
    print("reversed")
    a = [3, 1, 4, 2]
    a.sort()
    a = [1, 2, 3, 4]
    r = reversed(a)

    print(r)  # 这是一个迭代器
    print(list(r))  # 转成列表

    # max / sum
    print("max / sum")
    nums = [1, 5, 3, 10]

    print(max(nums))
    print(sum(nums))

    # elementwise_sum（逐元素求和）
    print("elementwise_sum（逐元素求和）")
    list_a = [1, 2, 3]
    list_b = [10, 20, 30]

    elementwise_sum = [sum(pair) for pair in zip(list_a, list_b)]
    print(elementwise_sum)  # [11, 22, 33]

    # sorted + key
    print("sorted + key")
    pairs = [(1, 5), (3, 2), (2, 8)]

    # 按第二个元素排序
    print(sorted(pairs, key=lambda el: el[1]))

    # 先按第二个，再按第一个排序
    print(sorted(pairs, key=lambda el: (el[1], el[0])))

    # 展平嵌套列表（flatten）
    print("展平嵌套列表（flatten）")
    import itertools

    nested = [[1, 2], [3, 4], [5]]
    flat = list(itertools.chain.from_iterable(nested))

    print(flat)  # [1,2,3,4,5]

    # 练习 1 把 [1,2,3] 和 [10,20,30] 逐元素相乘
    list_a = [1, 2, 3]
    list_b = [10, 20, 30]
    # list_c = []
    # for i in range(3):
    #     # print(list_a[i])
    #     # print(list_b[i])
    #     list_c.append(list_a[i] * list_b[i])

    # improve
    list_c = [a*b for a,b in zip(list_a, list_b)]
    print(list_c)

    # 练习 2 对列表 [5,2,9,1]： 生成一个新列表，元素都加 10  再按降序排序
    list_a = [5, 2, 9, 1]

    # list_res = []
    # for item in list_re:
    #     list_res.append(item + 10)
    list_res=[ x+10 for x in list_a]
    list_res.sort(reverse=True)

    print('练习2：')
    print(list(list_res))

    #  练习3 把下面嵌套列表展平成一维： data = [[1], [2,3], [4,5,6]]
    data = [[1], [2, 3], [4, 5, 6]]
    flat = itertools.chain.from_iterable(data)
    print(list(flat))


if __name__ == "__main__":
    main()
