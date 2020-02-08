methods="ascii latin1 cp1252 cp437 gb2312 utf-8 utf-16le".split()

s="abc@#$%αβγδ毫ě"
for method in methods:
    print(str(method)+":",end="")
    for i in s:
        try :
            print(i.encode(method),end="")
        except :
            print("!",end="")
    print("\n",end="")

print("hhh".upper())
