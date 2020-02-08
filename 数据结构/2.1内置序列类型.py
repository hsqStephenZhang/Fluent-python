"""
容器序列:list,tuple,collections.deque
扁平序列:str,bytes,bytearray,memoryview,array.array

可变序列:list,bytearray,].array.array,colletions.deque,memoryview
不可变序列:tuple,str,bytes
"""

# 这些序列都没怎么用过，不知道后面有没有说明
arr1 = bytearray([1, 2, 3])
arr2 = memoryview(arr1)
print(arr1)
print(arr2)
