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
def number_game():
    while True:
      num = random.randint(1, max_num)
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
            with open("scores.txt", "a", encoding="utf-8") as f:
                f.write(f"猜了{i+1}次\n")
            break
      else:
          print("游戏失败,正确答案是:", num)
      b = input("输入y再来一局：")
      if b != "y":
        break

number_game()