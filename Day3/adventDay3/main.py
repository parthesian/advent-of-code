from collections import defaultdict

symbols = [
    "$", "@", "#", "/", "+", "=", "-", "&", "*", "%"
]
coords_to_nums = defaultdict(list)

# reads the day3 input file
def readFile():
    with open("day3input.txt") as f:
        lines = [line.strip() for line in f]
        return lines

def findPartNums(row_text, row_num, all_text):
    r_sum, i = 0,0
    while i in range(len(row_text)):
        thisNum = ""
        if row_text[i].isnumeric():
            j = i
            while j + 1 < len(row_text) and row_text[j+1].isnumeric():
                thisNum += row_text[i]
                j += 1
            r_sum += searchNums(i, j, row_num, all_text)
            i = j
        i += 1
    return r_sum


def searchNums(left, right, x, all_text):
    p = left
    found_gear = False
    while p <= right:
        for dx in [-1,0,1]:
            for dy in [-1,0,1]:
                lx, rx = x + dx, p + dy
                if lx < 0 or lx >= 140 or rx < 0 or rx >= 140:
                    continue
                # for part 2, for any coordinate with a *, we add the surrounding part numbers
                if all_text[lx][rx] == "*" and not found_gear:
                    coords_to_nums[(lx, rx)].append(int(all_text[x][left:right + 1]))
                    found_gear = True
                if all_text[lx][rx] in symbols:
                    return int(all_text[x][left:right + 1])
        p += 1
    return 0


if __name__ == '__main__':
    newLines = readFile()
    t_sum, idx = 0,0
    for line in newLines:
        tmp = findPartNums(line, idx, newLines)
        t_sum += tmp
        idx = idx + 1
    print("part 1 sum: ", t_sum)

    g_sum = 0
    for pin in coords_to_nums.values():
        if len(pin) != 2:
            continue
        gear_product = pin[0] * pin[1]
        g_sum += gear_product
    print("part 2 sum: ", g_sum)


