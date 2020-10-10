def reconstructPath(path):
    for node in path:
        node.makePath()


# Use a list as a Stack (LIFO)
# append to add to the end of the list
# .pop() to remove the end of the list

def dfs(end, nodes, stack):
    current = stack.pop()
    current.visited = True

    if not(current.isStart()) and not(current.isEnd()):
        current.makeClosed()

    neighbours = current.getNeighbours()
    for neighbour in neighbours:
        tempCol = neighbour[0]
        tempRow = neighbour[1]
        tempNode = nodes[tempRow][tempCol]
        if not(tempNode.isBarrier()) and not(tempNode.visited):
            if tempNode == end:
                tempNode.parent = current
                path = []
                temp = tempNode
                path.append(temp)
                while temp.parent is not None:
                    path.append(temp.parent)
                    temp = temp.parent
                reconstructPath(path[1:-1])
                return True
            else:
                tempNode.parent = current
                stack.append(tempNode)
                if not (tempNode.isStart()) and not (tempNode.isEnd()):
                    tempNode.makeOpen()

    return stack
