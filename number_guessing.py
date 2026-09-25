#项目 猜数字
import random
import time
import json
import os
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
            if os.path.exists("scores.json"):
                with open("scores.json","r",encoding="utf-8") as f:
                    scores=json.load(f)#把json文本转化成列表
            else:
                scores=[]
            scores.append(i+1)
            with open("scores.json", "w", encoding="utf-8") as f:
                json.dump(scores, f)
            break
      else:
          print("游戏失败,正确答案是:", num)
      b = input("输入y再来一局：")
      if b != "y":
          break
    if os.path.exists("scores.json"):
        with open("scores.json", "r", encoding="utf-8") as f:
            scores = json.load(f)  # 把json文本转化成列表
    else:
        scores = []
    print("历史最佳5次")
    for rank,s in enumerate(sorted(scores)[:5],start=1):
        print(f"第 {rank} 名   猜了 {s} 次")







number_game()