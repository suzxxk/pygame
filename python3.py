num = 10
if num==10:
    print("10입니다.")
elif num==20:
    print("20입니다.")
else:
    print("10이 아닙니다.")
print("끝")

for i in range(10):
    print(i)

list = ['삼겹살', '항정살', '목살']
for i in list:
    print(i)

a = 1
while a<10:
    print(a)
    a+=1
# while True

#def plus3():
#    print("함수 실행함")
#print(plus3())

#def plus3(number):
#    return number
#print(plus3(500)+plus3(200))

#def plus3(number):
#    return number+3
#print(plus3(13,30))

def plus3(number1, number2):
    return number1+number2
print(plus3(13,30))


