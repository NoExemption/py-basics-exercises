import random
num = random.randint(1,10)
guess_num = int(input("输入你猜的数字"))
if guess_num == num:
    print("恭喜，第一次就中了")
else:
    if guess_num > num:
        print("你猜测的数字大了")
    else:
        print("你猜测的数字小了")
    guess_num = int(input("再次输入你猜测的数字"))
    if guess_num == num:
        print("恭喜，第二次中了")
    else:
        if guess_num > num:
            print("你猜测的数字大了")
        else:
            print("你猜测的数字小了")
        guess_num = int(input("最后输入你猜测的数字"))
        if guess_num == num:
            print("恭喜，第三次中了")
        else:
            print("三次机会用完了，你没能猜中")