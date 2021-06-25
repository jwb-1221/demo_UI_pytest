# a = ["appId","nonceStr","rechargeAmount","orderNo","mobile","oper","notifyUlr"]
# print(sorted(a))







# class Abc():
#     def __init__(self,a):
#         self.a = a
#     def A(self):
#         # print(self.a)
#         return self.a
#     @staticmethod
#     def B():
#         return
#     @classmethod
#     def C(cls):
#         return
# A =Abc(a=1)
# print(A.A())
# B =Abc
# print(B.B())
# C =Abc
# print(C.C())
import random
import string
# 多个字符中选取指定数量的字符组成新字符串：
print( ''.join(random.sample(['z','y','x','w','v','u','t','s','r','q','p','o','n','m','l','k','j','i','h','g','f','e','d','c','b','a'], 5)))
