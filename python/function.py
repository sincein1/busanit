# def add(a,b):
#     return a+b
# print(add(5,3))

# x = 3
# y = 4
# c = add(x, y)
# print(c)

# def A(a, b):
#     return a*b
# print(A(2,3))

# def say():
#     return 'Hi'

# print(say())

# def add(a,b):
#     print("%d, %d의 합은 %d입니다." %(a, b, a+b))
    
# add(5,3)

# def say():
#     print("Hi")
    
# say()

# def add(a, b):
#     result = a+b
#     return result

# result = add(5,3)
# print(result)

# def add_many(*args):
#     result = 0
#     for i in args:
#         result = result + i
#     return result

# result = add_many(1,2,3,4,5,6,7,8,9,10)
# print(result)

# def add_mul(choice, *args):
#     if choice == "add":
#         result = 0
#         for i in args:
#             result += i
            
#     elif choice == "mul":
#         result = 1
#         for i in args:
            
#             result *= i
            
#     return result

# a = add_mul("add", 1,2,3,4)
# print(a)
# b = add_mul("mul", 1,2,3,4)
# print(b)

def add_and_mul(a,b):
    return a+b, a*b

result = add_and_mul(3,4)
print(result)
print(type(result))