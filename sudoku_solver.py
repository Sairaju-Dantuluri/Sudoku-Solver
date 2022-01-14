class Sudoku:

    sudoku = None
    
    def take_input(self):
        sud = []
        for i in range(9):
            sud.append(list(map(int,[s for s in input()])))
        self.sudoku = sud

    def check(self, h, r):
        h[0] -= 1
        r[0] -= 1 
        dic = {0:0}
        for i in range(1,10):
            dic[i] = 0
        for i in range(h[0],h[1]):
            for j in range(r[0],r[1]):
                dic[self.sudoku[i][j]] += 1
                if dic[self.sudoku[i][j]] == 2 and self.sudoku[i][j]!=0:
                    return False
        return True

    def correctness(self):
        # Horizontal correctness
        for i in range(1,10):
            if not(self.check([i,i],[1,9])):
                return False
        # Vertical correctness
        for i in range(1,10):
            if not(self.check([1,9],[i,i])):
                return False
        # boxes 3 X 3 correctness
        for i in range(3):
            for j in range(3):
                if not(self.check([3*i + 1,3*i + 3], [3*i + 1,3*i + 3])):
                    return False
        return True

    def solve(self, x, y):
        # if this something we need to answer and is not given in question
        if self.sudoku[x-1][y-1]==0:
            for i in range(1,10):
                # try for a solution i
                self.sudoku[x-1][y-1] = i
                next = False
                # check if the present i satisfies the sudoku for now
                if self.correctness():
                    # check if the present i satisfies the complete solution of the sudoku
                    # ending condition
                    if x==9 and y==9:
                        return True
                    if y<9:
                        next = self.solve(x,y+1)
                    else:
                        next = self.solve(x+1,1)
                # if it satisfies the solution return True
                if next:
                    return True
                # else continue the loop
            # if no solution satisfies i.e previous block solution is wrong,
            # then empty the present block for other solutions to access this block
            self.sudoku[x-1][y-1] = 0
            return False
        # if already given in the question, proceed to next block
        else:
            if y<9:
                return self.solve(x,y+1)
            else:
                return self.solve(x+1,1)

    def solver(self, sudoku = None):
        print()
        if sudoku!=None:
            self.sudoku = sudoku
        # check for size issues
        if len(self.sudoku)!=9:
            print("size error")
            return False
        size = 0
        for i in range(9):
            size = max(size,len(self.sudoku[i]))
        if size!=9:
            print("size error")
            return False
        # check if the given Sudoku is Valid
        if not(self.correctness()):
            print('Invalid Sudoku')
            return False
        
        # If all conditions satisfy, start solving
        X = self.solve(1,1)
        # Print the solution
        if X:
            for i in range(9):
                st = ''
                for x in self.sudoku[i]:
                    st += (str(x) + ' ')
                print(st)
        else:
            print("Can't find a solution for this Sudoku")
        print()
        return X


if __name__ == '__main__':
    import time
    s = Sudoku()
    sudoku = [[8,7,0,0,2,0,0,4,6],
              [0,6,0,0,0,0,8,9,0],
              [2,0,0,8,0,0,7,1,5],
              [0,8,4,0,9,7,0,0,0],
              [7,1,0,0,0,0,0,5,9],
              [0,0,0,1,3,0,4,8,0],
              [6,9,7,0,0,2,0,0,8],
              [0,5,8,0,0,0,0,6,0],
              [4,3,0,0,8,0,0,7,0]]
    #s.take_input()
    start = time.time()
    s.solver(sudoku)
    end = time.time()
    print(f"Runtime of the program is {end - start} seconds")