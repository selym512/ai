import math
import sys



def gradDescent(T,step_size, epsilon, M, rand):

    if(rand == False):
        centroids = []
        gate = "null"
        counter = 0
        centroid = [] * (len(setlist[0]))
        for item in setlist:
            if gate == "null":
                gate = item[-1]
                for x in range(len(item)-1):
                    centroid[x] = centroid[x] + float(item[x])
                counter += 1
            elif gate != item[-1]:
                for y in range(len(centroid)-1):
                    centroid[y] = centroid[y] / counter
                centroids.append(centroid)
                gate = item[-1]
                counter = 0
                centroid = [] * (len(item))

                for x in range(len(item)-1):
                    centroid[x] = centroid[x] + float(item[x])
                counter += 1
            else:
                for x in range(len(item)-1):
                    centroid[x] = centroid[x] + float(item[x])
                centroid[len(item)-1] = str(item[len(item)-1])
                counter += 1
        for y in range(len(centroid)-1):
            centroid[y] = centroid[y] / counter
        centroids.append(centroid)
    else:
        centroids = []
        gate = "null"
        counter = 0
        centroid = {}
        for item in setlist:
            if item[-1] in centroid:
                print("centroid: " + str(centroid[item[-1]]) + "+" + str(item[x]))
                centroid[item[-1]].append(float(item))
            centroid[item[-1]] = str(item[len(item)-1])
            counter += 1
        for y in range(len(centroid)-1):
            # centroid[y] = centroid[y] / counter
        # centroids.append(centroid)
    
    print("CENTROID ARE: " + str(centroids))
    compares = []
    correct = 0
    for v in T:
        for e in centroids:
            compares.append(distance(e, v))
        mini = min(compares)
        for i in range(len(compares)):
            if mini is compares[i]:
                if centroids[i][-1] == v[-1]:
                    correct += 1
        compares = []
    
    prevCost = 10000000
    prevAcc = float(correct)/float(len(T))
    while(True):
        print("\n\n\n\n\n\nayo why " + str(prevAcc) + "\n\n\n\n\n\n")
        TCost = 0
        nvs = []
        nws = []
        for i in centroids:
            nvs.append(0)
            nws.append(0)
        compares = []
        for y in T:
            v = y[-1]
            for e in centroids:
                compares.append(distance(e, y))
            mini = min(compares)
            for i in range(len(compares)):
                if mini == compares[i]:
                    gw = i
            compares = []
            if centroids[gw][-1] != v:
                print(str(centroids[gw][-1]) + " did not equal " + str(v))
                for j in range(len(centroids)):
                    if y[-1] == centroids[j][-1]:
                        gv = centroids[j]
                        cost = float(distance(gv, y)) - float(distance(y, centroids[gw]))
                        print("MMM: " + str(M))
                        if cost < M:
                        #     # do stuff
                            TCost += cost
                            for b in range(len(centroids)):
                                if centroids[b][-1] == v:
                                    nvlocation = b
                            nvs[nvlocation] += float(distance(gv, y))
                            nws[nvlocation] += float(distance(y, centroids[gw]))
                        else:
                            TCost += M
        print("CENTROID AREEE: " + str(centroids))
        if TCost < epsilon:
            print("tcost < ep\n"+ str(TCost) + " < " + str(epsilon) + " cost func very good")
            return centroids
        if TCost > (1-epsilon)*prevCost:
            print("tcost > 1-ep * prevcost\n"+ str(TCost) + " > " + str((1-epsilon)*prevCost) + "\nnot worth")
            return centroids
        hv = []
        for e in range(len(centroids)):
            save = [0]*len(centroids[0])
            for piece in range(len(centroids[e])-1):
                save[piece] = nvs[e] * step_size
                save[piece] = save[piece] + float(centroids[e][piece])
            save[-1] = centroids[e][-1]
            hv.append(save)
        compares = []
        correct = 0
        for v in T:
            for e in hv:
                compares.append(distance(e, v))
            mini = min(compares)
            for i in range(len(compares)):
                if mini is compares[i]:
                    if str(hv[i][-1]) == str(v[-1]):
                        correct += 1
            compares = []
        NewAcc = float(correct)/float(len(T))
        print(str(NewAcc) + " < " + str(prevAcc))
        if(NewAcc < prevAcc):
            print("prev accuracy better "+ str(NewAcc) + " < " + str(prevAcc))
            return centroids
        for v in range(len(centroids)):
            centroids[v] = hv[v]
        prevCost = TCost
        prevAcc = NewAcc
        print(str(centroids))





def distance(exemp, Y):
    sums = 0
    for x in range(len(exemp)-1):
        value = float(exemp[x]) - float(Y[x])
        value = value * value
        sums = sums + value
    sums = math.sqrt(sums)
    return sums
def add(a, b):
    new = a
    for x in range(len(a)-1):
        new[x] = new[x] + b[x]
    return new




f = open(sys.argv[1], "r")
setlist = []
for line in f:
    line = line.rstrip('\n')
    putin = line.split(',')
    setlist.append(putin)

it = 0
print(" Iteration:" + str(it))
gradDescent(setlist, sys.argv[2], sys.argv[3], sys.argv[4], False)
for l in range(int(sys.argv[5])):    
    it += 1
    print(" Iteration:" + str(it))
    f = open(sys.argv[1], "r")
    setlist = []
    for line in f:
        line = line.rstrip('\n')
        putin = line.split(',')
        setlist.append(putin)
    gradDescent(setlist, sys.argv[2], sys.argv[3], sys.argv[4], True)
