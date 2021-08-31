"""
希尔排序：先将整个待排序的记录序列分割成为若干子序列分别进行直接插入排序，待整个序列中的记录"基本有序"时，
再对全体记录进行依次直接插入排序
时间复杂度：O(nlog2n)
"""
import math

def shell_sort():
    input_str = input("请输入排序的数据，逗号分隔，回车结束")
    str_list = input_str.split(",")
    num_list = [int(i) for i in str_list]

    gap = 1
    while (gap < len(num_list)/3):
        gap = gap * 3 + 1
    while gap > 0:
        for i in range(gap, len(num_list)):
            temp = num_list[i]
            j = i - gap
            while j >= 0 and num_list[j] > temp:
                num_list[j+gap] = num_list[j]
                j -= gap
            num_list[j+gap] = temp
        gap = math.floor(gap/3)
    print(f"排序后的序列：{num_list}")


if __name__ == "__main__":
    shell_sort()







