from math import log
import operator
def calcShannonEnt(dataSet):
    numEntries = len(dataSet)
    labelCounts = {}
    for featVec in dataSet:
        currentLabel = featVec[-1]
        if currentLabel not in labelCounts.keys():
            labelCounts[currentLabel] = 0
        labelCounts[currentLabel] += 1
        shannonEnt = 0.0
        for key in labelCounts:
            prob = float(labelCounts[key]) / numEntries
            shannonEnt -= prob * log(prob,2)
    return shannonEnt

def createDataSet():
    dataSet = [[1,1,'yes'],
               [1,1,'yes'],
               [1,0,'no'],
               [0,1,'no'],
               [0,1,'no']]
    labels = ['no surfacing','flippers']
    return dataSet,labels

#split the dataSet based on feature in specified axis
def splitData(dataSet,axis,value):
    #inorder to avoid polluting original dataSet
    splitedDataSet = []
    for row in dataSet:
        if row[axis] == value:
            newItem = row[:axis]
            newItem.extend(row[axis+1:])
            splitedDataSet.append(newItem)
    return splitedDataSet

def chooseBestFeatureToSplit(dataSet):
    bestFeat = -1;bestGain = 0.0
    baseEntropy = calcShannonEnt(dataSet)
    featNum = len(dataSet[0]) - 1
    for i in range(featNum):
        values = [example[i] for example in dataSet]
        uniqueValue = set(values)
        newEnt = 0.0
        for value in uniqueValue:
            subDataSet = splitData(dataSet,i,value)
            prob = len(subDataSet)/float(len(dataSet))
            newEnt += prob * calcShannonEnt(subDataSet)
        gain = baseEntropy - newEnt
        if(gain > bestGain):
            bestGain = gain
            bestFeat = i
    return i

def majorityCnt(classList):
    classCount = {}
    for eachClass in classList:
        if eachClass not in classCount.keys():
            classCount[eachClass] = 0
        classCount[eachClass] += 1
    sortedClassCount = sorted(classCount.iteritems(),key=operator.itemgetter(1),reverse=True)
    print sortedClassCount
    return sortedClassCount[0][0]

def createTree(dataSet,labels):
    classList = [example[-1] for example in dataSet]
    #return leaf node
    if classList.count(classList[0]) == len(classList):
        return classList[0]
    if len(dataSet[0]) == 1:
        return majorityCnt(classList)

    #return judge node
    bestFeature = chooseBestFeatureToSplit(dataSet)
    bestFeatLabel = labels[bestFeature]
    myTree = {bestFeatLabel:{}}
    del(labels[bestFeature])
    featValue = [example[bestFeature] for example in dataSet]

    for value in featValue:
        subLabels = labels[:]
        subDataSet = splitData(dataSet,bestFeature,value)
        myTree[bestFeatLabel][value] = createTree(subDataSet,subLabels)

    return myTree






