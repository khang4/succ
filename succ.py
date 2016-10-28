class scell:
    m_x=-1;
    m_y=-1;
    m_z=-1;

    m_v=-1;
    m_possible=set([1,2,3,4,5,6,7,8,9]);

    def __init__(self,x,y,z):
        self.m_x=x;
        self.m_y=y;
        self.m_z=z;

def genGraph():
    graph=[];
    boxGraph=[];
    boxCoord=0;

    for z in range(0,9):
        boxGraph.append([]);

    for y in range(0,9):
        graph.append([]);
        for x in range(0,9):
            boxCoord=calcBox(x,y);
            newScell=scell(x,y,boxCoord);
            graph[y].append(newScell);
            boxGraph[boxCoord].append(newScell);

    # graphPrint(graph);
    # boxGraphPrint(boxGraph);

    return [graph,boxGraph];

def calcBox(x,y):
    return calcBox2(x)+(3*calcBox2(y));

def calcBox2(num):
    if num<3:
        return 0;

    if num<6:
        return 1;
        
    return 2;

def graphPrint(graph):
    for x in graph:
        for y in x:
            print(y.m_possible,end=" ");
        print("");

def boxGraphPrint(boxGraph):
    for x in boxGraph:
        for y in x:
            print([y.m_x,y.m_y],end=" ");
        print("");

def addCell(x,y,v,graph):
    graph[0][y][x].m_v=v;

    #column (y)
    for x2 in graph[0]:
        print(x2[y].m_y);
    
    #row (x)
    for x3 in graph[0][y]:
        print(x3.m_y);

    #box (z)
    for x4 in graph[1][graph[0][y][x].m_z]:
        print(x4.m_z);

def main():
    #[graph,boxGraph]
    graph=genGraph();

    addCell(1,3,2,graph);

main();
