# 转ascill码
print(ord("A"))

# string转byte
print("ABC:",'ABC'.encode('ascii'))
print("中文:",'中文'.encode('utf-8'))

# utf8是unicode的实现,unicode是众多编码的统一

# byte转string
a = 'ABC'.encode('ascii')
print('ABC:',a.decode('ascii'))
b = '中文'.encode('utf-8')
print('中文:',b.decode('utf-8'))


# 计算字符串/字节长度
print('aaabbb len=',len("aaabbb"))
print('a len=',len(a))
# 单个中文占3个字节
print('b len=',len(b))


