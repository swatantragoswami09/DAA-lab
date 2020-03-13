l=[('A1',1,3),('A2',2,5),('A3',3,4),('A4',4,7),('A5',7,10),('A6',8,9),('A7',9,11),('A8',9,13),('A9',11,12),('A10',12,14)]
l=sorted(l,key=lambda x: x[2])
def activity_selection(l):
	# print(l)
	j=0
	result=[]
	result.append(l[0][0])
	for i in range(1,len(l)):
		if l[i][1]>=l[j][2]:
			result.append(l[i][0])
			j=i
	return result
print(activity_selection(l))
