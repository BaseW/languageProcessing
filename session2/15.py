N = int(input('N=?: '))

lines = []
with open('popular-names.txt') as f:
  for line in f:
    lines.append(line)

for i in range(N):
  print(lines[len(lines) - 1 - i])


# # coding: utf-8
# 
# fname = 'hightemp.txt'
# n = int(input('N--> '))
# 
# if n > 0:
#     with open(fname) as data_file:
#         lines = data_file.readlines()
# 
#     for line in lines[-n:]:
#         print(line.rstrip())
# 