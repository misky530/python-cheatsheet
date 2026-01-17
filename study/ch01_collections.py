def main():
    # ===================== Collections 复习 =====================

    # 1) Set（集合：去重 / 运算）
    print("Set")
    s = {1, 2, 2, 3}
    print(s)  # {1,2,3}

    a = {1, 2, 3}
    b = {3, 4, 5}
    print("union:", a | b)
    print("intersection:", a & b)
    print("difference:", a - b)
    print("sym diff:", a ^ b)

    print("-" * 50)

    # 2) Tuple（元组：不可变 / 解包 / 单元素）
    print("Tuple")
    t = ("alice", 18, "SG")
    name, age, city = t
    print("t:", t)
    print("unpacked:", name, age, city)

    single = (42,)  # 单元素 tuple 必须带逗号
    print("single:", single, type(single))

    print("-" * 50)

    # 3) Range（范围：惰性序列 / membership）
    print("Range")
    r = range(2, 10, 2)
    print("r:", r)
    print("list(r):", list(r))
    print("6 in r?:", 6 in r)

    print("-" * 50)

    # 4) Enumerate（枚举：索引 + 值）
    print("Enumerate")
    items = ["a", "b", "c"]
    for i, v in enumerate(items, start=0):
        print(i, v)

    print("-" * 50)

    # 5) Iterator（迭代器：iter/next/StopIteration）
    print("Iterator")
    it = iter([10, 20, 30])
    print(next(it))
    print(next(it))
    print(next(it))
    try:
        print(next(it))
    except StopIteration:
        print("StopIteration raised")

    print("-" * 50)

    # 6) Generator（生成器：yield）
    print("Generator")

    def countdown(n):
        while n > 0:
            yield n
            n -= 1

    gen = countdown(3)
    print("list(gen):", list(gen))  # [3,2,1]

    # ===================== Collections 复习结束 =====================

    # 练习 1（去重但保持顺序）nums = [1,2,2,3,1,4] -> [1,2,3,4]
    print("练习1")
    nums = [1, 2, 2, 3, 1, 4]
    dedup = []
    seen = set()
    for x in nums:
        if x not in seen:
            dedup.append(x)
            seen.add(x)
    print(dedup)

    # 练习 2（enumerate 找索引）items = ["a","b","c","b","b"] -> [1,3,4]
    print("练习2")
    items2 = ["a", "b", "c", "b", "b"]
    idxs = [i for i, v in enumerate(items2) if v == "b"]
    print(idxs)

    # 练习 3（集合：找共同元素）A,B 的交集
    print("练习3")
    A = {"cpu", "ram", "disk", "nic"}
    B = {"ram", "disk", "gpu"}
    print(A & B)

    # 练习 4（range：生成等差数列）生成 1..20 中所有 3 的倍数
    print("练习4")
    print(list(range(3, 21, 3)))

    # 练习 5（生成器：过滤偶数）写 gen_even(nums) 只 yield 偶数
    print("练习5")

    def gen_even(seq):
        for x in seq:
            if x % 2 == 0:
                yield x

    print(list(gen_even([1, 2, 3, 4, 5, 6])))


if __name__ == "__main__":
    main()
