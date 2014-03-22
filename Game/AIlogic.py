import sys

from basicStructs import *

#CONSTANTS:

FlatLevelsNr = 3
FlatLevels = [5, 3, 1]
PointsForFlatLevels = [7, 5, 3]
PointsForHuman = PointsForFlatLevels[:]
PointsForHuman.reverse()

PawnPoints = 20
KingPoints = 50

INF = 9e99


def boardPoints(board):
    res = 0
    tmp = board.gameWon()
    if tmp != 0:
        return tmp * 9e69
    for pos in boardCoords:
        if board[pos] == Field.AI:
            for i in xrange(FlatLevelsNr):
                if pos[1] > FlatLevels[i]:
                    #print "position:", pos, "points: ",PointsForFlatLevels[i]
                    res += PointsForFlatLevels[i]
                    break
            res += PawnPoints
        elif board[pos] == Field.AI_KING:
            res += KingPoints
        elif board[pos] == Field.HU:
            for i in xrange(FlatLevelsNr):
                if 7-pos[1] > FlatLevels[i]:
                    #print "position:", pos, "points: ",(-PointsForFlatLevels[i])
                    res -= PointsForFlatLevels[i]
                    break
            res -= PawnPoints
        elif board[pos] == Field.HU_KING:
            res -= KingPoints



    """for i in xrange(len(FlatLevels)):
        for field in FlatLevels[i]:
            if board[field] == Field.HU:
                res -= PointsForHuman[i]
            elif board[field] == Field.AI:
                res += PointsForFlatLevels[i]"""
    return res


nodes = 0
nodesMax = 1

def alfabeta(board, depth, maximizingPlayer, alfa, beta):
    global nodes
    nodes += 1

    """tmp = board.gameWon()
    if tmp != 0:
        if maximizingPlayer:
            print "OUT Node nr",nodes,"points =",9e52*tmp
            return [9e52 * tmp, None]
        else:
            print "OUT Node nr",nodes,"points =",-9e52*tmp
            return [-9e52 * tmp, None]"""
    x = boardPoints(board)
    if depth == 0 or abs(x) > 9e60:
        return [x, None]

    if maximizingPlayer:
        bestMove = None
        mov = board.possibleMoves()
        for i in mov:
            board2 = copy.deepcopy(board)
            board2.executeMove(i)
            board2.swapSides()
            val = alfabeta(board2, depth - 1, False, alfa, beta)[0]
            if val > alfa:
                alfa = val
                bestMove = i
            if alfa >= beta:
                break
        return [alfa, bestMove]
    else:
        bestMove = None
        mov = board.possibleMoves()
        for i in mov:
            board2 = copy.deepcopy(board)
            board2.executeMove(i)
            board2.swapSides()
            val = alfabeta(board2, depth - 1, True, alfa, beta)[0]
            if val < beta:
                beta = val
                bestMove = i
            if alfa >= beta:
                break
        return [beta, bestMove]


def minimaks(board, depth):
    global nodesMax, nodes
    nodesMax = 10**(depth-2);
    nodes = 0
    x = alfabeta(board, depth, True, -9e99, 9e99)
    nodes = 0
    return x


def readInt(a):
    while True:
        try:
            x = int(raw_input(a))
            break
        except ValueError:
            print "Oops!  That was no valid number.  Try again..."
    return int(x)


if __name__ == "__main__":
    a = Board()

    for i in range(0, 8, 2):
        a.set(i, 0, Field.AI)
        a.set(i, 6, Field.HU)

    for i in range(1, 8, 2):
        a.set(i, 1, Field.AI)
        a.set(i, 7, Field.HU)

    print a
    print a.possibleMoves()
    sys.stdout.flush()
    turns = 0
    while a.gameWon() == 0:
        turns += 1
        sys.stdout.write("Turn " + str(turns))
        res = minimaks(copy.deepcopy(a), 6)
        print "White:", res[1]
        a.executeMove(res[1])

        if a.gameWon() != 0:
            break

        ok = 0
        while ok == 0:
            After = a.copy()

            m = readInt("Moves? ")
            for i in xrange(m):
                x = readInt("SrcX? ")
                b = readInt("SrcY? ")
                c = readInt("DstX? ")
                d = readInt("DstY? ")
                Move = [Shift([x, b], [c, d])]
                After.executeMove(Move)

            if a.correctHumanMove(After):
                print "OK"
                a = After
                ok = 1
            else:
                print "Bad Move! Try again!"

    print a
    if a.gameWon() == 1:
        print "AI won!"
    else:
        print "Human won!"
    print "In", turns, "turns."
