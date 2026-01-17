def main():
    # ===================== Data 复习 =====================

    # 1) JSON
    print("JSON")
    import json
    obj = {"name": "Alice", "age": 18, "tags": ["python", "cli"], "active": True}
    s = json.dumps(obj, ensure_ascii=False)
    print(s)
    back = json.loads(s)
    print(back)

    print("-" * 50)

    # 2) Pickle
    print("Pickle")
    import pickle
    blob = pickle.dumps(obj)
    obj2 = pickle.loads(blob)
    print(obj2)

    print("-" * 50)

    # 3) CSV
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

    # 4) SQLite
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

    # 5) Bytes
    print("Bytes")
    b = "你好".encode("utf-8")
    print(b)
    print(b.decode("utf-8"))

    print("-" * 50)

    # 6) Struct
    print("Struct")
    import struct
    packed = struct.pack(">Ih", 65535, -7)
    print(packed)
    print(struct.unpack(">Ih", packed))

    print("-" * 50)

    # 7) Array
    print("Array")
    from array import array
    arr = array("i", [1, 2, 3])
    arr.append(4)
    print(arr, arr.tolist())

    print("-" * 50)

    # 8) Memory_View
    print("Memory_View")
    data = bytearray(b"abcdef")
    mv = memoryview(data)
    print(bytes(mv[1:4]))
    mv[2] = ord("Z")
    print(data)

    print("-" * 50)

    # 9) Deque
    print("Deque")
    from collections import deque
    dq = deque([1, 2, 3])
    dq.appendleft(0)
    dq.append(4)
    print(dq)
    print("popleft:", dq.popleft())
    print("pop:", dq.pop())
    print("dq now:", dq)

    # ===================== Data 复习结束 =====================

    # 练习 1
    print("练习1")
    import json
    obj = {"name": "Alice", "age": 18, "tags": ["python", "cli"], "active": True}
    s = json.dumps(obj, ensure_ascii=False)
    back = json.loads(s)
    print(back["tags"])

    # 练习 2
    print("练习2")
    rows = [{"name": "alice", "score": "90"}, {"name": "bob", "score": "80"}]
    score_map = {r["name"]: int(r["score"]) for r in rows}
    print(score_map)

    # 练习 3
    print("练习3")
    import sqlite3
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

    # 练习 4
    print("练习4")
    from collections import deque
    dq = deque(maxlen=3)
    for x in [10, 11, 12, 13, 14]:
        dq.append(x)
        print(list(dq))

    # 练习 5
    print("练习5")
    import struct
    fmt = ">HhB"
    pkt = struct.pack(fmt, 500, -12, 255)
    out = struct.unpack(fmt, pkt)
    print(out)


if __name__ == "__main__":
    main()
