"""
冒泡排序：比较相邻两个数据，前一个数比后一个数大则交换位置，直到最大的数字放置到最后面（升序）
时间复杂度：O(n²)
"""


def sort_bubbling():
    input_str = input("请输入想要排序的数字,回车结束输入")
    list_str = (input_str.split(','))
    list_num = [int(i) for i in list_str]

    for i in range(len(list_num)):
        for j in range(len(list_num) - i - 1):
            if list_num[j] > list_num[j+1]:
                list_num[j], list_num[j+1] = list_num[j+1], list_num[j]
    print(f'排序后的数字数组：{list_num}')


if __name__ == "__main__":
    sort_bubbling()
