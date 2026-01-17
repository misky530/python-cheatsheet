def main():
    # ===================== Functions 复习 =====================

    # 1) 最基本的函数定义与调用
    print("1) 基本函数")

    def add(a, b):
        return a + b

    result = add(2, 3)
    print(result)   # 5

    print("-" * 50)

    # 2) return 的本质（函数一旦 return 就结束）
    print("2) return 行为")

    def check_number(x):
        if x > 0:
            return "positive"
        return "non-positive"

    print(check_number(10))
    print(check_number(-1))

    print("-" * 50)

    # 3) 默认参数
    print("3) 默认参数")

    def greet(name, msg="Hello"):
        return f"{msg}, {name}"

    print(greet("Alice"))
    print(greet("Bob", "Hi"))

    print("-" * 50)

    # 4) 可变参数 *args
    print("4) *args")

    def sum_all(*args):
        total = 0
        for x in args:
            total += x
        return total

    print(sum_all(1, 2, 3))
    print(sum_all(1, 2, 3, 4, 5))

    print("-" * 50)

    # 5) 关键字参数 **kwargs
    print("5) **kwargs")

    def print_user(**kwargs):
        for k, v in kwargs.items():
            print(k, "=", v)

    print_user(name="Alice", age=18, city="Beijing")

    print("-" * 50)

    # 6) *args + **kwargs 同时使用
    print("6) *args + **kwargs")

    def demo(a, b, *args, **kwargs):
        print("a =", a)
        print("b =", b)
        print("args =", args)
        print("kwargs =", kwargs)

    demo(1, 2, 3, 4, x=10, y=20)

    print("-" * 50)

    # 7) 函数作为参数（非常重要）
    print("7) 函数作为参数")

    def apply(func, x, y):
        return func(x, y)

    print(apply(add, 3, 4))   # 7

    print("-" * 50)

    # 8) lambda（匿名函数）
    print("8) lambda")

    add_inline = lambda x, y: x + y
    print(add_inline(5, 6))

    nums = [1, 2, 3, 4]
    squared = list(map(lambda x: x * x, nums))
    print(squared)

    print("-" * 50)

    # 9) 返回多个值（本质是 tuple）
    print("9) 返回多个值")

    def min_max(nums):
        return min(nums), max(nums)

    mn, mx = min_max([3, 1, 9, 2])
    print(mn, mx)

    print("-" * 50)

    # ===================== Functions 复习结束 =====================


if __name__ == "__main__":
    main()
