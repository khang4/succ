class scell:
    def __init__(self,col,row,box):
        self.m_col=col;
        self.m_row=row;
        self.m_box=box;
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
                tempBox=calcBox(x,y);
                tempCell=scell(x,y,tempBox);
                self.m_cols[x].m_cells.append(tempCell);
                self.m_rows[y].m_cells.append(tempCell);
                self.m_boxes[tempBox].m_cells.append(tempCell);

    def add(self,col,row,value):
        self.m_rows[row].m_cells[col].m_value=value;
        self.m_rows[row].m_cells[col].m_possible.clear();        

        for x in self.m_rows[row].m_cells:
            x.m_possible.discard(value);

        for x in self.m_cols[col].m_cells:
            x.m_possible.discard(value);

        for x in self.m_boxes[calcBox(col,row)].m_cells:
            x.m_possible.discard(value);

    def printValues(self):
        for x in self.m_rows:
            for y in x.m_cells:
                # print(y.m_value,end=" ");
                tempValue=y.m_value;
                if tempValue<0:
                    tempValue="-";
                print("{:>3}".format(tempValue),end="");
            print("");

    def printNumPossible(self):
        for x in self.m_rows:
            for y in x.m_cells:
                # print(y.m_value,end=" ");
                print("{:>3}".format(len(y.m_possible)),end="");
            print("");

    def searchSingles(self):
        for x in self.m_boxes:
            singleFound=set([1,2,3,4,5,6,7,8,9]);
            doubleFound=set([]);

            for y in x.m_cells:                
                if len(y.m_possible)==1:
                    addValue=y.m_possible.pop();
                    self.add(y.m_col,y.m_row,addValue);
                    print("{} added at col {} row {}".format(addValue,y.m_col,y.m_row));

                if y.m_value!=-1:
                    singleFound.discard(y.m_value);
                    doubleFound.add(y.m_value);
                else:
                    tempPossible=y.m_possible.copy();
                    tempSet=singleFound&tempPossible;
                    singleFound-=tempSet;
                    tempPossible-=tempSet;
                    doubleFound|=tempPossible;

            print("unique values: ",end="");
            print(set([1,2,3,4,5,6,7,8,9])-doubleFound);

                
        
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

    for x in range(0,8):
        mainCrabs.add(x,0,x+1)

    mainCrabs.printValues();
    mainCrabs.printNumPossible();

    mainCrabs.searchSingles();

    mainCrabs.printValues();
    mainCrabs.printNumPossible();

    return;

main();
