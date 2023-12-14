import csv

h = {}

with open('file.csv') as file:
    file = csv.reader(file)
    for index, row in enumerate(file):
        h[index] = [x for x in row[0]]


def roll():
    global h
    # North
    n = 1
    while n < len(h):
        for ROW in range(1, len(h)):
            for item in range(len(h[ROW])):
                if h[ROW][item] == 'O':
                    if h[ROW - 1][item] == 'O' or h[ROW - 1][item] == '#':
                        pass
                    else:
                        h[ROW][item] = '.'
                        h[ROW - 1][item] = 'O'
        n += 1
    # West n has to be restarted
    n = 1
    while n < len(h):
        for item in range(1, len(h[0])):

            for ROW in range(len(h)):
                if h[ROW][item] == 'O':
                    if h[ROW][item - 1] == 'O' or h[ROW][item - 1] == '#':
                        pass
                    else:
                        h[ROW][item] = '.'
                        h[ROW][item - 1] = 'O'

        n += 1
    # South n has to be restarted
    n = 1
    while n < len(h):
        for ROW in range(len(h) - 2, -1, - 1):
            for item in range(len(h[ROW])):
                if h[ROW][item] == 'O':
                    if h[ROW + 1][item] == 'O' or h[ROW + 1][item] == '#':
                        pass
                    else:
                        h[ROW][item] = '.'
                        h[ROW + 1][item] = 'O'
        n += 1
    # East has to be restarted
    n = 1
    while n < len(h):
        for item in range(len(h[0]) - 2, -1, -1):
            for ROW in range(len(h)):
                if h[ROW][item] == 'O':
                    if h[ROW][item + 1] == 'O' or h[ROW][item + 1] == '#':
                        pass
                    else:
                        h[ROW][item] = '.'
                        h[ROW][item + 1] = 'O'

        n += 1


"""
After appending results to list anything over 135 iteration gave a len of 135 it means it repeats itself.
Checking number it has occurrence by 11. Then math 1000000000 - 125 element then when we repeat items. Div by 11 then 
x 11 +125. Gave number x when 6 was missing to 1000000000. Then we choose sixth element.
"""

count = 0
max_length = len(h)
res = 0
rr = []
lista = []
for a in range(200):
    roll()
    for i in h:
        for o in h[i]:
            if o == "O":
                count += 1
        if count > 0:
            res += count * (max_length - i)
            count = 0
    print(res)
    if res not in rr:
        rr.append(res)
    res = 0

print(rr)

