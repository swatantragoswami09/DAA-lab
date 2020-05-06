
import math
class Sorting:

	def Bubble_sort(self,l):
		t=0
		for i in range(len(l)-1,0,-1):
			for j in range(0,i):
				if l[j]>l[j+1]:
					t=l[j]
					l[j]=l[j+1]
					l[j+1]=t
		return l

	def Selection_sort(self,l):
		t=0
		for i in range(0,len(l)):
			min=i
			for j in range(i+1,len(l)):
				if l[j]<l[min]:
					min=j
			if min!=i:
				l[i],l[min]=l[min],l[i]
		return l

	def Insertion_sort(self,l):
		for i in range(1,len(l)):
			key=l[i]
			j=i-1
			while j>=0 and l[j]>key:
				l[j+1]=l[j]
				j=j-1
			l[j+1]=key
		return l
	
	def quick_sort(self,l,first,last):
		if first<last:
			q=self.partition(l,first,last)
			self.quick_sort(l,first,q-1)
			self.quick_sort(l,q+1,last)
		return l

	def partition(self,l,first,last):
		x=l[last]
		i=first-1
		for j in range(first,last):
			if l[j]<=x:
				i+=1
				l[i],l[j]=l[j],l[i]
		l[i+1],l[last]=l[last],l[i+1]
		return i+1

	def merge_sort(self,l,first,last):
		if first<last:
			q=math.ceil((first+last)/2)
			self.merge_sort(l,first,q)
			self.merge_sort(l,q+1,last)
			self.MERGE(l,first,q,last)
		return l

	def MERGE(self,l,first,q,last):
		n1=q-first+1
		n2=last-q
		left=[0]*(n1+1)
		Right=[0]*(n2+1)
		for i in range(0,n1-1):
			left[i]=l[first+i]
		for j in range(0,n2-1):
			right[j]=l[q+j]
		print(left)
		print(right)
		left[n1]=1000
		right[n2]=1000
		i=1
		j=1
		for k in range(first,last):
			if left[i]<=right[j]:
				l[k]=left[i]
				i+=1
			else:
				l[k]=right[j]
				j+=1

	def count_sort(self,l,k):
		c=[0]*(k+1)
		
		b=[0]*(len(l)+1)
		
		for i in range(0,len(l)):
			c[l[i]]+=1
		# print('c=',c)

		for i in range(1,k+1):
			c[i]+=c[i-1]
		# c.pop(0)
		# print('c=',c)

		for i in range(len(l)-1,0,-1):
			b[c[l[i]]]=l[i]
			c[l[i]]-=1
		# c.pop(0)
		# print('c=',c)
		b.pop(0)
		b.pop(0)


		return b

	def Heap_sort(self,l):
		self.Build_max_heap(l)
		heapsize=len(l)
		for i in range(heapsize-1,3):
			l[1],l[i]=l[i],l[1]
			heapsize-=1
			self.max_heapify(l,1)
		return l

	def Build_max_heap(self,l):
		heapsize=len(l)
		for i in range(math.ceil(heapsize/2),3,-1):
			self.max_heapify(l,i)

	def max_heapify(self,l,i):
		left=2*i
		right=2*i+1
		largest=0
		
		if left<=len(l)-1 and l[left]>l[i]:
			largest=left
		else:
			largest=i
		if right<=len(l)-1 and l[right]>l[largest]:
			largest=right
		if largest!=i:
			l[i],l[largest]=l[largest],l[i]
			self.max_heapify(l,largest)







	
		
l=[2,5,3,0,2,3,0,3]
s=Sorting()
print('Bubble Sorting =',s.Bubble_sort(l))
print('Selection Sorting =',s.Selection_sort(l))
print('Insertion Sorting =',s.Insertion_sort(l))
print('Quick Sorting =',s.quick_sort(l,0,5))
# print('Merge Sorting=',s.merge_sort(l,0,5))
print('Count Sorting =',s.count_sort(l,max(l)))
print('Heap Sorting =',s.Heap_sort(l))
