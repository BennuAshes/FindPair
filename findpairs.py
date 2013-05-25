# Returns a tuple of neighbors
def getNeighbors(grid, x,y):
    neighbors = []
    if x-1 >= 0:
        #grid[x-][y]
        neighbors.append((x-1,y))
    if y-1 >= 0:
        neighbors.append((x,y-1))
        
    if x+1 < len(grid[x]):
        neighbors.append((x+1,y))

    if y+1 < len(grid):
        neighbors.append((x,y+1))
    return neighbors


# Bad assumption #1 - 2d array
POS_X = 0
POS_Y = 1
grid = [[1,2,3],
        [1,3,4],
        [1,2,1]]
highestNode = (0,0) # first main node
highestNeighbor = (0,0)  # second
highestSum = 0 # Assumption #2, the minimum in the grid is greater than this number

for y,row in enumerate(grid):
    #print "y,row",y,row
    for x,node in enumerate(row):
        #print "x,node:",x,node
        neighbors = getNeighbors(grid,x,y)
        #print "Neighbor of (",x,y,")[",grid[y][x],"] = ",neighbors
        for neighbor in neighbors:
            #print "neighbor in inner loop",neighbor
            #print neighbor[POS_X],neighbor[POS_Y]
            edgeSum = grid[neighbor[POS_Y]][neighbor[POS_X]] + grid[y][x]
            print "current edge sum vs highest",edgeSum," vs ",highestSum
            if edgeSum > highestSum:
                highestNode = (x,y)
                highestNeighbor = neighbor
                highestSum = edgeSum
                print "Just set maxSum to edgeSum"
                
        #print y,x
        #print grid[y][x]
        #print len(grid) # 4
        #print len(grid[x]) # 3
print "WINNER WINNER",highestSum,highestNode,highestNeighbor
