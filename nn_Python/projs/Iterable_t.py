# Iterable 
# Results가 Iterable을 상속받았으면 True #

import collections

results = 7
print("{0} 는 반복 가능? = {1}".format(results, isinstance(results, collections.Iterable)))

results = ["홍", "마"]
print("{0} 는 반복 가능? - {1}".format(results, isinstance(results, collections.Iterable)))