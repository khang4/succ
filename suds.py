def main():
    grid=genGrid();

    addNum(3,1,0,grid);
    addNum(4,2,0,grid);

    printGrid(grid);
    printConstraints(grid);

def genGrid():
    grid=[];
    for x in range(0,9):
        grid.append([]);
        for y in range(0,9):
            grid[x].append([0,set([])]);    

    return grid;

def printGrid(grid):
    for x in grid:
        for y in x:
            print(y[0],end=" ");
        print("");

def printConstraints(grid):
    for x in grid:
        for y in x:
            print(list(y[1]),end=" ");
        print("");

def addNum(num,x,y,grid):
    grid[y][x][0]=num;
    grid[y][x][1].update([-1]);

    for x2 in range(0,9):
        if x2!=x:
            grid[y][x2][1].add(num);

    for y2 in range(0,9):
        if y2!=y:
            grid[y2][x][1].add(num);            

main();
