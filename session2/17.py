# first_cols = []
# with open('popular-names.txt') as f:
#   for line in f:
#     cols = line.split()
# #     print(cols)
#     first_cols.append(cols[0])
# 
# print(first_cols)

# coding: utf-8

fname = 'popular-names.txt'
with open(fname) as data_file:

    set_ken = set()
    for line in data_file:
        cols = line.split('\t')
        set_ken.add(cols[0])

for n in set_ken:
    print(n)
