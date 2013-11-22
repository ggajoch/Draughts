from basicStructs import *
import copy
import sys
#from gameLogic import *

#CONSTANTS:

FlatLevels = [ [[x,y] for x in xrange(8) for y in range(i,i+2)] for i in [0,2,4,6]]
PointsForFlatLevels = [2,4,8,20]
PointsForHuman = PointsForFlatLevels[:]
PointsForHuman.reverse()

PawnPoints = 5
KingPoints = 50

INF = 9e99

def boardPoints(board):
    res = 0
    tmp = board.gameWon()
    if tmp != 0:
        return tmp*9e99
    for pos in boardCoords:
        if board[pos] == Field.AI:
            res += PawnPoints
        elif board[pos] == Field.AI_KING:
            res += KingPoints
        elif board[pos] == Field.HU:
            res -= PawnPoints
        elif board[pos] == Field.HU_KING:
            res -= KingPoints
    
    for i in xrange(len(FlatLevels)):
        for field in FlatLevels[i]:
            if board[field] == Field.HU:
                res -= PointsForHuman[i]
            elif board[field] == Field.AI:
                res += PointsForFlatLevels[i]
    return res

nodes = 0

def alfabeta(board, depth, maximizingPlayer, alfa, beta):
    #print "(",depth,alfa,beta,")"
    ##print board

    #childs = []
    global nodes
    nodes += 1

    #if maximizingPlayer:
        #print "MAXI"
    #else:
        #print "MINI"
    tt = copy.copy(nodes)
    #print "INPUT Node nr",nodes,"depth = ",depth

    tmp = board.gameWon()
    if tmp != 0:
        if maximizingPlayer:
            #print "OUT Node nr",tt,"points =",9e52*tmp
            return (9e52 * tmp, None)
        else:
            #print "OUT Node nr",tt,"points =",-9e52*tmp
            return (-9e52 * tmp, None)
    if depth == 0:
        #print "OUT Node nr",tt,"points = ",boardPoints(board)
        return (boardPoints(board), None)
    if maximizingPlayer == True:
        bestMove = None
        #alfa = -9e99
        mov = board.possibleMoves()
        #if len(mov) == 1:
         #   return (alfa, mov[0])
        for i in mov:
            board2 = copy.deepcopy(board)
            board2.executeMove(i)
            board2.swapSides()
            #print "moving",i
            val = alfabeta(board2, depth-1, False, alfa, beta)[0]
            #print "Max|",val,i,"|"
            #childs.append((val, i))
            if val > alfa:
                alfa = val
                bestMove = i
            if alfa >= beta:
                break
        #print "OUT Node nr",tt,"points = ",alfa
        #if depth == 5:
            #print childs
        return (alfa, bestMove)
    else:
        bestMove = None
        #beta = 9e99
        mov = board.possibleMoves()
        #if len(mov) == 1:
        #    return (beta, mov[0])

        for i in mov:
            board2 = copy.deepcopy(board)
            board2.executeMove(i)
            board2.swapSides()
            #print "moving",i
            val = alfabeta(board2, depth-1, True, alfa, beta)[0]
            #print "Min|",val,i,"|"
            if val < beta:
                beta = val
                bestMove = i
            if alfa >= beta:
                break      
        #print "OUT Node nr",tt,"points = ",beta
        return (beta, bestMove)

def minimaks(board, depth, maximizingPlayer):
    return alfabeta(board, depth, True, -9e99, 9e99)


if __name__ == "__main__":
    a = Board();

    """a.set(1,3,Field.AI);
    a.set(3,1,Field.AI);
    a.set(5,3,Field.AI);
    a.set(5,5,Field.AI);
    a.set(6,6,Field.AI);

    a.set(4,2,Field.HU);
    a.set(4,4,Field.HU);"""
    

    """a.set(3,7,Field.HU_KING)
    a.set(5,7,Field.AI_KING)
    a.set(6,6,Field.AI)
    a.set(0,6,Field.AI)"""
    
    #a.set(1,7,Field.HU_KING)
    a.set(5,7,Field.AI_KING)
    a.set(7,7,Field.AI_KING)
    a.set(3,7,Field.HU_KING)


    #a.set(4,0,Field.HU_KING);
    #a.set(2,0,Field.AI_KING);

    #a.set(6,7,Field.HU_KING)
    #a.set(5,6,Field.AI)

    print a
    print a.possibleMoves()

    turns = 0
    while a.gameWon() == 0:
        turns += 1
        sys.stdout.write("Turn "+str(turns))
        res = minimaks(copy.deepcopy(a), 5, True)
        print "White:",res[1]
        a.executeMove(res[1])

        if a.gameWon() != 0: 
            break
            
        a.swapSides()
        res = minimaks(copy.deepcopy(a), 5, True)
        print "black:",res[1]
        a.executeMove(res[1])

        a.swapSides()
        #print a
        sys.stdout.flush()
        if turns > 50:
            break

    print a
    print a.gameWon()
    print "turns=",turns
