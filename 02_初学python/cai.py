import random
secret=random.randint(1,10)
temp = input("猜一个数字：")
guess = int(temp)
while guess != secret:
	temp = input("猜错了再试一次吧：")
	guess = int(temp)
	if guess == secret:
		print("你是我心里的蛔虫吗？！")
		print("哼，猜中了也没有奖励！")
	elif guess < secret:
		print("嘿嘿，小了，"
			  "小了")
	else:
		print("哥，大了大了！")
print("游戏结束，不玩啦ヾ(≧▽≦*)o")
