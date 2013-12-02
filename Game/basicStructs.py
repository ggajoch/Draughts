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
        return str([self.x, self.y])


boardCoords = [[x, y] for x in xrange(8) for y in xrange(8)]
nullPos = [-1, -1]
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
        self.Fields = [[Field.EMPTY for i in range(0, 8)] for j in range(0, 8)]

    def __repr__(self):
        ret = ""
        for x in xrange(8):
            t = []
            for y in xrange(8):
                t.append(self.Fields[y][7 - x])
            ret += str(t) + "\n"
        return ret

    def set(self, x, y, what):
        self[x, y] = what

    def copy(self):
        return copy.deepcopy(self)

    def __getitem__(self, key):
        return self.Fields[key[0]][key[1]]

    def __setitem__(self, key, val):
        self.Fields[key[0]][key[1]] = val

    def swapSides(self):
        board = copy.deepcopy(self.Fields)
        for i in boardCoords:
            now = board[7 - i[0]][7 - i[1]]
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
                self[basic.dst.x, basic.dst.y] = Field.HU_KING
            elif basic.src.x == AIkingPos[0]:
                self[basic.dst.x, basic.dst.y] = Field.AI_KING
            elif basic.dst.x == nullPos[0]: #to /dev/null
                self[basic.src.x, basic.src.y] = Field.EMPTY
            else:
                self[basic.dst.x, basic.dst.y] = self[basic.src.x, basic.src.y]
                self[basic.src.x, basic.src.y] = Field.EMPTY

    def possibleMoves(self):
        moves = []
        for pos in boardCoords:
            if self[pos] == Field.AI_KING:
                moves.extend(kingBeats(self, pos))
        if len(moves) != 0:
            return moves

        for pos in boardCoords:
            if self[pos] == Field.AI:
                moves.extend(pawnBeats(self, pos))
        if len(moves) != 0:
            return moves

        for pos in boardCoords:
            if self[pos] == Field.AI_KING:
                moves.extend(kingMoves(self, pos))
            elif self[pos] == Field.AI:
                moves.extend(pawnMoves(self, pos))
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

    def equal(self, board2):
        for i in xrange(8):
            for j in xrange(8):
                if self[i, j] != board2[i, j]:
                    return False
        return True

    def correctHumanMove(self, board2):
        Template = self.copy()
        Template.swapSides()
        for move in Template.possibleMoves():
            Actual = Template.copy()
            Actual.executeMove(move)
            Actual.swapSides()
            if Actual.equal(board2):
                return True
        return False

    def flatKings(self):
        for i in xrange(8):
            for j in xrange(8):
                if self[i, j] == Field.HU_KING:
                    self[i, j] = Field.HU
                if self[i, j] == Field.AI_KING:
                    self[i, j] = Field.AI

    def boardFromCamera(self, nextBoard):
        now = self.copy()
        now.swapSides()
        #print "nextBoard:"
        #print nextBoard
        for move in now.possibleMoves():
            Actual = now.copy()
            Actual.executeMove(move)
            flat = Actual.copy()
            flat.flatKings()
            flat.swapSides()
            #print "Flat:"
            #print flat

            if flat.equal(nextBoard):
                Actual.swapSides()
                return Actual
        return None


class Shift:
    src = Field([-2, -2])
    dst = Field([-2, -2]) #dummy constants

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
    def add(self, s):
        self.moveList.append(s)


def addToList(_list, _num):
    return [x + _num for x in _list]


def kingBeats(board, pos):
    global pawnBeatsTable
    pawnBeatsTable = []
    for dx, dy in [(-1, -1), (-1, 1), (1, -1), (1, 1)]:
        actual = [pos[0] + dx, pos[1] + dy]
        while 1 <= actual[0] <= 6 and 1 <= actual[1] <= 6:
            if AIFigure(board[actual]):
                break
            if humanFigure(board[actual]) and empty(board[actual[0] + dx, actual[1] + dy]):
                #attacking on actual, moving on Next
                #res.append([Shift(pos, [actual[0] + dx, actual[1] + dy]), Shift(actual, nullPos)])

                #checking for next attacks (like for pawn)
                kingBeatsHelper(board, [actual[0] + dx, actual[1] + dy], pos, [Shift(actual, nullPos)], dy)

                break
            if not empty(board[actual]):
                break
            actual = [actual[0] + dx, actual[1] + dy]

    return pawnBeatsTable


