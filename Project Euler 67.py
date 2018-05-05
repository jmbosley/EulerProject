def Rowsum(data,num):
    for i in range(len(data[num])): #so in the range of the second to bottom row
        data[num][i] += max([data[num+1][i],data[num+1][i+1]]) #find the max path from bottom up by adding the largest neighbor to each number in that row
    if len(data[num]) ==1: #when the entire triangle has been summed over
        return data[num][0] #return total sum
    else:
        return Rowsum(data,num-1) # recursively call this for entire triangle
    
rows = []
with open('p067_triangle.txt') as f:
    for line in f:
        rows.append([int(i) for i in line.rstrip('\n').split(" ")])
        
result = Rowsum(rows,len(rows)-2)
print(result)