from turtle import*

n=int(input("숫자를 입력하세요: "))
a=int(input("한 변의 길이를 입력하세요: "))

for i in range(n):
    forward(a)
    left(360/n)
