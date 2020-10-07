def heuristic(a, b):
    (x1, y1) = a
    (x2, y2) = b
    return abs(x1 - x2) + abs(y1 - y2)


def reconstructPath(path):
    for node in path:
        node.makePath()


def astar(start, end, nodes, openSet, closedSet):
    winner = 0
    for i in range(len(openSet)):
        if openSet[i].f < openSet[winner].f:
            winner = i

    current = openSet.pop(winner)
    if current != start and current != end:
        current.makeOpen()

    if current == end:
        path = []
        temp = current
        path.append(temp)
        while temp.previous is not None:
            path.append(temp.previous)
            temp = temp.previous
        reconstructPath(path[1:-1])
        return True

    closedSet.append(current)
    if current != start and current != end:
        current.makeClosed()
    neighbours = current.getNeighbours()
    for neighbour in neighbours:
        tempCol = neighbour[0]
        tempRow = neighbour[1]
        tempNode = nodes[tempRow][tempCol]
        if not(tempNode in closedSet) and not(tempNode.isBarrier()):
            tempG = tempNode.g + 1

            newPath = False
            if tempNode in openSet:
                if tempG < tempNode.g:
                    tempNode.g = tempG
                    newPath = True
            else:
                tempNode.g = tempG
                newPath = True
                openSet.append(tempNode)
                if tempNode != start and tempNode != end:
                    tempNode.makeOpen()

            if newPath:
                tempNode.h = heuristic((tempCol, tempRow), end.pos)
                tempNode.f = tempNode.g + tempNode.h
                tempNode.previous = current

    return openSet, closedSet