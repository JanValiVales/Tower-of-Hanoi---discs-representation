'''
    TOWER OF HANOI
    The goal is to show how the discs are distributed among the pegs after given numbers of moves.
    The binary representation of disk positions will be shown as well: https://en.wikipedia.org/wiki/Tower_of_Hanoi#Binary_solution
    Adjust these variables: num_discs, stop_move
'''
# -*-coding:utf8;-*-
import sys


def main():
    if stop_move > 2 ** num_discs - 1:
        print("The towers are solved after %d moves. You entered number %d." % (2 ** num_discs - 1, stop_move))
    else:
        move_tower(num_discs, "A", "C", "B")


def move_tower(height, from_pole, to_pole, with_pole):
   if height >= 1:
       move_tower(height - 1, from_pole, with_pole, to_pole)
       move_disk(from_pole, to_pole)
       move_tower(height - 1, with_pole, to_pole, from_pole)


def move_disk(fp, tp):
    global count

    if fp == "A":
       itm = start_peg[0]
       del start_peg[0]
    elif fp == "B":
       itm = spare_peg[0]
       del spare_peg[0]
    elif fp == "C":
       itm = final_peg[0]
       del final_peg[0]

    if tp == "A":
       start_peg.insert(0, itm)
    elif tp == "B":
       spare_peg.insert(0, itm)
    elif tp == "C":
       final_peg.insert(0, itm)

    count += 1
    x = str("{0:b}".format(count))
    for _ in range(0, num_discs - len(x), 1):
       x = "0" + x

    if count == stop_move:
        print("%d moves have been made" % count)
        print("{0} moves left to the end".format(2 ** num_discs - 1 - count))
        print("Binary representation of the disk positions: {0}".format(x))
        print("Pegs on towers: {0} {1} {2}".format(start_peg, spare_peg, final_peg))
        sys.exit()

def integers_list(a, b):
    return list(range(a, b + 1))


"""CHANGE HERE THE NUMBER OF DISCS AND NUMBER OF MOVES IN WITCH YOU WANT TO STOP THE GAME"""
num_discs = 20
stop_move = 1043570


count = 0
start_peg = integers_list(1, num_discs)
spare_peg = []
final_peg = []

if __name__ == '__main__':
    main()