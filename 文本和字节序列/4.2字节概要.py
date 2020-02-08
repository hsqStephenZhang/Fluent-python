methods="ascii latin1 cp1252 cp437 gb2312 utf-8 utf-16le".split()
str1="cafě"
cafe=bytes(str1,encoding="utf-8")

print(cafe) # 字符ě无法用ASCII表示出来，因此在utf-8编码中长度多余一个字节
print(cafe[0],cafe[:1],sep="  ")
print(cafe[0]==cafe[:1],str1[0]==str1[:1]) # Tips:该语句只是对str这种序列成立
