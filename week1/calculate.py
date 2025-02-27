# 定义函数 
def demo(a, n): 
    # 设置初值均为0 
    result, t = 0, 0 
 
    # 循环n次，[0 ~ n-1] 
    for i in range(n): 
        # 计算每一项的值 
        t = t * 10 + a 
        # 累加每一项的值 
        result =   result+t                                           
 
    # 返回结果 
    return result 
 
# 测试上面的函数 ---------------- 
print(demo(3, 4))        
# 3+33+333+3333 = 3702 