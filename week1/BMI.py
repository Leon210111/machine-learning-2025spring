# 输入身高和体重 
height = float(input('请输入身高(m):')) 
weight = float(input('请输入体重(kg):'))                                     
# 计算BMI 
BMI =  weight/height**2        
# 判断BMI是否正常 
if 18.5 <= BMI <= 24.9: 
    print('正常') 
else:
    print('不正常')