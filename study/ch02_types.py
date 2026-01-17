def main():
    # ===================== Types 复习 =====================

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
    print("strip:", s.strip())
    print("split:", "a,b,c".split(","))
    print("join:", "-".join(["a", "b", "c"]))
    print("startswith:", "Hello".startswith("He"))
    print("replace:", s.replace("Python", "World").strip())

    print("-" * 50)

    # 3) Regular_Exp（findall / search / group）
    print("Regular_Exp")
    import re
    text = "Order: #A-1024, #B-7, #C-999"
    pairs = re.findall(r"#([A-Z])-(\d+)", text)
    print(pairs)
    m = re.search(r"#B-(\d+)", text)
    print(m.group(1) if m else None)

    print("-" * 50)

    # 4) Format（f-string / format spec）
    print("Format")
    name = "Alice"
    score = 93.4567
    print(f"{name} score is {score:.2f}")
    print(f"{42:05d}")
    print(format(255, "x"))

    print("-" * 50)

    # 5) Numbers（浮点精度 / Decimal）
    print("Numbers")
    print("0.1 + 0.2 =", 0.1 + 0.2)
    from decimal import Decimal
    print("Decimal:", Decimal("0.1") + Decimal("0.2"))

    print("-" * 50)

    # 6) Combinatorics（排列组合）
    print("Combinatorics")
    import itertools
    arr = [1, 2, 3]
    print("permutations(2):", list(itertools.permutations(arr, 2)))
    print("combinations(2):", list(itertools.combinations(arr, 2)))
    print("product sample:", list(itertools.product([0, 1], repeat=3))[:5], "...")

    print("-" * 50)

    # 7) Datetime（now / timedelta / strptime）
    print("Datetime")
    from datetime import datetime, timedelta, timezone
    now = datetime.now(timezone(timedelta(hours=8)))
    print("now(+08):", now.isoformat())
    print("tomorrow:", (now + timedelta(days=1)).strftime("%Y-%m-%d %H:%M:%S"))
    parsed = datetime.strptime("2026-01-17 16:30:00", "%Y-%m-%d %H:%M:%S")
    print("parsed:", parsed)

    # ===================== Types 复习结束 =====================

    # 练习 1
    print("练习1")
    text = "Order: #A-1024, #B-7, #C-999"
    nums = [int(n) for _, n in re.findall(r"#([A-Z])-(\d+)", text)]
    print(nums)

    # 练习 2
    print("练习2")
    raw = "anthony cai"
    titled = " ".join(w.capitalize() for w in raw.split())
    print(titled)

    # 练习 3
    print("练习3")
    v = 12.34567
    print(f"{v:.2f}")

    # 练习 4
    print("练习4")
    print(str(Decimal("0.1") + Decimal("0.2")))

    # 练习 5
    print("练习5")
    d1 = datetime.strptime("2026-01-01", "%Y-%m-%d")
    d2 = datetime.strptime("2026-01-17", "%Y-%m-%d")
    print((d2 - d1).days)


if __name__ == "__main__":
    main()
