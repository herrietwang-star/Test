# 常见数据类型----获取指定的字面量或变量的类型
print(type("hello")) #str
print(type(100)) #int
print(type(3.14)) #float
print(type(True)) #bool
print(type(None)) #NoneTyope

# 常见数据类型 ----isinstance(数据，类型)----bool值-------判定数据是否为指定的类型，如果是：True，否则：False
print(isinstance(100,int)) #True
print(isinstance("hello",str))
print(isinstance(True,bool)) #True
print(isinstance(3.14,int)) #False

# 字符串
# 常见的字符串类型
s1="hello" #双引号
s2='python' #单引号
s3=""""hello
python
hello
world""" #三引号
print(s1)
print(s2) 
print(s3) #三引号可以换行

# 定义字符串
# 转义字符\'  \"  \n  \t
msg='It\'s a beautiful day' #使用转义字符\'
print(msg)
msg1="It's a beautiful day" 
print(msg1)
msg2="hello的意思是\"你好\"" #使用转义字符\"
print(msg2)
msg3='hello的意思是"你好"' 
print(msg3)
print("hello\npython") #使用转义字符\n换行
print("\thello\n\tpython") #使用转义字符\t制表符---缩进

# 字符串拼接
s1 = "我用python" "," "创造奇迹"
print(s1) 
msg1="我用python"
msg2="创造奇迹"
print("王晓雯说："+msg1+","+msg2) #字符串拼接
# 案例 ----需要将int类型的数字转为字符串str
name = "王晓雯"
age = 19
pro = "油气储运工程"
hobby = "健身、书法、旅游"
print("大家好，我是"+name+","+"今年"+str(age)+"岁，我的专业是"+pro+",我的爱好是："+hobby)

# 字符串格式化----使用占位符%
name = "王晓雯"
age = 19
pro = "油气储运工程"
hobby = "健身、书法、旅游"
print("大家好，我是%s今年%s岁，我的专业是%s,我的爱好是:%s"%(name,age,pro,hobby))
# 字符串格式化----使用f"  {变量名/表达式}  "---最推荐
name = "王晓雯"
age = 19
pro = "油气储运工程"
hobby = "健身、书法、旅游"
print(f"大家好，我是{name}今年{age}岁，我的专业是{pro},我的爱好是:{hobby}")