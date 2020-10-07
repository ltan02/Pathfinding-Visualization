def reconstructPath(path):
    for node in path:
        node.makePath()


def dijkstra(end, nodes, unexplored):
    winner = 0
    for i in range(len(unexplored)):
        if unexplored[i].distance < unexplored[winner].distance:
            winner = i

    print(winner)
    currentNode = unexplored.pop(winner)
    if not(currentNode.isStart()) and not(currentNode.isEnd()):
        currentNode.makeOpen()

    if currentNode == end:
        path = []
        temp = currentNode
        path.append(temp)
        while temp.parent is not None:
            path.append(temp.parent)
            temp = temp.parent
        reconstructPath(path[1:-1])
        return True

    neighbours = currentNode.getNeighbours()
    if not (currentNode.isStart()) and not (currentNode.isEnd()):
        currentNode.makeClosed()
    for neighbour in neighbours:
        tempCol = neighbour[0]
        tempRow = neighbour[1]
        tempNode = nodes[tempRow][tempCol]
        if tempNode in unexplored and not(tempNode.isBarrier()):
            if not (tempNode.isStart()) and not (tempNode.isEnd()):
                tempNode.makeOpen()
            newDist = currentNode.distance + 1
            if newDist < tempNode.distance:
                tempNode.distance = newDist
                tempNode.parent = currentNode

    return unexplored







