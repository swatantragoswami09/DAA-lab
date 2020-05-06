import operator
n=3#number of objects
profit=[25,24,15]
weight=[18,15,10]
m=20#maximum capacity
l=[]

for i in range(n):
	l.append([profit[i],weight[i],profit[i]*1.0/weight[i]])
l=sorted(l,reverse=True,key=operator.itemgetter(2))
# print(l)
max_profit=0
fraction_obj=0

for i in range(n):
	if m>0 and l[i][1]<m:
		m-=l[i][1]
		max_profit+=l[i][0]
	else:
		fractional_obj=i
		break
if m>0:
	max_profit+=(l[fractional_obj][0])*m/(l[fractional_obj][1])
print(max_profit)
