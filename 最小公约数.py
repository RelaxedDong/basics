def hcf(x,y):
    if(x<y):
        smaller = x
    else:
        smaller = y
        for i in range(1,smaller+1):
            if((x%i==0) and (y%i==0)):
                end = i
    return end



num1 = int(input("输入第一个数字: "))
num2 = int(input("输入第二个数字: "))

print('最大公约数是：',hcf(num1,num2))

# 输入第一个数字: 54
# 输入第二个数字: 24
# 最大公约数是： 6