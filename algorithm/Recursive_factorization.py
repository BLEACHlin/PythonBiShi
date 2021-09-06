"""
递归实现N阶乘
"""


def recuresive_factorization(n):
    if n == 1:
        return 1
    else:
        return recuresive_factorization(n-1) * n


if __name__ == "__main__":
    n = input("请输入想要阶乘的数字：\n")
    n = int(n)
    print(recuresive_factorization(n))
