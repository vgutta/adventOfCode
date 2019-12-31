input = open('day2input').read().split(',')


mstlst = [int(x) for x in input]


def attempt(lst):
    pos = 0

    while True:
        opcode = lst[pos]
        intone = lst[pos+1]
        inttwo = lst[pos+2]
        outpos = lst[pos+3]

        if opcode == 1:
            lst[outpos] = lst[intone] + lst[inttwo]
        elif opcode == 2:
            lst[outpos] = lst[intone] * lst[inttwo]
        else:
            assert opcode == 99
            break
        pos += 4
    return lst[0]


for noun in range(100):
    for verb in range(100):
        newlst = [int(x) for x in mstlst]
        newlst[1] = noun
        newlst[2] = verb
        if attempt(newlst) == 19690720:
            print(100 * noun + verb)
