class Solution:
    def minJumps(self, arr: List[int]) -> int:
        n = len(arr)
        G = {}
        for i in range(n):
            x = arr[i]
            if(x not in G):G[x]=[i]
            else:G[x].append(i)
        
        q1 = []
        q2 = []
        visited = [0]*n
        q1.append(0)
        q2.append(n-1)
        steps=0
        L1 = 1
        L2 = 1
        flag = 1
        steps1 = 0
        steps2 = 0
        q=q1
        while(len(q)!=0):
            t = 0
            if(flag==1):
                q = q1
                L = L1
            else:
                q = q2
                L = L2
                
            for i in range(L):
                x = q.pop(0)
                if(flag==1 and x in q2):return steps1 + steps2
                if(flag==2 and x in q1):return steps1 + steps2
                if(visited[x]==1):continue
                visited[x]=1
                nei = []
                if(x>0):nei.append(x-1)
                if(x<n-1):nei.append(x+1)
                if(arr[x] in G):
                    y = G[arr[x]]
                    for i in y:
                        if(i!=x):nei.append(i)
                t+=len(nei)
                q.extend(nei)
            
            
            if(flag==1):
                L1 = t
                steps1+=1
            else:
                L2 = t
                steps2+=1
            if(L1>L2):flag=2
            else:flag = 1
        
        return steps
            
