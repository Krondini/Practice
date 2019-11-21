from sys import argv
from random import shuffle

def createList(givers):

    same = True
    recipients = givers.copy()
    shuffle(recipients)
    while same:
        same = False
        shuffle(recipients)
        for i in range(len(givers)):
            if givers[i] == recipients[i]:
                same = True

    return recipients

def main(args):

    givers = ["Cara", "Gavin", "Cat", "Caitlynn", "Ashley", "Sabrina K.", "Sara",
              "Lauren", "Dani", "Kendall", "Hannah", "Max", "Sam", "Coralie",
              "Jake", "Harshini", "Grace", "Colby", "Garrett"]

    recipients = createList(givers)

    for i in range(len(givers)):
        print("%s -> %s" % (givers[i], recipients[i]))

if __name__ == '__main__':
    main(argv)
