def readInput(array, path):
    file = open(path, 'r')
    m = int(file.readline().strip())
    n = int(file.readline().strip())
    for i in range(m):
        array.append(file.readline().strip().split())


# Question 1
class Question1:
    def __init__(self) -> None:
        self.visited = []
        self.matrix = []
        self.graph = {}

    def dfs(self, graph, node, count=0):
        if node not in self.visited:
            count += 1
            self.visited.append(node)
            for neighbor in graph[node]:
                count = self.dfs(graph, neighbor, count)
        return count

    def getNode(self, row, col):
        return row*len(self.matrix[row])+col+1

    def task(self):
        readInput(self.matrix, 'input1.txt')

        for i in range(len(self.matrix[-1])*len(self.matrix)):
            self.graph[i+1] = list()

        for row in range(len(self.matrix)):
            for col in range(len(self.matrix[row])):
                node = self.getNode(row, col)
                neighbors = [(row+1, col+1), (row+1, col), (row+1, col-1), (row, col+1),
                             (row, col-1), (row-1, col+1), (row-1, col), (row-1, col-1)]
                for i in range(len(neighbors)):
                    neighborRow = neighbors[i][0]
                    neighborCol = neighbors[i][1]
                    if neighborRow >= 0 and neighborRow < len(self.matrix) and neighborCol >= 0 and neighborCol < len(self.matrix[row]):
                        if self.matrix[neighborRow][neighborCol] == 'Y':
                            self.graph[node].append(
                                self.getNode(neighborRow, neighborCol))
        max = 0

        for row in range(len(self.matrix)):
            for col in range(len(self.matrix[row])):
                nodeValue = self.matrix[row][col]
                node = self.getNode(row, col)
                if nodeValue == 'Y' and node not in self.visited:
                    infected = self.dfs(self.graph, node)
                    if max < infected:
                        max = infected
        print(max)


# Question 2
class Question2:

    def __init__(self) -> None:
        self.queue = []
        self.visited = []
        self.matrix = []
        self.graph = {}

    def bfs(self, graph, node):
        self.visited.append(node)
        self.queue.append(node)
        time = 0
        while self.queue:
            currNode = self.queue.pop(0)
            attack = 0
            for neighbor in graph[currNode]:
                if neighbor not in self.visited:
                    self.visited.append(neighbor)
                    self.queue.append(neighbor)
                    attack = 1
                    row = (neighbor-1) // (len(self.matrix[-1]))
                    col = (neighbor-1) % (len(self.matrix[-1]))
                    self.matrix[row][col] = 'A'
            if attack:
                time += 1
        return time

    def getNode(self, row, col):
        return row*len(self.matrix[row])+col+1

    def task(self):
        readInput(self.matrix, 'input2.txt')

        for i in range(len(self.matrix)*len(self.matrix[0])):
            self.graph[i+1] = []

        for row in range(len(self.matrix)):
            for col in range(len(self.matrix[row])):
                nodeValue = self.matrix[row][col]
                node = self.getNode(row, col)
                if nodeValue != 'T':
                    neighbors = [(row-1, col), (row, col-1),
                                 (row, col+1), (row+1, col)]
                    for i in range(len(neighbors)):
                        neighborRow = neighbors[i][0]
                        neighborCol = neighbors[i][1]
                        if neighborRow >= 0 and neighborRow < len(self.matrix) and neighborCol >= 0 and neighborCol < len(self.matrix[row]):
                            if self.matrix[neighborRow][neighborCol] == 'H':
                                self.graph[node].append(
                                    self.getNode(neighborRow, neighborCol))
        maximumTime = 0

        for row in range(len(self.matrix)):
            for col in range(len(self.matrix[row])):
                nodeValue = self.matrix[row][col]
                node = self.getNode(row, col)
                if nodeValue == 'A' and node not in self.visited:
                    time = self.bfs(self.graph, node)
                    if maximumTime < time:
                        maximumTime = time
        print('Time:', maximumTime, 'minutes')

        human = 0

        for row in range(len(self.matrix)):
            for col in range(len(self.matrix[row])):
                nodeValue = self.matrix[row][col]
                if nodeValue == 'H':
                    human += 1

        print("No one survived") if human == 0 else print(human, "survived")


if __name__ == "__main__":
    print()
    ques1 = Question1()
    ques1.task()
    print()

    ques2 = Question2()
    ques2.task()
    print()
