N = int(input('N=?: '))

lines = []
with open('popular-names.txt') as f:
  for line in f:
    lines.append(line)

for i in range(N):
  print(lines[i])

#  # coding: utf-8
#  
#  fname = 'hightemp.txt'
#  n = int(input('N--> '))
#  
#  with open(fname) as data_file:
#      for i, line in enumerate(data_file):
#          if i >= n:
#              break
#          print(line.rstrip())