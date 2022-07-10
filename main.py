#NP16 累加与平均数
my_list=[ i for i in range(1,1001)]    # 创建一个列表，这个列表从1到1000
print(min(my_list))                    # min求最小值
print(max(my_list))                    # max求最大值
print(sum(my_list))                    # sum求和
print(round(sum(my_list)/1000,1))      #round函数，设定结果保留位数
