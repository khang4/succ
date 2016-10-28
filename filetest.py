def main():
    col=0;
    row=0;

    with open("test1.txt","r") as infile:
        for x in infile:
            for y in x:
                value=y;
                if value=="-":
                    value=-1;

                mainCrabs.add(col,row,value);
                col+=1;
                row+=1;
                if col>8:
                    col=0;
                if row>8:
                    row=0;

main();
