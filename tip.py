#globals()#是将变量转换为全局变量
#nonlocal()#是将局部变量转换为全局变量
#shutil.copyfile(file, file)前者复制到后者
#abs()返回一个数的绝对值
#getattr()获取函数属性值，getattr(对象，属性，“值”),如果属性不存在就会报错，也可以给不存在的属性返回默认值
# setattr()设置属性值，setattr(对象，属性，值),如果属性不存在会创建一个新的对象属性，并对属性赋值：
#hex() 函数用于将一个指定数字转换为 16 进制数。
#oct()函数用于将一个整数转换为8进制字符串
#sort 与 sorted 区别：sort会对原列表进行更改，sorted可以对所有可迭代的对象进行排序操作，生成新的对象
#map(函数, [1,2,3,4,5])    # 计算列表各个元素的平方,list(map(square, [1,2,3,4,5]))   # 使用 list() 转换为列表
#bin()返回一个数字的二进制
#filter(function, iterable)function -- 判断函数。iterable -- 可迭代对象。
#math.pow( x, y )，x的y方。pow(x,y):x的y次方
#vars(object) 函数返回对象object的属性和属性值的字典对象。
#locals() 函数会以字典类型返回当前位置的全部局部变量。
    # def runoob(arg):    # 两个局部变量：arg、z
    #   z = 1
    #   print (locals())
#memoryview() 函数返回给定参数的内存查看对象(memory view)。
# v = memoryview('abcefg')
# v[1]
# ---'b'
# v[-1]
# ---'g'
# v[1:4]
# ---<memory at 0x77ab28>
# v[1:4].tobytes()
# ---'bce'






# 随机浮点型数字
# import random
# import string

# print(random.random())随机浮点型数字

# print(random.uniform(1, 10))1到10随机的浮点型数字

# print(random.choice('abcdefghijklmnopqrstuvwxyz!@#$%^&*()'))从中随机一个字符

# print(random.sample('zyxwvutsrqponmlkjihgfedcba',5))从中随机五个字符，五个字符用列表包起来

# 从a-zA-Z0-9生成指定数量的随机字符：
#ran_str = ''.join(random.sample(string.ascii_letters + string.digits, 8))
#print (ran_str)

# 多个字符中选取指定数量的字符组成新字符串：
#print( ''.join(random.sample(['z','y','x','w','v','u','t','s','r','q','p','o','n','m','l','k','j','i','h','g','f','e','d','c','b','a'], 5)))

# 打乱排序
# items = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
# print random.shuffle(items)






class A:
    __bar = 1
    # print(__bar)
    a= 1
    b=2
    abc=a+b
    # print(abc)

class B():
    a = A()
    # print("bar1")
    @classmethod
    def b(self):
        # return 123
        # print(getattr(B.a,"bar"))
        setattr(B.a,"bar",8)
        # return getattr(B.a,"bar")
        return A().a
# setattr(B.a,"bar1",8)
# print(A.bar)
if __name__ == "__main__":
    print(B().b())

