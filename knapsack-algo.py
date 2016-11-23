def knapsack(W,wt,val,n):
	k = [[0 for x in range(W+1)]for x in range(n+1)]
	for i in range(n+1):
		for w in  range(W+1):
			if i==0 or w==0:
			  k[i][w] = 0
			elif wt[i-1]<= w:
			  k[i][w] = max(val[i-1]) + k[i-1][w-wt[i-1]], k[i-1][w]
			else:
			  k[i][w] = k[i-1][w]

	return k[n][W]

val = [2,2,5]
wt = [1,2,3]
W = 5
n = len(val)
print (knapsack(W,wt,val,n))		 
