name = "YESILKOY SERCAN "
number = "202103933 "
major = "Computer Engineering "
mother_land = "Turkiye"

성함 = "예실코이 세르잔 "
학번 = "202103933 "
전공 = "컴퓨터공학전공 "
본국 = "튀르키예"

a = int(input("Write 0 for English, 한국어 안내를 위하여 1 작성해십시오"))

if a == 0:
              print(name + number + major + mother_land)
elif a == 1:
              print(성함 + 학번 + 전공 + 본국)
else:
  print("개꿈")
