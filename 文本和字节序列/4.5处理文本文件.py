"""
有的时候编解码不一致会带来一些问题
常见的问题就是依赖于默认编解码方式导致的兼容问题
在GNU/Linux OS 系统中，默认值都是utf-8，因此基本上不存在编码的问题，windows用户
更容易碰到这个问题
"""
with open("test", 'r') as fp:
    print(fp.encoding)
    # 结果是cp936

import locale

print(locale.getpreferredencoding(do_setlocale=True))
