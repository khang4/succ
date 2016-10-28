class crab:
    def __init__(self):
        self.ccrab=[];
        self.cccrab=[];

    def add(self,x):
        if x in self.ccrab:
            self.cccrab[self.ccrab.index(x)]+=1;
            return;

        self.ccrab.append(x);
        self.cccrab.append(1);

    def printc(self):
        print(self.ccrab);
        print(self.cccrab);

def main():
    crabb=crab();
    crabb.add(1);
    crabb.add(2);
    crabb.add(1);
    crabb.printc();

main();
