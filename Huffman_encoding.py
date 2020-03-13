import heapq
#heapq by default makes min heap
#heapq.heappush(heap, item)
#heapq.heappop(heap)
#heapq.heappushpop(heap, item)
#heapq.heapify(x)
#heapq.heapreplace(heap, item)
#heapq.nlargest(n, iterable, key=None)
#heapq.nsmallest(n, iterable, key=None)
# from collections import Counter
d={'A':45,'B':13,'C':12,'D':16,'E':9,'F':5}

def huffman_encode(d):
	heap=[[w,[s,'']] for s,w in d.items()]
	heapq.heapify(heap)
	while len(heap)>1:
		lo=heapq.heappop(heap)
		hi=heapq.heappop(heap)
		for pair in lo[1:]:
			pair[1]='0'+pair[1]
		for pair in hi[1:]:
			pair[1]='1'+pair[1]
		heapq.heappush(heap,[lo[0]+hi[0]]+lo[1:]+hi[1:])
	return sorted(heapq.heappop(heap)[1:],key=lambda p: (len(p[-1]),p))

huff=huffman_encode(d)
print(huff)
for p in huff:
	print(p[0].ljust(10)+str(d[p[0]]).ljust(10)+p[1])
