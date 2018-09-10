import matplotlib.pyplot as plt

decisionNode = {'boxstyle': "sawtooth", 'fc': "0.8"}
leafNode = {'boxstyle': "round4", 'fc': "0.8"}
arrow_args = dict(arrowstyle="<-")

def plotNode(nodeTxt,centerPt,parentPt,nodeType):
    createPlot.ax1.annotate(nodeTxt, xy=parentPt,xycoords='axes fraction',
                              xytext=centerPt,textcoords='axes fraction',
                              va='center',ha='center',bbox=nodeType,arrowprops=arrow_args)

def createPlot():
    fig = plt.figure(1,facecolor='white')
    fig.clf()
    createPlot.ax1 = plt.subplot(111,frameon=False)
    plotNode('a decision node',(0.5,0.1),(0.1,0.5),decisionNode)
    plotNode('a leaf node',(0.8,0.1),(0.3,0.8),leafNode)
    plt.show()

def getLeafNum(tree):
    leafNum = 0;
    firstKey = tree.keys()[0]
    subTree = tree[firstKey]
    for key in subTree.keys():
        if type(subTree[key]).__name__ == 'dict':
            leafNum += getLeafNum(subTree[key])
        else:
            leafNum += 1
    return leafNum

def getDepth(tree):
    maxDepth = 0
    firstKey = tree.keys()[0]
    subTree = tree[firstKey]
    for key in subTree.keys():
        currentDepth = 0
        if type(subTree[key]).__name__ == 'dict':
            currentDepth = 1 + getDepth(subTree[key])
        else:
            currentDepth = 1
        if currentDepth > maxDepth:
            maxDepth = currentDepth
    return maxDepth

def plotMidText(cntrPt,parentPt,txtString):
    xMid = (parentPt[0] - cntrPt[0]) / 2.0 + cntrPt[0]
    yMid = (parentPt[1] - cntrPt[1]) / 2.0 + cntrPt[1]
    createPlot.ax1.text(xMid,yMid,txtString)

def plotTree(myTree,parentPt,nodeTxt):
    leafNums = getLeafNum(myTree)
    depth = getDepth(myTree)
    firstStr = myTree.keys()[0]
    cntrPt = (plotTree.xOff + (1.0 + float(leafNums)) / 2.0 / plotTree.totalW,plotTree.yOff)
    plotMidText(cntrPt,parentPt,nodeTxt)
    plotNode(firstStr,cntrPt,parentPt,decisionNode)
    secondDict = myTree[firstStr]
    plotTree.yOff = plotTree.yOff - 1.0 / plotTree.totalD
    for key in secondDict.keys():
        if type(secondDict[key]).__name__ == 'dict':
            plotTree(secondDict[key],cntrPt,str(key))
        else:
            plotTree.xOff = plotTree.xOff + 1.0 / plotTree.totalW
            plotNode(secondDict[key],(plotTree.xOff,plotTree.yOff),cntrPt,leafNode)
            plotMidText((plotTree.xOff,plotTree.yOff),cntrPt,str(key))
    plotTree.yOff = plotTree.yOff + 1.0 / plotTree.totalD

def createPlot(inTree):
    fig = plt.figure(1,facecolor='white')
    fig.clf()
    axprops = dict(xticks=[],yticks=[])
    createPlot.ax1 = plt.subplot(111,frameon=False,**axprops)
    plotTree.totalW = float(getLeafNum(inTree))
    plotTree.totalD = float(getDepth(inTree))
    plotTree.xOff = -0.5/plotTree.totalTree; plotTree.yOff = 1.0;
    plotTree(inTree,(0.5,1.0),'')
    plt.show()