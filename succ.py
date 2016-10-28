class scell:
    def __init__(self,x,y,z):
        self.m_x=x;
        self.m_y=y;
        self.m_z=z;

        self.m_v=-1;
        self.m_possible=set([1,2,3,4,5,6,7,8,9]);

class crab:
    def __init__(self):
        self.m_values=set([]);
        self.m_seen=set([]);
        self.m_doubles=set([]);


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

    graph[0][y][x].m_possible.discard(v);

    #column (y)
    for x2 in graph[0]:
        # print(x2[y].m_y);
        x2[y].m_possible.discard(v);
    
    #row (x)
    for x3 in graph[0][y]:
        #print(x3.m_y);
        x3.m_possible.discard(v);

    #box (z)
    for x4 in graph[1][graph[0][y][x].m_z]:
        #print(x4.m_z);
        x4.m_possible.discard(v);

def printimPossible(graph):
    for x in graph:
        for y in x:
            print(list(set([1,2,3,4,5,6,7,8,9]).difference(y.m_possible)),end=" ");
        print("");

def main():
    #[graph,boxGraph]
    graph=genGraph();

    addCell(1,0,2,graph);
    addCell(2,0,1,graph);

    printimPossible(graph[0]);

main();
