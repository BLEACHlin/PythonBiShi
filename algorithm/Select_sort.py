"""
选择排序：每次选出为排序序列中最小的数的，放置在序列的最前面，再选出第二小的数，放置在已排序序列的后面。。。
时间复杂度： O(n²)
"""


def select_sort():
    str_input = input("请输入要排序的数字，逗号分开，回车结束")
    str_list = str_input.split(",")
    num_list = [int(i) for i in str_list]

    for i in range(len(num_list) - 1):
        index = i
        for j in range(i+1, len(num_list)):
            if num_list[index] > num_list[j]:
                index = j   # 每次选出最小的数

        # 最小的数排在最前面
        num_list[i], num_list[index] = num_list[index], num_list[i]
    print(f'排序后的数组：{num_list}')


if __name__ == "__main__":
    select_sort()
