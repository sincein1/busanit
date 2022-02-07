'''def add(a,b):
    return a+b

print(add(3,4))

a = add(5,6)
print(a)

food = "\"python is very easy.\" he says."
print(food)

multiline = "Life is too short \nYou need python"
print(multiline)
'''

"""
multiline=
Life is to short
      You need python

print(multiline)
"""
'''
a = "Python"
b = " is fun!"

print(a+b)

num1 = "100"
num2 = 2
print(num1 * num2)
'''
'''
a = "-"
b = "a"
print(a*10)
print(b*10)
'''
'''
a = "Life is too short"
print(len(a))
print(a[3])
print(a[4])
print(a[-1])'''
'''
a = "Life is too short, You need python"

b = a[12:17]
c = a[6]
print(c)'''
'''
a = "20010331Rainy"
year = a[:4]
month = a[4:6]
day = a[6:8]
weather = a[8:]

print(year)
print(month)
print(day)
print(weather)'''

# %d, %s : 포맷스트링
'''
number = 10
day = "three"
print("I eat %-10d apples." % number)
print("I eat %10s apples." % "five")

print("I ate %d apples. so I was sick for %s days." % (number, day))'''
'''
print("%10s" % "five")
print("%-10d" % 1234)
print("%10.1f" % 3.17)'''
'''
print("I eat %d apples." % 3)
print("I eat {0} apples.".format("three"))
print("I eat {0} apples.".format(3))'''
'''
number = 10
day = "three"
print("I ate {0} apples. so I was sick for {1} days.".format(number, day))'''
'''
print("{0:=<10}".format("hi"))'''
'''
a = 3.1412341234
print("{0:0.4f}".format(a))'''
'''
{인덱스 : 채울문자 정렬방식 전체자릿수}
print("{0:-^10}".format("asdf"))
'''
'''
a = 3.123123123
print("{0:0.4f}".format(a))

print("값은 {{{0}}}입니다.".format(123))

name = "홍길동"
age = 30
print(f"나는 {name}이다. {age}살이고, 내년에는 {age+1}살이 된다.")
print("나는 {0}이다. {1}살이고, 내년에는 {2}살이 된다.".format(name, age, age+1))'''

'''
a = "abababanana"
b = 1231231123

print(len(a))
print(a.count('a'))
print(a.find('a'))
print(a.index('a'))
print(a.find('c'))
print(a.index('ab'))
print(a.find('ab'))'''
'''
a = "life is too short"

print(a.replace("life", "leg"))'''
'''
a = "life is too short"
b = a.split()
print(a.split())
print(b[3],b[2])'''

'''
a = "홍길동;30;서울;vip"

print(a.split(";"))'''

# 리스트
'''
number = [1,2,3,4,5,6,7,8,9,0]
odd = [1,3,5,7,9]
even = [2,4,6,8]

print(number)
print(odd)'''
'''
dic = {'name':'pey', 'phone':'0119993323', 'birth':'1118'}

print(dic['name'], dic['phone'])

dic['hobby'] = 'game'
print(dic)
del dic['name']
print(dic)'''

#  name_list = ["김연아","류현진","박지성","귀도"]
#  special = ["피겨","야구","축구","파이썬"]

# name = input("찾는 이름은?")
# idx = name_list.index(name)
# spe = special[idx]

# print(f"{name}의 특기는 {spe}입니다.")

# dic = {"김연아":"피겨","류현진":"야구","박지성":"축구","귀도":"파이썬"}

# name = input("찾는이름은?")
# spe = dic[name]
# print(f"{name}의 특기는 {spe}입니다.")

# abc = {"김연아":"피겨","류현진":"야구","박지성":"축구","귀도":"파이썬"}

# print(abc.keys())
# print(abc.values())

# print(list(abc.keys()))

# print(abc.items())


# for i in abc.keys():
#     print(i)

# for j in abc.values():
#     print(j)

# for k in abc.items():
#     print(k)

# print(list(abc.items()))

# del abc['김연아']

# print(abc.get('김연아'))
# print(abc['김연아'])

# print(abc.get('박우진'))

# print(abc.get('박우진','없다'))

# print('박우진' in abc)
# print('김연아' in abc)
# print('피겨' in abc)
 
# abc = {"김연아":"피겨","류현진":"야구","박지성":"축구","귀도":"파이썬"}

# key_value = input('찾고 싶은 사람은?')

# if key_value in abc:
#     print(abc.get(key_value))
# else:
#     print(f"{key_value}(은)는 없는 키입니다.")

# from copy import copy

# a = [1,2,3]
# b = copy(a)

# print("a =", id(a))
# print("b =", id(b))

#------------------------------------------------------------------
# # 01 연습문제
# jumsu = [80,75,55]

# avg = (jumsu[0]+jumsu[1]+jumsu[2])/len(jumsu)

# print(avg)

 # 풀이
# jumsu = [80, 75, 55]
# total = 0
# for i in jumsu:
#      total = total + i
  
# avg = total/len(jumsu)
# print(avg)
#-----------------------------------------------

# # 02 연습문제
# a = 13
# if a%2:
#     print('홀수')
# else:
#     print('짝수')
#---------------------------------------
# 03 연습문제
# a = '881234-1121212'
# print(a[0:6], a[7:])
#-------------------------------------------
# 04 
# a = '881234-1121212'
# print("성별확인숫자 =",a[7])
#------------------------------------
# 05
# a = "a:b:c:d"
# print(a.replace(":","#"))
#-------------------------------------
# 06
# a = [1, 3, 5, 4, 2]
# a.sort()
# a.reverse()
# print(a)
# -----------------------------------------
# 07
# a = ['life','is','too','short']
# b = " ".join(a)
# print(b)
# -------------------------------------------
# 08
# a = (1, 2, 3)
# b = (4,)
# print(a+b)
# -------------------------------------------------
# 09
# 딕셔너리에 변할 수 있는 값 리스트는 넣을　수 없다
# ----------------------------------------------------
# 10
# a = {'A':90, 'B':80, 'C':0}
# print(a.pop('B'))
# ----------------------------------------
# 11
# a = [1,1,1,2,2,2,3,3,4,4,5]
# b = set(a)
# c = list(b)
# print(c)
# ----------------------------------------
# 12
# a = b = [1, 2, 3]
# a[1] = 4
# print(a)


