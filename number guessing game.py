#项目 猜数字
import random
import time
print("猜数字游戏")
time.sleep(1)
print("1-简单 2-中等 3-困难")
time.sleep(1)
level=int(input("请输入你选择的难度："))
if level==1:
    max_num=50
    chance=10
if level==2:
    max_num=100
    chance=7
if level==3:
    max_num=200
    chance=5
while True:
    num = random.randint(1, max_num)
    win=False
    for i in range (chance):
      a=int(input("请输入你猜测的数字："))
      if a>num :
          print("猜大了，还剩",chance-i-1,"次机会")
      elif a<num:
          print("猜小了,还剩",chance-i-1,"次机会")
      elif a==num:
          print("猜对了")
          time.sleep(1)
          print("恭喜你")
          win=True
          break
    if win:
        c=input("输入y再来一局：")
        if c!="y":
            break
    else:
        print("游戏失败,正确答案是:",num)
        time.sleep(1)
        b=input("输入y再来一局：")
        if b!="y":
            break
