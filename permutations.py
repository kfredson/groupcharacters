#f and g have form: f[0] is frozenset of tuples
#f[1] is dict
#Tuples and dict do not have any elements mapped to themselves
def compose(f,g):
    tupleList = []
    newDict = {}
    for x in g[1]:
        img = g[1][x]
        if img in f[1]:
            img = f[1][img]
        if x != img:
            tupleList.append((x,img))
            newDict[x] = img
    for x in f[1]:
        if x not in g[1]:
            tupleList.append((x,f[1][x]))
            newDict[x] = f[1][x]
    return [frozenset(tupleList),newDict]

#List of pairs of form:
#f[0] is frozenset of tuples
#f[1] is dict
#Tuples and dict do not have any elements mapped to themselves
def generateGroup(gens):
    currentElementSet = set()
    gpElements = []
    for x in gens:
        currentElementSet.add(x[0])
        gpElements.append(x)
    compStack = []
    for x in gens:
        for y in gens:
            compStack.append((x,y))
    while len(compStack) > 0:
        x = compStack.pop()
        p = compose(x[0],x[1])
        if p[0] in currentElementSet:
            pass
        else:
            gpElements.append(p)
            currentElementSet.add(p[0])
            for z in gens:
                compStack.append((p,z))
    return gpElements
        
def createPairs(gens):
    pairList = []
    for x in gens:
        currentTuples = []
        xcopy = x.copy()
        for y in x:
            if x[y]==y:
                del xcopy[y]
            else:
                currentTuples.append((y,x[y]))
        pairList.append([frozenset(currentTuples),xcopy])
    return pairList


x = createPairs([{1:2,2:1},{1:2,2:3,3:1}])
y = generateGroup(x)
assert(len(y)==6)

nums = range(8)
swapList = []
for x in nums:
    for y in nums:
        if x < y:
            swapList.append({x:y,y:x})
x = createPairs(swapList)
y = generateGroup(x)
assert(len(y)==8*7*6*5*4*3*2*1)
            
        
