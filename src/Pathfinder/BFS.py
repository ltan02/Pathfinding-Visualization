def reconstructPath(path):
    for node in path:
        node.makePath()


# List can be used as a queue (FIFO)
# append adds to the end of the list
# pop(0) removes the first element of the list

def bfs(end, nodes, queue):
    v = queue.pop(0)
    if not(v.isStart()) and not(v.isEnd()):
        v.makeClosed()

    if v == end:
        path = []
        temp = v
        path.append(v)
        while temp.parent is not None:
            path.append(temp.parent)
            temp = temp.parent
        reconstructPath(path[1:-1])
        return True

    neighbours = v.getNeighbours()
    for neighbour in neighbours:
        tempCol = neighbour[0]
        tempRow = neighbour[1]
        tempNode = nodes[tempRow][tempCol]
        if not(tempNode.isBarrier()) and not(tempNode.discovered):
            tempNode.discovered = True
            queue.append(tempNode)
            tempNode.parent = v
            if not(tempNode.isStart()) and not(tempNode.isEnd()):
                tempNode.makeOpen()

    return queue