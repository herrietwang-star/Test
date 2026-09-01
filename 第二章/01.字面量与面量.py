# 字面量的写法
print(100)  # 整数字面量（int）
print(3.14)  # 浮点数字面量（float）
print(True) # 布尔字面量（bool）
print(False)  # 布尔字面量（bool）
print("hello python")  # 字符串字面量（str）
print("------------")  #字符串字面量（str）
print(None)# 空字面量（NoneType）
# 布尔类型本质上也是整数类型，True在计算机中是1，False在计算机中是0
print(True+1)  #2
print(False-1)  #-1
print(True+False)  #1

# 变量---Python中动态语言类型，一个变量是可以储存不同类型的数据的，但推荐一种变量储存一种类型的数据
num = 1000  
print(num)  

num = num+100
print(num)

a = "cpdd"
print(a)

b = False
print(b)
# # 案例
# 课程基础播放量为：每个月20万，课程上线后每个月的播放量为上个月的播放量加上40万，计算课程上线后第2个月的播放量
base = 20 #基础播放量
incr = 40 #每个月的播放量增量
print("课程第一个月的播放总量",base+incr)
print("课程第二个月的播放总量",base+incr*2)
# # 案例puls
base,incr = 20 ,40
print("课程第一个月的播放总量",base+incr)
print("课程第二个月的播放总量",base+incr*2)

# 案例 现有三个变量a分别为a=100, b=200, c=300,现在需要将三个变量的值进行交换，将a,b,c的值分别赋值给c, a, b
a=100
b=200
c=300
e=a #e=100
f=b #f=200
g=c #g=300
c=e
a=f
b=g
print(a,b,c)


