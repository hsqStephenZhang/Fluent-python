"""
字典推导式和list推导式差不多
但是要注意要用元组传参，zip(list1,list2)
"""
strings=list("abC")
my_dic1 = {i: char for i,char in zip(range(3),strings)}
my_dic2 = {i: char.upper() for i,char in zip(range(3),strings)}
my_dic3 = {i: char.isupper() for i,char in zip(range(3),strings)}
print(my_dic1)
print(my_dic2)
print(my_dic3)
