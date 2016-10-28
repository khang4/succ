import sys;

def main():
    with open(sys.argv[1],"r") as infile:
        print(infile.read());

main();
