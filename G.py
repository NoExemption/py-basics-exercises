def bubblesortDown(date):
    length = len(date)
    # **********SPACE**********
    for i in range(0, length):
        for j in range(0, length - i - 1):
            if (date[j] > date[j + 1]):
                t = date[j]
                date[j] = date[j + 1]
                date[j + 1] = t
    m = 0
    if (date[m] == '0'):
        while (date[m] == '0'):
            # **********SPACE**********
            m += 1
        else:
            date[0] = date[m]
            date[m] = '0'
    content = "".join(date)
    return content


def bubblesortUp(date):
    length = len(date)
    for i in range(length - 1):
        for j in range(length - 1, i, -1):
            # **********SPACE**********
            if date[j - 1] > date[j]:
                t = date[j - 1]
                # **********SPACE**********
                date[j - 1] = date[j]
                date[j] = t
    content = "".join(date)
    return content


def diss(a):
    list1 = list(a)
    max = int(bubblesortUp(list1))
    min = int(bubblesortDown(list1))
    dis = max - min
    print("最大数为:{},最小数为:{},差为:{}".format(max, min, dis))


def main():
    num = input("请输入一个正整数：")
    diss(num);


