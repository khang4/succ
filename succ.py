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
        self.m_filled=pow(9,2);

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
        # print("adding {} at col {} row {}".format(value,col,row));
        self.m_rows[row].m_cells[col].m_value=value;
        self.m_rows[row].m_cells[col].m_possible.clear();        

        for x in self.m_rows[row].m_cells:
            x.m_possible.discard(value);

        for x in self.m_cols[col].m_cells:
            x.m_possible.discard(value);

        for x in self.m_boxes[calcBox(col,row)].m_cells:
            x.m_possible.discard(value);

        self.m_filled-=1;
        return self.m_filled;

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
        if self.m_filled==0:
            return 0;

        for i,x in enumerate(self.m_boxes):
            singleFound=set([1,2,3,4,5,6,7,8,9]);
            doubleFound=set([]);

            for y in x.m_cells:                
                if len(y.m_possible)==1:
                    addValue=y.m_possible.pop();
                    self.add(y.m_col,y.m_row,addValue);
                    # print("{} added at col {} row {}".format(addValue,y.m_col,y.m_row));

                if y.m_value!=-1:
                    singleFound.discard(y.m_value);
                    doubleFound.add(y.m_value);
                else:
                    tempPossible=y.m_possible.copy();
                    tempSet=singleFound&tempPossible;
                    singleFound-=tempSet;
                    tempPossible-=tempSet;
                    doubleFound|=tempPossible;

            hiddenSingles=set([1,2,3,4,5,6,7,8,9])-doubleFound;
            print("unique values in box {}: ".format(i),end="");
            print(hiddenSingles);

            if len(hiddenSingles)!=0:
                for y in x.m_cells:
                    tempIntersect=y.m_possible&hiddenSingles;
                    if len(tempIntersect)>0:
                        self.add(y.m_col,y.m_row,tempIntersect.pop());

        return 1;
                
        
def calcBox(col,row):
    return calcBoxConvert(col)+(calcBoxConvert(row)*3);

def calcBoxConvert(num):
    if num<3:
        return 0;
    if num<6:
        return 1;
    return 2;

def loadFile(mainCrabs,filename):
    col=0;
    row=0;

    with open(filename,"r") as infile:
        for x in infile:
            for y in x:
                value=y;
                if value=="\n":
                    break;
                if value!="-":
                    mainCrabs.add(col,row,int(value));
                col+=1;
                if col>8:
                    col=0;
                    row+=1;

def main():
    mainCrabs=crabs();

    loadFile(mainCrabs,"test1.txt");

    while mainCrabs.searchSingles()==1:
        pass;

    mainCrabs.printValues();

    # mainCrabs.printValues();
    # mainCrabs.printNumPossible();

    return;

main();
