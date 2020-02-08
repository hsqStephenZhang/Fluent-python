methods="ascii latin1 cp1252 cp437 gb2312 utf-8 utf-16le".split()
# 以上是基本的几种编解码器

s="abc@#$%αβγδ千毫āēě"
for method in methods:
    print(str(method)+":",end="")
    for i in s:
        try :
            print(i.encode(method),end="")
        except :
            print("?",end="")
    print("\n",end="")

print("hhh".upper())
