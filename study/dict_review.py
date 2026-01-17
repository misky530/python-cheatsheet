def main():
    # ===================== Dict 复习 =====================

    # 1) 创建字典 & 取值 / 赋值
    print("创建字典 & 取值/赋值")
    d = {"a": 1, "b": 2, "c": 3}

    print(d["a"])  # 1
    d["d"] = 4  # 新增 key
    d["b"] = 20  # 修改 value
    print(d)  # {'a': 1, 'b': 20, 'c': 3, 'd': 4}

    print("-" * 50)

    # 2) keys / values / items（动态视图）
    print("keys / values / items")
    print("keys:", d.keys())
    print("values:", d.values())
    print("items:", d.items())

    # 视图会“实时反映变化”
    d["e"] = 5
    print("更新后 keys:", d.keys())

    print("-" * 50)

    # 3) get（安全取值）
    print("get")
    print(d.get("a"))  # 1
    print(d.get("not_exist"))  # None
    print(d.get("not_exist", 999))  # 999

    print("-" * 50)

    # 4) setdefault（有就取，没有就写入默认值）
    print("setdefault")
    d2 = {"x": 10}

    print(d2.setdefault("x", 100))  # 10（已有，不修改）
    print(d2)

    print(d2.setdefault("y", 200))  # 200（没有，写入）
    print(d2)

    print("-" * 50)

    # 5) defaultdict（自动默认值）
    print("defaultdict")
    from collections import defaultdict

    # 默认值是 0（int()）
    dd = defaultdict(int)
    dd["a"] += 1
    dd["b"] += 2
    print(dd)  # defaultdict(<class 'int'>, {'a': 1, 'b': 2})

    # 默认值固定为 1
    dd2 = defaultdict(lambda: 1)
    print(dd2["new_key"])  # 1
    print(dd2)

    print("-" * 50)

    # 6) 从集合创建 dict
    print("从集合创建 dict")

    pairs = [("a", 1), ("b", 2), ("c", 3)]
    print(dict(pairs))  # {'a': 1, 'b': 2, 'c': 3}

    keys = ["x", "y", "z"]
    values = [10, 20, 30]
    print(dict(zip(keys, values)))  # {'x': 10, 'y': 20, 'z': 30}

    print(dict.fromkeys(["a", "b", "c"]))  # {'a': None, 'b': None, 'c': None}
    print(dict.fromkeys(["a", "b", "c"], 0))  # {'a': 0, 'b': 0, 'c': 0}

    print("-" * 50)

    # 7) update（合并/覆盖）
    print("update")
    d3 = {"a": 1, "b": 2}
    d3.update({"b": 20, "c": 30})
    print(d3)  # {'a': 1, 'b': 20, 'c': 30}

    print("-" * 50)

    # 8) pop（删除并返回）
    print("pop")
    v = d3.pop("b")
    print("被删除的值:", v)
    print("剩余:", d3)

    print("-" * 50)

    # 9) 字典推导式：按值筛选 key（返回 set）
    print("根据 value 取 key（set）")
    d4 = {"a": 10, "b": 20, "c": 10}
    keys_with_10 = {k for k, v in d4.items() if v == 10}
    print(keys_with_10)  # {'a', 'c'}

    print("-" * 50)

    # 10) 字典推导式：按 key 筛选（返回 dict）
    print("按指定 keys 过滤 dict")
    allowed_keys = {"a", "c"}
    filtered = {k: v for k, v in d4.items() if k in allowed_keys}
    print(filtered)  # {'a': 10, 'c': 10}

    print("-" * 50)

    # 11) Counter（计数器）
    print("Counter")
    from collections import Counter

    counter = Counter(['blue', 'blue', 'blue', 'red', 'red'])
    counter['yellow'] += 1

    print(counter)
    print(counter.most_common())
    # [('blue', 3), ('red', 2), ('yellow', 1)]

    # ===================== Dict 复习结束 =====================

    # 练习 1（高频场景：词频统计）words = ["apple", "banana", "apple", "orange", "banana", "apple"]
    words = ["apple", "banana", "apple", "orange", "banana", "apple"]
    counter = Counter(words)

    print("练习1")
    print(counter)

    # 练习 2（安全取值）user = {"name": "Alice"} 用 get 取 user["age"]，若不存在返回 18
    user = {"name": "Alice"}
    print("练习2")
    user.setdefault("age", 18)
    print(user)

    # 练习 3（过滤字典）scores = {"math": 90, "english": 70, "physics": 85, "chemistry": 60}
    # allowed = {"math", "physics"}
    # 用字典推导式得到：只保留 allowed 里的 key
    scores = {"math": 90, "english": 70, "physics": 85, "chemistry": 60}
    allowed = {"math", "physics"}

    print("练习3")
    filtered = {k: v for k, v in scores.items() if k in allowed}
    print(filtered)


# PyCharm / 标准 Python 入口
if __name__ == "__main__":
    main()
