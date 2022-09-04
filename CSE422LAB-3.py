import math
import random


class ROBOSwordFight:
    def __init__(self, minPoint, maxPoint, totalLeaf):
        self.leafPoints = []
        for i in range(totalLeaf):
            randomNumber = random.randint(minPoint, maxPoint)
            while randomNumber in self.leafPoints:
                randomNumber = random.randint(minPoint, maxPoint)
            self.leafPoints.append(randomNumber)

    def alphaBetaPruningAlgo(self, depth, branches, nodeAt, maxTurn, alpha, beta):
        if depth == 0:
            return self.leafPoints[nodeAt]
        elif not maxTurn:
            minScore = float('inf')
            for oneBranch in range(branches):
                score = self.alphaBetaPruningAlgo(
                    depth-1, branches, nodeAt*branches+oneBranch, True, alpha, beta)
                minScore = min(score, minScore)
                beta = min(beta, minScore)
                if alpha > beta:
                    break
            return minScore
        else:
            maxScore = float('-inf')
            for oneBranch in range(branches):
                score = self.alphaBetaPruningAlgo(
                    depth-1, branches, nodeAt*branches+oneBranch, False, alpha, beta)
                maxScore = max(maxScore, score)
                alpha = max(alpha, maxScore)
                if alpha > beta:
                    break
            return maxScore


if __name__ == "__main__":
    id = input("\nEnter your student ID: ")
    id = id.replace("0", "8")

    goal = int(id[:5:-1])
    minPoint = int(id[4])
    maxPoint = math.ceil(goal*1.5)

    branches = 2
    depth = 3

    finalBattle = ROBOSwordFight(minPoint, maxPoint, branches**depth)

    # Task 1
    print("\nGenerated 8 random points between the minimum and maximum point limits:",
          finalBattle.leafPoints)
    print("Total points to win:", goal)
    optimusScore = finalBattle.alphaBetaPruningAlgo(
        depth, branches, 0, True, float('-inf'), float('inf'))
    print("Achieved point by applying alpha-beta pruning =", optimusScore)
    print("The Winner is", "Optimus Prime" if optimusScore >= goal else "Megatron")

    # Task 2
    optimusScoreList = []
    maxScore = float('-inf')
    wins = 0
    shuffles = int(id[3])
    for i in range(shuffles):
        random.shuffle(finalBattle.leafPoints)
        optimusScoreList.append(finalBattle.alphaBetaPruningAlgo(
            depth, branches, 0, True, float('-inf'), float('inf')))
        if optimusScoreList[i] > maxScore:
            maxScore = optimusScoreList[i]
        if optimusScoreList[i] >= goal:
            wins += 1

    print("\nAfter the shuffle:")
    print("List of all points values from each shuffle:", optimusScoreList)
    print("The maximum value of all shuffles:", maxScore)
    print("Won", wins, "times out of", shuffles, "number of shuffles\n")
