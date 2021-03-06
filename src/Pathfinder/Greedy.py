def reconstructPath(path):
    for node in path:
        node.makePath()


def greedy(end, nodes, nodesToVisit):
    winner = 0
    for i in range(len(nodesToVisit)):
        if nodesToVisit[i].distance < nodesToVisit[winner].distance:
            winner = i

    current = nodesToVisit.pop(winner)
    current.visited = True
    if not(current.isStart()) and not(current.isEnd()):
        current.makeOpen()

    if current == end:
        path = []
        temp = current
        path.append(temp)
        while temp.parent is not None:
            path.append(temp.parent)
            temp = temp.parent
        reconstructPath(path[1:-1])
        return True

    neighbours = current.getNeighbours()
    for neighbour in neighbours:
        tempCol = neighbour[0]
        tempRow = neighbour[1]
        tempNode = nodes[tempRow][tempCol]
        if not (current.isStart()) and not (current.isEnd()):
            current.makeClosed()
        if not(tempNode.isBarrier()) and not(tempNode.visited):
            tempNode.distance = tempNode.heuristic(end)
            tempNode.parent = current
            if not (tempNode.isStart()) and not (tempNode.isEnd()):
                tempNode.makeOpen()
            nodesToVisit.append(tempNode)

    return nodesToVisit



