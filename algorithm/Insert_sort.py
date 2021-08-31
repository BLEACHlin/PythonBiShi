"""
插入排序，将第一待排序序列第一个元素看做一个有序序列，把第二个元素到最后一个元素当成是未排序序列。
从头到尾依次扫描未排序序列，将扫描到的每个元素插入有序序列的适当位置。
（如果待插入的元素与有序序列中的某个元素相等，则将待插入元素插入到相等元素的后面。）
插入排序一般来说是低效的，因为插入排序每次只能将数据移动一位
时间复杂度：O(n2)

11 21 33 9
i=0  preIndex=-1 current=11 arr[0]=11
i=1 preIndex=0   current=21 arr[1]=21
i=2 preIndex=1 current=33 arr[2] = 33
    i=3 preIndex=2 current=9  arr[3] = 33 preIndex = 1
    i=3 preIndex=1 current=9  arr[2] = 21 preIndex =0
    i=3 preIndex=0 current=9  arr[1] = 11 preIndex = -1
arr[0] = 9
"""


def insert_sort():
    str_num = input("请输入要排序的序列，逗号隔开，回车结束")
    str_list = str_num.split(",")
    num_list = [int(i) for i in str_list]
    for i in range(len(num_list)):
        index = i - 1
        current = num_list[i]
        while index >= 0 and num_list[index] > current:
            num_list[index + 1] = num_list[index]
            index -= 1
        num_list[index+1] = current
    print(f"排序后的序列：{num_list}")


if __name__ == "__main__":
    insert_sort()