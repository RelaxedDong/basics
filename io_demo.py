import os
# ------------------------------------------------------
# 1	 os.access(path, mode) 检验权限模式

# path - - 要用来检测是否有访问权限的路径。
# mode - - mode为F_OK，测试存在的路径，或者它可以是包含R_OK, W_OK和X_OK或者R_OK, W_OK和X_OK其中之一或者更多。
# os.F_OK: 作为access() 的mode参数，测试path是否存在。
# os.R_OK: 包含在access() 的mode参数中 ， 测试path是否可读。
# os.W_OK 包含在access() 的mode参数中 ， 测试path是否可写。
# os.X_OK 包含在access() 的mode参数中 ，测试path是否可执行。

# ret1 = os.access('基础笔记.txt',os.F_OK)
# print('F_OK值%s'%ret1)
# ret2 = os.access('基础笔记.txt',os.R_OK)
# print('R_OK值为%s'%ret2)
# ret3 = os.access('基础笔记.txt',os.W_OK)
# print('R_OK值为%s'%ret3)
# ret4 = os.access('基础笔记.txt',os.X_OK)
# print('R_OK值为%s'%ret4)

# ********结果：
# F_OK值True
# R_OK值为True
# R_OK值为True
# R_OK值为True
# **********
#_-----------------------------------------------
# 2.os.chdir() 方法用于改变当前工作目录到指定的路径。
# 查看当前工作目录
# print(os.getcwd())
#更改工作目录
# path = r'D:\pycharm_project\test'
# ret = os.getcwd()
# os.chdir(path)
# print('目录修改成功',ret)
#