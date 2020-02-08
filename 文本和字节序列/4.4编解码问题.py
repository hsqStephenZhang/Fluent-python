methods="ascii latin1 cp1252 cp437 gb2312 utf-8 utf-16le".split()
# 以上是基本的几种编解码器

s="abc@%αβδ千ě"
for method in methods:
    print(str(method),end=": ")
    print(s.encode(method,errors="ignore")) # 直接忽视编码问题
    print(" "*(len(str(method))+1),end="")
    print(s.encode(method,errors="replace")) # 输出编码问题，代替为?



