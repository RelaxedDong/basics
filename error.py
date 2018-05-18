#encoding:utf-8

# while True print("hello")
# SyntaxError: invalid

# print('2'+'3')

# while True:
#     try:
#         x = int(input('input a number:'))
#
#         print(x)
#         break
#     except ValueError:
#         raise NameError('必须输入数字')

#自定义异常类
class MyError(Exception):
    def __init__(self,value):
        self.value = value
    def __str__(self):
        return repr(self.value)

# try:
#     raise MyError(2*2)
# except MyError as e:
#     print('my exception occured,value:',e.value)

raise MyError('sjdf')