_end = '_end'
nums = {"one": "1",
        "two": "2",
        "three": "3",
        "four": "4",
        "five": "5",
        "six": "6",
        "seven": "7",
        "eight": "8",
        "nine": "9",
        "zero": "0"
        }
written_numbers = ["zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]

# reads the day1 input file
def readFile():
    with open("day1input.txt") as f:
        lines = f.read().splitlines()
        return lines
# makes a trie out of a list of words
def make_trie(words, rev):
    root = dict()
    for word in words:
        current_dict = root
        if not rev:
            for letter in word:
                current_dict = current_dict.setdefault(letter, {})
        else:
            for letter in word[::-1]:
                current_dict = current_dict.setdefault(letter, {})

        current_dict[_end] = _end
    return root
# checks if a word is fully in the trie
def in_trie(trie, word):
    current_dict = trie
    for letter in word:
        if letter not in current_dict:
            return False
        current_dict = current_dict[letter]
    return _end in current_dict
# checks if a word is partially in the trie
# returns 0 if not found, 1 if found, otherwise None
def partial_match(trie, word, index):
    current_dict = trie
    idx = 0
    for letter in word[index:]:
        if letter not in current_dict:
            return 0
        if _end in current_dict[letter]:
            return idx + 1
        current_dict = current_dict[letter]
        idx = idx + 1
def solveLine(line, trie, trie2):
    ret1 = 0
    ret2 = 0
    idx = 0
    for ch in line:
        if ch.isdigit():
            ret1 = ch
            break
        ans = partial_match(trie, line, idx)
        if ans is not None and ans != 0:
            ret1 = nums[line[idx:ans + idx]]
            break
        idx = idx + 1
    idx = 0
    rev_line = line[::-1]
    for ch in rev_line:
        if ch.isdigit():
            ret2 = ch
            break
        ans = partial_match(trie2, rev_line, idx)
        if ans is not None and ans != 0:
            ret2 = nums[rev_line[idx:ans + idx][::-1]]
            break
        idx = idx + 1
    return ret1 + ret2




# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    newLines = readFile()
    sum = 0
    trie = make_trie(written_numbers, False)
    trie2 = make_trie(written_numbers, True)
    idx = 0
    for line in newLines:
        print(line)
        res = solveLine(line, trie, trie2)
        sum = sum + int(res)
        print(res, "new sum = ", sum)
        idx = idx +1
# See PyCharm help at https://www.jetbrains.com/help/pycharm/
