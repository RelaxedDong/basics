#encoding:utf-8

import os
# # print(os.getcwd())
# print(dir(os))
# print(help(os))

# import glob
# print(glob.glob('*.py'))

# import sys
# print(sys.argv)
# import random
# print(random.choice(['apple','orange','banana']))

# import random
# print(random.sample(range(200),20))

from datetime import date,datetime
now = date.today()
birthday = date(1998,2,18)
age = now - birthday
print()
print('本大帅从出生到现在已经\'%s\'天了'%age.days)
