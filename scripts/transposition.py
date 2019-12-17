"""
transpose table
"""

def transposition(table):
    with open(table) as t:
        lists = []
        [lists.append(line.strip().split('\t')) for line in t]
        column = len(lists[0])
        row = len(lists)
        for i in range(column):
            tmplist = [lists[j][i] for j in range(row)]
            with open(table + '.transposition', 'a') as fo:
                fo.write('\t'.join(tmplist) + '\n')
