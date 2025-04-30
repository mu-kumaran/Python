A = [1,1,2,2,3,3,4,5,6]
B = set(A) 
print(B) # output: {1,2,3,4,5,6}
B.add(7) # output: {1,2,3,4,5,7,6}
B.add(1) # Here duplication is not allowed. So ame set result
B.remove(4)
print(sorted(B))