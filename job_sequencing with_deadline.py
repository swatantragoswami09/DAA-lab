def printJobSequencing(arr,t):
              n=len(arr)
              for i in range(n):
                  for j in range(n-1-i):
                      if(arr[j][2]<arr[j+1][2]):
                          arr[j],arr[j+1]=arr[j+1],arr[j]
              result = [False]*t
              job = ['-1']*t
              for i in range(len(arr)):
                  for j in range(min(t-1,arr[i][1]-1),-1,-1):
                      if(result[j] is False):
                          result[j] = True
                          job[j] = arr[i][0]
                          break
              print(job)
arr = [['j1',2,60],['j2',1,100],['j3',3,20],['j4',2,40],['j5',1,20]]    
print("Following is the maximum profit sequence of jobs")
printJobSequencing(arr,3)
