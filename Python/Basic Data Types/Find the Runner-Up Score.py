n = int(input())
arr = set(list(map(int, input().split())))     
arr.remove(max(arr)) 
print(max(arr))      
