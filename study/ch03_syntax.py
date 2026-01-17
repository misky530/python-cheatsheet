def main():
    # ===================== Syntax 复习 =====================

    # 1) Function
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

    # 2) Inline
    print("Inline")
    add = lambda a, b: a + b
    x = 10
    label = "big" if x > 5 else "small"
    print(add(2, 3))
    print(label)

    print("-" * 50)

    # 3) Import
    print("Import")
    import math as m
    print(m.sqrt(16))

    print("-" * 50)

    # 4) Decorator
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

    # 5) Class
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

    # 6) Duck_Type
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

    # 7) Enum
    print("Enum")
    from enum import Enum

    class Env(Enum):
        DEV = "dev"
        PROD = "prod"

    env = Env.DEV
    print(env, env.value)

    print("-" * 50)

    # 8) Except
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

    # ===================== Syntax 复习结束 =====================

    # 练习 1
    print("练习1")
    from functools import wraps

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

    # 练习 2
    print("练习2")

    def safe_int(s):
        try:
            return int(s)
        except ValueError:
            return None

    print(safe_int("123"))
    print(safe_int("x"))

    # 练习 3
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

    # 练习 4
    print("练习4")
    words = ["banana", "fig", "apple", "kiwi"]
    print(sorted(words, key=lambda x: len(x)))

    # 练习 5
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


if __name__ == "__main__":
    main()
