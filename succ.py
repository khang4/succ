class scell:
    def __init__(self):
        self.m_value=-1;
        self.m_possible=set([1,2,3,4,5,6,7,8,9]);

class crab:
    def __init__(self):
        self.m_cells=[];        

class crabs:
    def __init__(self):
        self.m_cols=[];
        self.m_rows=[];
        self.m_boxes=[];

        for x in range(0,9):
            self.m_cols.append(crab());
            self.m_rows.append(crab());
            self.m_boxes.append(crab());

        for x in range(0,9):
            for y in range(0,9):
                tempCell=scell();
                self.m_cols[x].m_cells.append(tempCell);
                self.m_rows[y].m_cells.append(tempCell);
                self.m_boxes[calcBox(x,y)].m_cells.append(tempCell);

    def add(self,col,row,value):
        self.m_rows[row].m_cells[col].m_value=value;
        for x in self.m_rows[row].m_cells:
            x.m_possible.discard(value);

def calcBox(col,row):
    return calcBoxConvert(col)+(calcBoxConvert(row)*3);

def calcBoxConvert(num):
    if num<3:
        return 0;

    if num<6:
        return 1;

    return 2;

def main():
    mainCrabs=crabs();

    mainCrabs.add(3,2,2);

    for x in mainCrabs.m_rows:
        for y in x.m_cells:
            print(y.m_value,end=" ");
        print("");

    return;

main();
