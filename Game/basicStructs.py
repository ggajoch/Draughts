import copy
class Field:
        EMPTY = 0
        HU = 1
        HU_KING = 2
        AI = 3
        AI_KING = 4
        x = 0
        y = 0
        def __init__(self, pos):
                self.x = pos[0]
                self.y = pos[1]
        def __str__(self):
                return str([self.x,self.y])

boardCoords = [[x,y] for x in xrange(8) for y in xrange(8)]
nullPos = [-1,-1]
AIkingPos = [-2, -2]
HUkingPos = [-3, -3]
   
def humanFigure(x):
    if x == Field.HU or x == Field.HU_KING:
        return True
    else:
        return False

def AIFigure(x):
    if x == Field.AI or x == Field.AI_KING:
        return True
    else:
        return False

def gamer(x):
    if x == Field.AI or x == Field.AI_KING:
        return Field.AI
    elif x == Field.HU or x == Field.HU_KING:
        return Field.HU
    return Field.EMPTY

def empty(x):
    if x == Field.EMPTY:
        return True
    else:
        return False


class Board:
        Fields = []
        def __init__(self):
                self.Fields = [[Field.EMPTY for i in range(0,8)] for j in range(0,8)]
                
        def __repr__(self):
                ret = ""
                for x in xrange(8):
                        t = []
                        for y in xrange(8):
                                t.append(self.Fields[y][7-x])
                        ret += str(t) + "\n"
                return ret

        def set(self,x,y,what):
                self[x,y] = what;
                
        def __getitem__(self,key):
                return self.Fields[key[0]][key[1]]
        def __setitem__(self, key, val):
                self.Fields[key[0]][key[1]] = val

        def swapSides(self):
            board = copy.deepcopy(self.Fields)
            for i in boardCoords:
                now = board[7-i[0]][7 - i[1]]
                if now == Field.AI:
                    self[i] = Field.HU
                elif now == Field.HU:
                    self[i] = Field.AI
                elif now == Field.AI_KING:
                    self[i] = Field.HU_KING
                elif now == Field.HU_KING:
                    self[i] = Field.AI_KING
                else:
                    self[i] = Field.EMPTY


        def executeMove(self, move): # move - [ [ [src1X, src1Y], [dst1X, dst1Y] ], [ [src1X, src1Y], [dst1X, dst1Y] ] ]
            for basic in move:
                if basic.src.x == HUkingPos[0]:
                    self[basic.dst.x,basic.dst.y] = Field.HU_KING
                elif basic.src.x == AIkingPos[0]:
                    self[basic.dst.x,basic.dst.y] = Field.AI_KING
                elif basic.dst.x == nullPos[0]: #to /dev/null
                    self[basic.src.x,basic.src.y] = Field.EMPTY;
                else:
                    self[basic.dst.x,basic.dst.y] = self[basic.src.x,basic.src.y]
                    self[basic.src.x,basic.src.y] = Field.EMPTY;
        
        def possibleMoves(self):
            moves = []
            for pos in boardCoords:
                if self[pos] == Field.AI_KING:
                    moves.extend(kingBeats(self,pos))
            if len(moves) != 0:
                return moves
            
            for pos in boardCoords:
                if self[pos] == Field.AI:
                    moves.extend(pawnBeats(self,pos))
            if len(moves) != 0:
                return moves

            for pos in boardCoords:
                if self[pos] == Field.AI_KING:
                    moves.extend(kingMoves(self,pos))
                elif self[pos] == Field.AI:
                    moves.extend(pawnMoves(self,pos))
            return moves
        
        def gameWon(self):
            """ 0 - not ended,
                1 - AI won,
                -1 = Human won """
            if len(self.possibleMoves()) == 0:
                return -1
            self.swapSides()
            if len(self.possibleMoves()) == 0:
                self.swapSides()
                return 1
            self.swapSides()      
            """AIpawns,HUpawns = (0,0)
            for i in boardCoords:
                if AIFigure(self[i]):
                    AIpawns += 1
                elif humanFigure(self[i]):
                    HUpawns += 1
            if AIpawns == 0:
                return -1
            if HUpawns == 0:
                return 1"""
            return 0

