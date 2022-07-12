#创建一个列表my_list，其中包括 [1, 50] 内全部能被5整除的数字；再使用一个 for 循环将这个列表中的数字都打印出来（每个数字独占一行）。
my_list=[i for i in range(1,51) if i%5==0]
for i in my_list:
    print(i)