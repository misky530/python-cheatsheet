def main():
    # ===================== 1. Collections 复习 =====================

    # 1) Set（去重 / 集合运算）
    print("Set")
    s = {1, 2, 2, 3}
    print("s:", s)  # {1,2,3}

    a = {1, 2, 3}
    b = {3, 4, 5}
    print("union:", a | b)          # 并集
    print("intersection:", a & b)   # 交集
    print("difference:", a - b)     # 差集
    print("sym diff:", a ^ b)       # 对称差

    print("-" * 50)

    # 2) Tuple（不可变 / 解包 / 单元素）
    print("Tuple")
    t = ("alice", 18, "SG")
    name, age, city = t
    print("t:", t)
    print("unpacked:", name, age, city)

    single = (42,)  # 单元素 tuple 必须带逗号
    print("single:", single, type(single))

    print("-" * 50)

    # 3) Range（惰性序列 / membership）
    print("Range")
    r = range(2, 10, 2)
    print("r:", r)
    print("list(r):", list(r))
    print("6 in r?:", 6 in r)

    print("-" * 50)

    # 4) Enumerate（索引+值）
    print("Enumerate")
    items = ["a", "b", "c"]
    for i, v in enumerate(items, start=0):
        print(i, v)

    print("-" * 50)

    # 5) Iterator（iter/next/StopIteration）
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

    # 6) Generator（yield）
    print("Generator")

    def countdown(n):
        while n > 0:
            yield n
            n -= 1

    gen = countdown(3)
    print("list(gen):", list(gen))  # [3,2,1]

    # ===================== 1. Collections 复习结束 =====================

    # 练习 1（去重但保持顺序）nums = [1,2,2,3,1,4] -> [1,2,3,4]
    print("练习1")
    nums = [1, 2, 2, 3, 1, 4]
    seen = set()
    dedup = []
    for x in nums:
        if x not in seen:
            dedup.append(x)
            seen.add(x)
    print(dedup)

    # 练习 2（enumerate 找索引）items = ["a","b","c","b","b"] -> [1,3,4]
    print("练习2")
    items = ["a", "b", "c", "b", "b"]
    idxs = [i for i, v in enumerate(items) if v == "b"]
    print(idxs)

    # 练习 3（集合运算应用）找出“只在 A 或只在 B”的元素（对称差）
    print("练习3")
    A = {1, 2, 3, 9}
    B = {3, 4, 5, 9, 10}
    print(A ^ B)

    # 练习 4（range 切片感）生成 1..20 中所有 3 的倍数
    print("练习4")
    multiples = list(range(3, 21, 3))
    print(multiples)

    # 练习 5（生成器：按需产出平方）squares(6) -> 0,1,4,9,16,25
    print("练习5")

    def squares(n):
        for i in range(n):
            yield i * i

    print(list(squares(6)))

    # ===================== 2. Types 复习 =====================

    # 1) Type（type / isinstance）
    print("Type")
    x = 123
    print(type(x))
    print(isinstance(x, int))
    print(isinstance(x, bool))  # False

    print("-" * 50)

    # 2) String（strip / split / join / replace / startswith）
    print("String")
    s = "  Hello, Python  "
    print(s.strip())
    print("a,b,c".split(","))
    print("-".join(["a", "b", "c"]))
    print("Hello".startswith("He"))
    print(s.replace("Python", "World").strip())

    print("-" * 50)

    # 3) Regular_Exp（findall / search / group）
    print("Regular_Exp")
    import re

    text = "Order: #A-1024, #B-7, #C-999"
    pairs = re.findall(r"#([A-Z])-(\d+)", text)
    print(pairs)  # [('A','1024'),...]
    m = re.search(r"#B-(\d+)", text)
    print(m.group(1) if m else None)

    print("-" * 50)

    # 4) Format（f-string / format spec）
    print("Format")
    name = "Alice"
    score = 93.4567
    print(f"{name} score is {score:.2f}")
    print(f"{42:05d}")          # 00042
    print(format(255, "x"))     # ff

    print("-" * 50)

    # 5) Numbers（浮点精度 / Decimal）
    print("Numbers")
    print(0.1 + 0.2)  # 0.30000000000000004
    from decimal import Decimal
    print(Decimal("0.1") + Decimal("0.2"))  # 0.3

    print("-" * 50)

    # 6) Combinatorics（排列组合）
    print("Combinatorics")
    import itertools

    arr = [1, 2, 3]
    print(list(itertools.permutations(arr, 2)))
    print(list(itertools.combinations(arr, 2)))
    print(list(itertools.product([0, 1], repeat=3))[:5], "...")

    print("-" * 50)

    # 7) Datetime（now / timedelta / strptime）
    print("Datetime")
    from datetime import datetime, timedelta, timezone
    now = datetime.now(timezone(timedelta(hours=8)))
    print("now(+08):", now.isoformat())
    print("tomorrow:", (now + timedelta(days=1)).strftime("%Y-%m-%d %H:%M:%S"))
    parsed = datetime.strptime("2026-01-17 16:30:00", "%Y-%m-%d %H:%M:%S")
    print("parsed:", parsed)

    # ===================== 2. Types 复习结束 =====================

    # 练习 1（正则提取数字）"Order: #A-1024, #B-7, #C-999" -> [1024, 7, 999]
    print("练习1")
    text = "Order: #A-1024, #B-7, #C-999"
    nums = [int(n) for _, n in re.findall(r"#([A-Z])-(\d+)", text)]
    print(nums)

    # 练习 2（字符串标题化）"anthony cai" -> "Anthony Cai"
    print("练习2")
    raw = "anthony cai"
    titled = " ".join(w.capitalize() for w in raw.split())
    print(titled)

    # 练习 3（格式化）把 12.34567 输出为 "12.35"
    print("练习3")
    v = 12.34567
    print(f"{v:.2f}")

    # 练习 4（排列组合）从 [1,2,3,4] 中取 2 个组合（不关顺序）
    print("练习4")
    print(list(itertools.combinations([1, 2, 3, 4], 2)))

    # 练习 5（日期差）2026-01-01 到 2026-01-17 差几天
    print("练习5")
    d1 = datetime.strptime("2026-01-01", "%Y-%m-%d")
    d2 = datetime.strptime("2026-01-17", "%Y-%m-%d")
    print((d2 - d1).days)

    # ===================== 3. Syntax 复习 =====================

    # 1) Function（默认参数 / *args / **kwargs）
    print("Function")

    def greet(name, title="Mr.", *tags, **meta):
        msg = f"Hello {title} {name}"
        if tags:
            msg += " | tags=" + ",".join(tags)
        if meta:
            msg += " | meta=" + ",".join(f"{k}={v}" for k, v in meta.items())
        return msg

    print(greet("Anthony"))
    print(greet("Anthony", "Dr.", "vip", "python", city="SG"))

    print("-" * 50)

    # 2) Inline（lambda / 三元表达式）
    print("Inline")
    add = lambda a, b: a + b
    x = 10
    label = "big" if x > 5 else "small"
    print(add(2, 3))
    print(label)

    print("-" * 50)

    # 3) Import（as 别名）
    print("Import")
    import math as m
    print(m.sqrt(16))

    print("-" * 50)

    # 4) Decorator（计时装饰器）
    print("Decorator")
    import time
    from functools import wraps

    def timer(fn):
        @wraps(fn)
        def wrapper(*args, **kwargs):
            start = time.perf_counter()
            out = fn(*args, **kwargs)
            cost_ms = (time.perf_counter() - start) * 1000
            print(f"[timer] {fn.__name__} took {cost_ms:.2f} ms")
            return out
        return wrapper

    @timer
    def slow_sum(n):
        return sum(range(n))

    print(slow_sum(200000))

    print("-" * 50)

    # 5) Class（类 / 实例 / 方法 / 属性）
    print("Class")

    class CounterBox:
        def __init__(self):
            self.count = 0

        def inc(self, step=1):
            self.count += step
            return self.count

    box = CounterBox()
    print(box.inc())
    print(box.inc(5))
    print(box.count)

    print("-" * 50)

    # 6) Duck_Type（鸭子类型：看行为不看类型）
    print("Duck_Type")

    class Duck:
        def quack(self):
            return "quack"

    class Person:
        def quack(self):
            return "I can imitate duck"

    def make_quack(x):
        return x.quack()

    print(make_quack(Duck()))
    print(make_quack(Person()))

    print("-" * 50)

    # 7) Enum（枚举）
    print("Enum")
    from enum import Enum

    class Env(Enum):
        DEV = "dev"
        PROD = "prod"

    env = Env.DEV
    print(env, env.value)

    print("-" * 50)

    # 8) Except（try/except/else/finally）
    print("Except")

    def safe_div(a, b):
        try:
            return a / b
        except ZeroDivisionError:
            return None
        except TypeError:
            return None

    print(safe_div(10, 2))
    print(safe_div(10, 0))
    print(safe_div(10, "x"))

    # ===================== 3. Syntax 复习结束 =====================

    # 练习 1（装饰器：打印返回值）show_return 装饰后：打印并原样返回
    print("练习1")
    def show_return(fn):
        @wraps(fn)
        def wrapper(*args, **kwargs):
            ret = fn(*args, **kwargs)
            print(f"[return] {fn.__name__} -> {ret}")
            return ret
        return wrapper

    @show_return
    def mul(a, b):
        return a * b

    mul(3, 4)

    # 练习 2（异常：安全转 int）safe_int("123")->123, safe_int("x")->None
    print("练习2")
    def safe_int(s):
        try:
            return int(s)
        except ValueError:
            return None

    print(safe_int("123"))
    print(safe_int("x"))

    # 练习 3（类：余额不能为负）BankAccount deposit/withdraw
    print("练习3")
    class BankAccount:
        def __init__(self, balance=0):
            self.balance = balance

        def deposit(self, amount):
            if amount < 0:
                raise ValueError("amount must be >= 0")
            self.balance += amount
            return self.balance

        def withdraw(self, amount):
            if amount < 0:
                raise ValueError("amount must be >= 0")
            if self.balance - amount < 0:
                raise ValueError("insufficient funds")
            self.balance -= amount
            return self.balance

    acc = BankAccount(100)
    print("deposit:", acc.deposit(50))
    try:
        print("withdraw:", acc.withdraw(999))
    except ValueError as e:
        print("withdraw error:", e)

    # 练习 4（lambda + sort）按字符串长度排序
    print("练习4")
    words = ["banana", "fig", "apple", "kiwi"]
    words_sorted = sorted(words, key=lambda x: len(x))
    print(words_sorted)

    # 练习 5（duck typing）写一个函数 speak(x)：只要 x 有 speak() 方法就能用
    print("练习5")
    class Cat:
        def speak(self):
            return "meow"

    class Robot:
        def speak(self):
            return "beep"

    def speak(x):
        return x.speak()

    print(speak(Cat()))
    print(speak(Robot()))

    # ===================== 5. Data 复习 =====================

    # 1) JSON（dumps / loads）
    print("JSON")
    import json
    obj = {"name": "Alice", "age": 18, "tags": ["python", "cli"], "active": True}
    s = json.dumps(obj, ensure_ascii=False)
    print(s)
    back = json.loads(s)
    print(back)

    print("-" * 50)

    # 2) Pickle（⚠️ 只对可信数据使用）
    print("Pickle")
    import pickle
    blob = pickle.dumps(obj)
    obj2 = pickle.loads(blob)
    print(obj2)

    print("-" * 50)

    # 3) CSV（内存读写）
    print("CSV")
    import csv
    import io

    buf = io.StringIO()
    w = csv.writer(buf)
    w.writerow(["name", "score"])
    w.writerow(["alice", 90])
    w.writerow(["bob", 80])
    content = buf.getvalue()
    print(content.strip())

    buf2 = io.StringIO(content)
    r = csv.DictReader(buf2)
    rows = list(r)
    print(rows)

    print("-" * 50)

    # 4) SQLite（:memory: + 参数化查询）
    print("SQLite")
    import sqlite3
    conn = sqlite3.connect(":memory:")
    cur = conn.cursor()
    cur.execute("create table user(name text, age int)")
    cur.execute("insert into user values (?, ?)", ("alice", 18))
    cur.execute("insert into user values (?, ?)", ("bob", 20))
    conn.commit()
    cur.execute("select name, age from user where age >= ?", (19,))
    print(cur.fetchall())
    conn.close()

    print("-" * 50)

    # 5) Bytes（encode/decode）
    print("Bytes")
    b = "你好".encode("utf-8")
    print(b)
    print(b.decode("utf-8"))

    print("-" * 50)

    # 6) Struct（pack/unpack）
    print("Struct")
    import struct
    packed = struct.pack(">Ih", 65535, -7)  # uint32 + int16
    print(packed)
    print(struct.unpack(">Ih", packed))

    print("-" * 50)

    # 7) Array（紧凑数值数组）
    print("Array")
    from array import array
    arr = array("i", [1, 2, 3])
    arr.append(4)
    print(arr, arr.tolist())

    print("-" * 50)

    # 8) Memory_View（零拷贝视图）
    print("Memory_View")
    data = bytearray(b"abcdef")
    mv = memoryview(data)
    print(bytes(mv[1:4]))
    mv[2] = ord("Z")
    print(data)

    print("-" * 50)

    # 9) Deque（双端队列）
    print("Deque")
    from collections import deque
    dq = deque([1, 2, 3])
    dq.appendleft(0)
    dq.append(4)
    print(dq)
    print("popleft:", dq.popleft())
    print("pop:", dq.pop())
    print("dq now:", dq)

    # ===================== 5. Data 复习结束 =====================

    # 练习 1（JSON 文件感）把 obj dumps 成字符串，再 loads 回来，取出 tags
    print("练习1")
    obj = {"name": "Alice", "age": 18, "tags": ["python", "cli"], "active": True}
    s = json.dumps(obj, ensure_ascii=False)
    back = json.loads(s)
    print(back["tags"])

    # 练习 2（CSV -> dict）rows = [{'name':'alice','score':'90'}...] -> {name:int(score)}
    print("练习2")
    rows = [{"name": "alice", "score": "90"}, {"name": "bob", "score": "80"}]
    score_map = {r["name"]: int(r["score"]) for r in rows}
    print(score_map)

    # 练习 3（SQLite group by）统计每个 tag 的 sum(val)
    print("练习3")
    conn = sqlite3.connect(":memory:")
    cur = conn.cursor()
    cur.execute("create table meter(tag text, val int)")
    cur.executemany(
        "insert into meter values (?, ?)",
        [("peak", 10), ("peak", 5), ("valley", 3), ("flat", 7), ("valley", 2)]
    )
    conn.commit()
    cur.execute("select tag, sum(val) from meter group by tag order by tag")
    print(cur.fetchall())
    conn.close()

    # 练习 4（deque 窗口）deque(maxlen=3) 依次 append 10..14，打印窗口变化
    print("练习4")
    dq = deque(maxlen=3)
    for x in [10, 11, 12, 13, 14]:
        dq.append(x)
        print(list(dq))

    # 练习 5（struct 自定义报文）fmt=">HhB" pack 再 unpack，验证一致
    print("练习5")
    fmt = ">HhB"  # uint16, int16, uint8
    pkt = struct.pack(fmt, 500, -12, 255)
    out = struct.unpack(fmt, pkt)
    print(out)


# PyCharm / 标准 Python 入口
if __name__ == "__main__":
    main()
