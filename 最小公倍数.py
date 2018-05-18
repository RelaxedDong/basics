def lcm(x,y):
    if(x<y):
        greater = x
    else:
        greater = y
    while(True):
        if((greater%x==0) and (greater %y==0)):
            end = greater
            break
        greater+=1
    return end


num1 = int(input("输入第一个数字: "))
num2 = int(input("输入第二个数字: "))

print('最小公倍数是：',lcm(num1,num2))


# 输入第一个数字: 54
# 输入第二个数字: 24
# 最大公倍数是： 216
#
# Process finished with exit code 0