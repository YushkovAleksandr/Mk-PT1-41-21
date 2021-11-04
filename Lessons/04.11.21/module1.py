# import module2
# mdl2 = module2
# import module2 as mdl2
# from module2 import x as y, func as gunc
import module1
from module2 import *

x = 333
print(module1.x)

func()
print(x)