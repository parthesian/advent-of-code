colors = {
    "red" : 12,
    "green" : 13,
    "blue" : 14
}
def readFile():
    with open("day2input.txt") as f:
        lines = f.read().splitlines()
        return lines
def processLinePart1(line):
    lpc = line.split(':')
    lpid = int(lpc[0][4:])

    sems = lpc[1].split(';')

    for i in range(len(sems)):
        com = sems[i].split(',')
        for j in range(len(com)):
            spa = com[j].split(' ')
            if int(spa[1]) > colors[spa[2]]:
                return 0
    return lpid
def processLinePart2(line):
    lpc = line.split(':')
    lpp = 1

    sems = lpc[1].split(';')

    maxColors = {
        "red": 0,
        "green": 0,
        "blue": 0
    }
    for i in range(len(sems)):
        com = sems[i].split(',')
        for j in range(len(com)):
            spa = com[j].split(' ')
            maxColors[spa[2]] = max(maxColors[spa[2]], int(spa[1]))
    lpp = maxColors["red"] * maxColors["green"] * maxColors["blue"]
    return lpp


if __name__ == '__main__':
    lines = readFile()
    sum = 0
    for line in lines:
        # lp = processLinePart1(line)
        lp = processLinePart2(line)
        sum = sum + lp
        print(lp, "Sum is now: ", sum)
    print(sum)

