#===============================================================================
# Starting in the top left corner of a 2*2 grid, there are 
# 6 routes (without backtracking) to the bottom right corner.
# How many routes are there through a 20*20 grid?
# 
# http://projecteuler.net/index.php?section=problems&id=15
#===============================================================================

def routeGen(gridSize):
    elements = [1,2]
    for i in xrange(1,gridSize):
        numRoutes =2*(sum(elements))
        elements.append(numRoutes)
        for index in xrange(1, len(elements)-1):
            elements[index] += int(elements[index-1])
        print ""
    return elements, elements[-1] 
    
print routeGen(20)[1]