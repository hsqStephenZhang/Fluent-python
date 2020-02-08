# 最简单的列表推导式
a = [x for x in range(5)]
b = [ord(char) for char in "zhang"]
c= [x*y for x in range(1,4) if x!=1 for y in range(1,4) if y!=1] #二维情况
print(a,b,c)

# 通过filter和map函数也可以实现和list推导式一样的效果
# map函数的具体使用见第五章
symbols="afjwieo"
c = [ord(char) for char in symbols if ord(char)>63]
d=list(filter(lambda c:c>63,map(ord,symbols)))
print(c,d)

#  通过list推导式生成笛卡尔积
colors=['white','black','yellow','red']
numbers=[i for i in range(1,4)]
results=[(color,number) for color in colors for number in numbers]
print(results)

# 生成器表达式形式上和list推导式差不多，只是将方括号换成了圆括号
# 但是其能够节省内存，因为其只有iter到了该位置才生成数据
import array
a=(i for i in range(5))
b=array.array("B",(i for i in range(5)))
print(a,b)
