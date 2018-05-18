def end(n):
    if n<=1:
        return n
    else:
        return (end(n-1)+end(n-2))

input_n = int(input('n is?'))

if input_n<=0:
    print('no no no ')
else:
    print('Fibonacci sequence :')
    for i in range(input_n):
        print(end(i))


#end:
# n is?10
# Fibonacci sequence :
# 0
# 1
# 1
# 2
# 3
# 5
# 8
# 13
# 21
# 34

