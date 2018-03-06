#题目：一个整数，它加上100后是一个完全平方数，再加上168又是一个完全平方数，请问该数是多少？

#分析

for k in range(1,13):
    a=84/k-k/2
    if int(a)==a:
        print(a*a-100)

#另外一种方法
print([n**2-100 for m in range(168) for n in range(m) if(m+n)*(m-n)==168])