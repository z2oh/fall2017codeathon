elements = ['h', 'he', 'li', 'be', 'b', 'c', 'n', 'o', 'f', 'ne', 'na', 'mg', 'al', 'si', 'p', 's', 'cl', 'ar', 'k', 'ca', 'sc', 'ti', 'v', 'cr', 'mn', 'fe', 'co', 'ni', 'cu', 'zn', 'ga', 'ge', 'as', 'se', 'br', 'kr', 'rb', 'sr', 'y', 'zr', 'nb', 'mo', 'tc', 'ru', 'rh', 'pd', 'ag', 'cd', 'in', 'sn', 'sb', 'te', 'i', 'xe', 'cs', 'ba', 'la', 'ce', 'pr', 'nd', 'pm', 'sm', 'eu', 'gd', 'tb', 'dy', 'ho', 'er', 'tm', 'yb', 'lu', 'hf', 'ta', 'w', 're', 'os', 'ir', 'pt', 'au', 'hg', 'tl', 'pb', 'bi', 'po', 'at', 'rn', 'fr', 'ra', 'ac', 'th', 'pa', 'u', 'np', 'pu', 'am', 'cm', 'bk', 'cf', 'es', 'fm', 'md', 'no', 'lr', 'rf', 'db', 'sg', 'bh', 'hs', 'mt', 'ds', 'rg', 'cn', 'nh', 'fl', 'mc', 'lv', 'ts', 'og']

elem_sort = ['ac', 'ag', 'al', 'am', 'ar', 'as', 'at', 'au', 'b', 'ba', 'be', 'bh', 'bi', 'bk', 'br', 'c', 'ca', 'cd', 'ce', 'cf', 'cl', 'cm', 'cn', 'co', 'cr', 'cs', 'cu', 'db', 'ds', 'dy', 'er', 'es', 'eu', 'f', 'fe', 'fl', 'fm', 'fr', 'ga', 'gd', 'ge', 'h', 'he', 'hf', 'hg', 'ho', 'hs', 'i', 'in', 'ir', 'k', 'kr', 'la', 'li', 'lr', 'lu', 'lv', 'mc', 'md', 'mg', 'mn', 'mo', 'mt', 'n', 'na', 'nb', 'nd', 'ne', 'nh', 'ni', 'no', 'np', 'o', 'og', 'os', 'p', 'pa', 'pb', 'pd', 'pm', 'po', 'pr', 'pt', 'pu', 'ra', 'rb', 're', 'rf', 'rg', 'rh', 'rn', 'ru', 's', 'sb', 'sc', 'se', 'sg', 'si', 'sm', 'sn', 'sr', 'ta', 'tb', 'tc', 'te', 'th', 'ti', 'tl', 'tm', 'ts', 'u', 'v', 'w', 'xe', 'y', 'yb', 'zn', 'zr']

# TODO: binary search to reduce constant
def is_elem(st):
    return st in elem_sort

# Get the input
word = input()

# We intialize our graph to be filled with empty values
graph = [None] * ((len(word) * 2) - 1)

# Now we fill our graph with valid digraphs and letters
for i, c in enumerate(word):
    if(i != len(word) - 1 and is_elem(c + word[i+1])):
        graph[len(word) + i] = c + word[i+1]
    if(is_elem(c)):
        graph[i] = c

def count(word):
    num = 0
    if len(word) == 1:
        if(is_elem(word)):
            num += 1
    elif len(word) == 2:
        if is_elem(word):
            num += 1
        if is_elem(word[0]) and is_elem(word[1]):
            num += 1
    else:
        digraph = word[-2] + word[-1]
        single = word[-1]
        if is_elem(digraph):
            num += count(word[0:-2])
        if is_elem(single):
            num += count(word[0:-1])
    return num

def count_with_solutions(word):
    return _count_with_solutions(word, [])

def _count_with_solutions(word, arr):
    num = 0
    if len(word) == 1:
        if(is_elem(word)):
            arr.insert(0, word)
            print("Solution!", arr)
            num += 1
    elif len(word) == 2:
        if is_elem(word):
            abc = arr.copy()
            abc.insert(0, word)
            print("Solution!", abc)
            num += 1
        if is_elem(word[0]) and is_elem(word[1]):
            abd = arr.copy()
            abd.insert(0, word[1])
            abd.insert(0, word[0])
            print("Solution!", abd)
            num += 1
    else:
        digraph = word[-2] + word[-1]
        single = word[-1]
        if is_elem(digraph):
            acd = arr.copy()
            acd.insert(0, digraph)
            num += _count_with_solutions(word[0:-2], acd)
        if is_elem(single):
            acs = arr.copy()
            acs.insert(0, single)
            num += _count_with_solutions(word[0:-1], acs)
    return num

print(count_with_solutions(word))
