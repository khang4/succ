baseSet=set([]);

def main():
    bob=set([]);

    for x in range(1,10):
        baseSet.add(x);

    bob.add(1);
    bob.add(2);
    bob.add(3);
    bob.add(7);
    bob.add(9);
    
    print(baseSet.difference(bob));
    print(baseSet);

main();
