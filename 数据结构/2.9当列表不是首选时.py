"""
虽然列表灵活又方便，但是因为其可以存放多种类型的对象，所以其运行速度必然很慢
对于数组来说，最好使用numpy,scipy,array类型
"""
""" 
常用的array的类型码有:
'h'/'H':signed/Unsigned short
'i'/'I':signed/Unsigned int
'l'/'L':signed/Unsigned long
'f':float
'd':double
'b'/B':signed/Unsigned char
"""
from array import array

a=array(range(10))
print(a)