class Shift:
        src = Field([-2,-2])
        dst = Field([-2,-2]) #dummy constants
        def __init__(self, _src, _dst):
                #print _src
                self.src = Field(_src)
                self.dst = Field(_dst)
        def __repr__(self):
                return "\n(" + str(self.src) + " -> " + str(self.dst) + ")"
        
class Move:
        moveList = []
        #def __init__(self, moves):
                #moveList.append(Shift(
        def add(self,s):
                self.moveList.append(s)
                




def addToList(_list, _num):
    return [x + _num for x in _list]



def kingBeats(board, pos):
    res = []
    for dx,dy in [(-1,-1),(-1,1),(1,-1),(1,1)]:
        actual = [pos[0] + dx, pos[1] + dy]
        while 1 <= actual[0] <= 6 and 1 <= actual[1] <= 6:
            if AIFigure(board[actual]):
                break
            if humanFigure(board[actual]) and empty(board[actual[0] + dx, actual[1] + dy]):
                res.append([Shift(pos, [actual[0] + dx, actual[1] + dy]), Shift(actual, nullPos)])
                break
            if not empty(board[actual]):
                break
            actual = [actual[0] + dx, actual[1] + dy]
    return res


def kingMoves(board, pos):
    res = []
    for dx,dy in [(-1,-1),(-1,1),(1,-1),(1,1)]:
        actual = [pos[0] + dx, pos[1] + dy]
        while 0 <= actual[0] <= 7 and 0 <= actual[1] <= 7:
            if AIFigure(board[actual]):
                break;
            if empty(board[actual]):
                res.append([Shift(pos, actual)])
            actual = [actual[0] + dx, actual[1] + dy]
    return res


def pawnBeats(board, pos):
    res = []
    for dx,dy in [(-1,1),(1,1)]:
        actual = [pos[0] + dx, pos[1] + dy]
        if 0 <= actual[0]+dx <= 7:
            if 1 <= actual[1]+dy <= 6:
                if humanFigure(board[actual]) and empty(board[actual[0] + dx, actual[1] + dy]):
                    res.append([Shift(pos, [actual[0] + dx, actual[1] + dy]), Shift(actual, nullPos)])

            if actual[1]+dy == 0:
                if humanFigure(board[actual]) and empty(board[actual[0] + dx, actual[1] + dy]):
                    if board[pos] == Field.HU:
                        res.append([Shift(HUkingPos, [actual[0] + dx, actual[1] + dy]), Shift(pos, nullPos), Shift(actual,nullPos)])

            if actual[1]+dy == 7:
                if humanFigure(board[actual]) and empty(board[actual[0] + dx, actual[1] + dy]):
                    if board[pos] == Field.AI:
                        res.append([Shift(AIkingPos, [actual[0] + dx, actual[1] + dy]), Shift(pos, nullPos),Shift(actual,nullPos)])
    return res


def pawnMoves(board, pos):
    res = []
    for dx,dy in [(-1,1),(1,1)]:
        actual = [pos[0] + dx, pos[1] + dy]
        if 0 <= actual[0] <= 7 and 0 <= actual[1] <= 6:
            if empty(board[actual]):
                res.append([Shift(pos, actual)])
        if actual[1] == 0:
            if empty(board[actual]):
                if board[pos] == Field.HU:
                    res.append([Shift(HUkingPos, actual), Shift(pos, nullPos)])
        if actual[1] == 7:
            if empty(board[actual]):
                if board[pos] == Field.AI:
                    res.append([Shift(AIkingPos, actual), Shift(pos, nullPos)])

    return res








if __name__ == "__main__":
        a = Board()