l = [4,5,6,1,2,1,3,7]
# 四种常见的排序
#1.冒泡排序
# 冒泡排序是最常见到的排序算法，也是很基础的一种排序算法。它的实现思想是：相邻的两个元素进行比较，然后把较大的元素放到后面（正向排序），在一轮比较完后最大的元素就放在了最后一个位置，像鱼儿在水中吐的气泡在上升的过程中不断变大
def bubble_sort(list):
    count = len(list)
    for i in range(count):
        for j in range(i + 1, count):
            if list[i] > list[j]:
                list[i], list[j] = list[j], list[i]
    return list
# print(bubble_sort(l))

# 2.选择排序
# 选择排序的思路是：第一轮的时候，所有的元素都和第一个元素进行比较，如果比第一个元素大，就和第一个元素进行交换，在这轮比较完后，就找到了最小的元素；第二轮的时候所有的元素都和第二个元素进行比较找出第二个位置的元素，以此类推。
def selection_sort(arr):
    """选择排序"""
    # 第一层for表示循环选择的遍数
    for i in range(len(arr) - 1):
        # 将起始元素设为最小元素
        min_index = i
        # 第二层for表示最小元素和后面的元素逐个比较
        for j in range(i + 1, len(arr)):
            if arr[j] < arr[min_index]:
                # 如果当前元素比最小元素小，则把当前元素角标记为最小元素角标
                min_index = j
        # 查找一遍后将最小元素与起始元素互换
        arr[min_index], arr[i] = arr[i], arr[min_index]
    return arr

# print(selection_sort(l))
# 3.插入排序
# 插入排序的思想是将一个数据插入到已经排好序的有序数据中，从而得到一个新的、个数加一的有序数据，算法适用于少量数据的排序，时间复杂度为O(n^2)。 是稳定的排序方法。插入算法把要排序的数组分成两部分：第一部分包含了这个数组的所有元素，但将最后一个元素除外（让数组多一个空间才有插入的位置）， 而第二部分就只包含这一个元素（即待插入元素）。在第一部分排序完成后，再将这个最后元素插入到已排好序的第一部分中
def insert_sort(list):
    count = len(list)
    for i in range(1, count):
        key = list[i]
        j = i - 1
        while j >= 0:
            if list[j] > key:
                list[j + 1] = list[j]
                list[j] = key
            j -= 1
    return list
# print(insert_sort(l))

# 4.快速排序
def quick_sort(data):
    """quick_sort"""
    if len(data) >= 2:
        mid = data[len(data)//2]
        left,right = [], []
        data.remove(mid)
        for num in data:
            if num >= mid:
                right.append(num)
            else:
                left.append(num)
        return quick_sort(left) + [mid] + quick_sort(right)
    else:
        return data
print(quick_sort(l))