def kingBeatsHelper(board, pos, begin, toClear, direction):
    global pawnBeatsTable
    possibleAttack = 0
    for dx, dy in [(-1, direction), (1, direction)]:
        actual = [pos[0] + dx, pos[1] + dy]
        if 0 <= actual[0] + dx <= 7:
            Next = [actual[0] + dx, actual[1] + dy]
            if 0 <= actual[1] + dy <= 7:
                if humanFigure(board[actual]) and empty(board[actual[0] + dx, actual[1] + dy]):
                    possibleAttack = 1
                    #check next beat on this position
                    Move = [Shift(pos, Next), Shift(actual, nullPos)]
                    board2 = board.copy()
                    board2.executeMove(Move)
                    kingBeatsHelper(board2, Next, begin, toClear + [Shift(actual, nullPos)], direction)

    if possibleAttack == 0 and begin != pos:
        toClear.append(Shift(begin, pos))
        pawnBeatsTable.append(toClear)


def kingMoves(board, pos):
    res = []
    for dx, dy in [(-1, -1), (-1, 1), (1, -1), (1, 1)]:
        actual = [pos[0] + dx, pos[1] + dy]
        while 0 <= actual[0] <= 7 and 0 <= actual[1] <= 7:
            if AIFigure(board[actual]):
                break
            if empty(board[actual]):
                res.append([Shift(pos, actual)])
            actual = [actual[0] + dx, actual[1] + dy]
    return res


pawnBeatsTable = []


def pawnBeats(board, pos):
    global pawnBeatsTable
    pawnBeatsTable = []
    pawnBeatsHelper(board, pos, pos, [])
    return pawnBeatsTable


def pawnBeatsHelper(board, pos, begin, toClear):
    global pawnBeatsTable
    possibleAttack = 0
    for dx, dy in [(-1, 1), (1, 1)]:
        actual = [pos[0] + dx, pos[1] + dy]
        if 0 <= actual[0] + dx <= 7:
            Next = [actual[0] + dx, actual[1] + dy]
            if 1 <= actual[1] + dy <= 6:
                if humanFigure(board[actual]) and empty(board[actual[0] + dx, actual[1] + dy]):
                    possibleAttack = 1
                    #check next beat on this position
                    Move = [Shift(pos, Next), Shift(actual, nullPos)]
                    board2 = board.copy()
                    board2.executeMove(Move)
                    pawnBeatsHelper(board2, Next, begin, toClear + [Shift(actual, nullPos)])
                    #res.append([Shift(pos, [actual[0] + dx, actual[1] + dy]), Shift(actual, nullPos)])

            if actual[1] + dy == 0 and board[pos] == Field.HU:
                if humanFigure(board[actual]) and empty(board[Next]):
                    pawnBeatsTable.append(
                        toClear + [Shift(actual, nullPos), Shift(begin, nullPos), Shift(HUkingPos, Next)])
                    return
                    #res.append([, Shift(pos, nullPos), Shift(actual,nullPos)])

            if actual[1] + dy == 7 and board[pos] == Field.AI:
                if humanFigure(board[actual]) and empty(board[Next]):
                    pawnBeatsTable.append(
                        toClear + [Shift(actual, nullPos), Shift(begin, nullPos), Shift(AIkingPos, Next)])
                    return
                    #res.append([Shift(AIkingPos, [next]), Shift(pos, nullPos),Shift(actual,nullPos)])

    if possibleAttack == 0 and begin != pos:
        toClear.append(Shift(begin, pos))
        pawnBeatsTable.append(toClear)


def pawnMoves(board, pos):
    res = []
    for dx, dy in [(-1, 1), (1, 1)]:
        actual = [pos[0] + dx, pos[1] + dy]
        if 0 <= actual[0] <= 7:
            if 0 <= actual[1] <= 6:
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
